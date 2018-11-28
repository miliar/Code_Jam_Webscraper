/*input

*/

//Template

//Header files
#include <bits/stdc++.h>

//Shortcuts
#define lli long long int
#define fo(i,n) for(i=0;i<n;i++)
#define fi(i,a,n) for(i=a;i<=n;i++)
#define fd(i,n,a) for(i=n;i>=a;i--)
#define modulo 1000000007
#define gi(a) scanf("%d",&a)
#define gs(a) scanf("%s",a)
#define gll(a) scanf("%lld",&a)
#define glf(a) scanf("%lf",&a)
#define gui(a) scanf("%u",&a)
#define f(n) for(i=0;i<n;i++)
#define pn printf("\n")
#define pb push_back
#define mp make_pair
#define pii pair<int,int>
#define min(a,b) (a<b)?a:b
#define max(a,b) (a>b)?a:b

using namespace std;


int main()
{
	freopen ("B-large.in","r",stdin);
    freopen ("out.txt","w",stdout);
    lli t,tt,last,indx,ans;
    string stck;
    gll(t);
    for(tt=1;tt<=t;tt++)
    {
        cin>>stck;
        last = stck.length()-1;
        ans=0;
        while(true)
        {
            while(last>=0)
            {
                if(stck[last]=='+')
                    last--;
                else
                    break;
            }

            if(last<0)
                break;
            indx=-1;
            while(indx+1<=last)
            {
                if(stck[indx+1]=='+')
                    indx++;
                else
                    break;
            }

            if(indx>=0)
            {
                ans++;
                for(int i=0;i<(indx+1)/2;i++)
                {
                    char temp = stck[i];
                    stck[i]=stck[indx-i];
                    stck[indx-i]=temp;
                }
                for(int i=0;i<=indx;i++)
                {
                    if(stck[i]=='-')
                        stck[i]='+';
                    else if(stck[i]=='+')
                        stck[i]='-';
                }
            }
            if(indx<last)
            {
                ans++;
                for(int i=0;i<(last+1)/2;i++)
                {
                    char temp = stck[i];
                    stck[i]=stck[last-i];
                    stck[last-i]=temp;
                }
                for(int i=0;i<=last;i++)
                {
                    if(stck[i]=='-')
                        stck[i]='+';
                    else if(stck[i]=='+')
                        stck[i]='-';
                }
            }
        }
        printf("Case #%lld: %lld\n",tt,ans);
    }
    return 0;
}

