#include<algorithm>
#include<cmath>
#include<cstdio>
#include<iostream>
#include<map>
#include<queue>
#include<set>
#include<sstream>
#include<string>
#include<vector>

#define forn(i,n) for(int i=0;i<(int)(n);i++)
#define dforn(i,n) for(int i=(int)(n)-1;i>=0;i--)
#define all(v) v.begin(),v.end()

using namespace std;

int calc(vector<long long> vec)
{
    int n = vec.size();
    if(n==1)
        return 0;
    int mn = 0;
    forn(i,vec.size())
    if(vec[i]<vec[mn])
        mn = i;
    int res = min(mn,(int)vec.size()-1-mn);
    vector<long long> aux;
    forn(i,n)
    if(i!=mn)
        aux.push_back(vec[i]);
    return res + calc(aux);
}

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B.out","w",stdout);
	int casos;
	cin >> casos;
	for(int casito=1;casito<=casos;casito++)
    {
        int n;
        cin >> n;
        vector<long long> vec;
        vec.resize(n);
        forn(i,n)
            cin >> vec[i];
        int res = calc(vec);
        cout << "Case #"<< casito <<": " << res << endl;
    }
}
