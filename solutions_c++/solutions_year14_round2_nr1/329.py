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

template<class X>void debug(vector<X>&v){for(int i=0;i<v.size();i++)cout<<v[i]<<" ";cout<<endl;}

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("a2.out","w",stdout);
    int i,j,k,t,n,ks=0;
    cin>>t;
    while(t--)
    {


        ks++;
        cin>>n;
        vector<string>s(n);
        for(int i=0;i<n;i++)cin>>s[i];


        vector<char>sid;
        sid.pb(s[0][0]);
        for(int i=0;i<s[0].size();i++)if(sid.back()!=s[0][i])sid.pb( s[0][i] );


        vi pos(n,0);
        int ans=0;

       // debug(sid);

        for(int i=0;i<sid.size();i++)
        {

            char c=sid[i];
            vector<int>v(n,0);


            for(int j=0;j<n;j++)
            {
                if( pos[j]>=s[j].size() || s[j][pos[j]]!=c )goto hell;

                while( pos[j]<s[j].size() && s[j][pos[j]]==c )
                {
                    v[j]++;
                    pos[j]++;
                }
            }

           // cout<<c<<endl;
          //  debug(v);

            SORT(v);


            int mid=v[v.size()/2];
            for(int j=0;j<v.size();j++)ans+=abs( mid-v[j] );
        }


        for(int i=0;i<n;i++)if(pos[i]!=s[i].size())goto hell;

        printf("Case #%d: %d\n",ks,ans);
        continue;

        hell:
        printf("Case #%d: Fegla Won\n",ks);


    }

    return 0;
}
