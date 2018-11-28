//Bismillahir Rahmanir Rahim
/******Harun Or Rashid******/
/***********Template Starts Here***********/
#include<bits/stdc++.h>
using namespace std;

#define MEM(a,b) memset(a,b,sizeof(a))
#define CLR(a) memset(a,0,sizeof(a))
#define MAX(a,b) ((a)>(b)?(a):(b))
#define MIN(a,b) ((a)>(b)?(b):(a))
#define ABS(a) ((a)>0? (a):(-(a)))
#define SQ(a) ((a)*(a))
#define SZ(a) (int)a.size()
#define FORN(i,n) for(i=1;i<=n;i++)
#define FORAB(i,a,b) for(i=a;i<=b;i++)
#define ALL(V) V.begin(),V.end()
#define pb(a) push_back(a)
#define pr(a) cout<<a<<endl
#define SQR(a) ((a)*(a))
#define pf printf
#define sf scanf
#define mp make_pair
#define PI acos(-1)
#define xx first
#define yy second
#define eps 10e-9

typedef int D;
typedef long long int LLD;
typedef unsigned long long int LLU;
typedef vector<D> VI;
typedef set<D> SI;
typedef vector<D>::iterator Viti;

/***********Template Ends Here***********/

int main()
{
//    ios_base::sync_with_stdio(false);
    int T,cs,s,i,cnt,tt,digit;
    scanf("%d",&T);
    for(cs=1; cs<=T; cs++)
    {
        scanf("%d",&s);
        char str[s+1];
        scanf("%s",str);
        cnt=tt=0;
        for(i=0; str[i]; i++)
        {
            if(str[i]=='0') continue;
            if(i<=tt)
            {
                tt+=(str[i]-'0');
                continue;
            }
            cnt+=(i-tt);
            tt+=(i-tt)+(str[i]-'0');
        }
        printf("Case #%d: %d\n",cs,cnt);
    }
    return 0;
}
