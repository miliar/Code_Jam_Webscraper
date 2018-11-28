/*===============*\
|  ID: TMANDZU    |
|    LANG: C++    |
\*===============*/
//Tornike Mandzulashvili
//#pragma comment(linker,"/STACK:256000000")
#include <time.h>
#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
#include <stack>
#include <math.h>
#include <vector>
#include <string>
#include <map>
#include <queue>
#include <iostream>
#include <set>

#define EPS 0.000000001
#define Pi 3.1415926535897932384626433832795028841971
#define hash1 1000003
#define hash2 1000033
#define md 1000000007
#define INF 1000000500
#define mp make_pair
#define pb push_back
#define S size()
#define MX(aa,bb) (aa>bb?aa:bb)
#define MN(aa,bb) (aa<bb?aa:bb)
#define fi first
#define se second
#define PI pair < int,int >
#define REP(i,a,n) for(i=a;i<n;i++)
#define sc scanf
#define pt printf
#define big long long
#define VI vector <int>
#define DID (long long)


using namespace std;

int T,i,j,n,t,flag,ans,now;
string s;

bool F(char k)
{
    if (k=='a') return 0;
    if (k=='e') return 0;
    if (k=='i') return 0;
    if (k=='o') return 0;
    if (k=='u') return 0;
    return 1;
}

main()
{
    freopen("text.in","r",stdin);   freopen("text.out","w",stdout);

    cin>>T;
    for (t=1;t<=T;t++)
    {
        cin>>s;
        cin>>n;

        ans=0;

        for (i=0;i<s.S;i++)
        {
            j=i;
            flag=0;
            now=0;

            while (j<s.S)
            {
                if (F(s[j])) now++; else now=0;

                if (now>=n)
                {
                    ans+=s.S-j;
                    break;
                }

                j++;
            }

        }

        cout<<"Case #"<<t<<": "<<ans<<endl;
    }
}
