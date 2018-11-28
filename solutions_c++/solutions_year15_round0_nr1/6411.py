#include<stdio.h>
#include<algorithm>
#include<ctype.h>
#include<stack>
#include<queue>
#include<string.h>
#include<vector>
#include<math.h>
#include<map>
using namespace std;
#define MAX(a,b) ( (a>b)? (a) : (b) )
#define MIN(a,b) ( (a<b)? (a) : (b) )
#define forab(i,a,b) for(int i=a;i<=b;i++)
#define forabd(i,a,b) for(int i=a;i>=b;i--)
#define pb(a) push_back(a)
#define ll long long
#define forabL(i,a,b) for(ll int i=a;i<=b;i++)
char s[10000002];
int f[1002];
int main()
{
    FILE *ifp, *ofp;
    ifp=fopen("A-large.in", "r");
    ofp=fopen("output","w");
    int T,n;
    fscanf(ifp,"%d ",&T);


    forab(j,1,T)
    {
        fscanf(ifp,"%d",&n);
        fscanf(ifp,"%s",s);
        int lim=strlen(s)-1;

        forab(i,0,lim)
        f[i]=s[i]-'0';

        int c=f[0];
        int ans=0;
        forab(i,1,n)
        {
            if(c<i)
            {
                ans+=(i-c);
                c+=f[i]+i-c;
            }
            else
                c+=f[i];
        }
        fprintf(ofp,"Case #%d: %d\n",j,ans);
    }


	return 0;
}
