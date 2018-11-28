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
int main()
{
    FILE *ifp, *ofp;
    char G[]="GABRIEL\0";
    char R[]="RICHARD\0";
    ifp=fopen("D-small-attempt0.in", "r");
    ofp=fopen("outputCJ3","w");
    int T,x,r,c;
    fscanf(ifp,"%d ",&T);

    int ans;
    forab(j,1,T)
    {
        fscanf(ifp,"%d%d%d",&x,&r,&c);
        int a=MIN(r,c);
        int b=MAX(r,c);
        switch(x)
        {
        case 1:
              ans=1; // ans=1 means Gab
              break;
        case 2:
            if( (r%2)&& (c%2))
                ans=0;
            else
                ans=1;
            break;
        case 3:
            if(a==2 &&b==3)
                ans=1;
            else if(a==3&&b==3)
                ans=1;
            else if(a==3 && b==4)
                ans=1;
            else
                ans=0;
            break;
        case 4:
            if(a==3&&b==4)
                ans=1;
            else if(a==4 && b==4)
                ans=1;
            else ans=0;
                break;
        };
            if(ans)
            fprintf(ofp,"Case #%d: %s\n",j,G);
            else
            fprintf(ofp,"Case #%d: %s\n",j,R);

    }


	return 0;
}
