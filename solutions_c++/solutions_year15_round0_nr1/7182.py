#include <bits/stdc++.h>
/* all header files included */

#define mod         1000000007
#define pi          acos(-1.0)
#define eps         1e-9

#define fs          first
#define sc          second
#define pb(a)       push_back(a)
#define mp(a,b)     make_pair(a,b)
#define sp          printf(" ")
#define nl          printf("\n")

#define set0(a)     memset(a,0,sizeof(a))
#define setneg(a)   memset(a,-1,sizeof(a))
#define setinf(a)   memset(a,126,sizeof(a))

#define tc1(x)      printf("Case %d: ",x)
#define tc2(x)      fprintf(fp,"Case #%d: ",x)
#define tc3(x)      printf("Case %d:\n",x)
#define tc4(x)      printf("Case #%d:\n",x)

#define pr1(x)      cout<<x<<"\n"
#define pr2(x,y)    cout<<x<<" "<<y<<"\n"
#define pr3(x,y,z)  cout<<x<<" "<<y<<" "<<z<<"\n"
/* defining macros */

using namespace std;

/* template functions */

typedef long long LL;
typedef unsigned long long ULL;
typedef pair<int, int>pii;
typedef pair<LL, LL>pll;
typedef pair<double, double>pdd;
typedef vector<int>vi;
typedef vector<LL>vll;
typedef vector<double>vd;
/* type definition */


int tc=1;
const long long int mx=100000;
/* global declaration */

int main()
{
    int t,i,ans,n,extra;
    char str[1000+5];
    FILE *f,*fp;
    f=fopen("A-large.in","r");
    fp=fopen("StandingLarge.txt","w");
    fscanf(f,"%d",&t);
    //scanf("%d",&t);
    while(t--)
    {
        fscanf(f,"%d %s",&n,str);
       // scanf("%d %s",&n,str);
        ans=0;
        extra=0;
        for(i=0; i<=n; i++)
        {
            if(i==0)
            {
                if(str[i]=='0')
                    ans++;
                else if(str[i]>'1')
                    extra+=(str[i]-'0')-1;
            }
            else
            {
                if(str[i]=='0' && extra)
                    extra--;
                else if(str[i]=='0' && extra==0)
                    ans++;
                else if(str[i]>'1')
                    extra+=(str[i]-'0')-1;
            }
        }
        //pr1(ans);
        tc2(tc++);
        fprintf(fp,"%d\n",ans);
    }
    fclose(fp);
    fclose(f);
    return 0;
}

