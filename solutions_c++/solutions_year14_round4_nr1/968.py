
#define ll long long
#define vi vector <int>
#define pii pair <int,int>
#define FOR(i, a, b) for (i = (a); i <= (b); i++)
#define REP(i, a) for (i = 0; i < (a); i++)
#define ALL(v) (v).begin(), (v).end()
#define SET(a, x) memset((a), (x), sizeof(a))
#define SZ(a) ((int)(a).size())
#define CL(a) ((a).clear())
#define SORT(x) sort(ALL(x))
#define mp make_pair
#define pb push_back
#define MAX(a,b) ((a)>(b)?(a):(b))
#define MIN(a,b) ((a)<(b)?(a):(b))

#define filer() freopen("in.txt","r",stdin)
#define filew() freopen("out.txt","w",stdout)

#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <queue>
#include <cassert>


using namespace std;



template<class T>void debug(vector<T>v)
{
    for(int i=0;i<v.size();i++)cout<<v[i]<<" ";cout<<endl;
}

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("aout1.txt","w",stdout);

    int T,n,i,j,k,x;
    cin>>T;

    for(int ks=1;ks<=T;ks++)
    {
        cin>>n>>x;
        vi v(n);
        multiset<int>S;
        for(i=0;i<n;i++)cin>>v[i];
        SORT(v);

        for(i=0;i<n;i++)S.insert(v[i]);

        int ans=0;


        while(!S.empty())
        {
            int a=*S.begin();

            S.erase( S.find(a) );

            int b=x-a;
            set<int>::iterator it=S.upper_bound( b );

            if(it!=S.begin())
            {
                it--;
                S.erase(it);
            }

            ans++;

        }


        printf("Case #%d: %d\n",ks,ans);




    }
    return 0;
}












