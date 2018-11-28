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

vector<int> vec;

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A.out","w",stdout);
	int casos;
	cin >> casos;
	for(int casito=1;casito<=casos;casito++)
    {
        int n, t;
        cin >> n >> t;
        vec.resize(n);
        forn(i,n)
            cin >> vec[i];
        sort(all(vec));
        int res = vec.size();
        int p1 = 0, p2 = vec.size()-1;
        while(p1<p2)
        {
            if(vec[p1]+vec[p2]<=t)
            {
                res--;
                p1++;
                p2--;
            }
            else
            {
                p2--;
            }
        }
        cout << "Case #"<< casito <<": "<<res << endl;
    }
}
