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
	freopen ("A-large.in","r",stdin);
    freopen ("out.txt","w",stdout);
    int t,tt,sum,cnt,i,j,maxi,pos,n;
    cin>>t;
    for(tt=1;tt<=t;tt++)
    {
        sum=0;
        cin>>n;
        int arr[26];
        for(i=0;i<n;i++)
        {
            cin>>arr[i];
            sum+=arr[i];
        }
        printf("Case #%d: ",tt);
        while(true)
        {
            maxi=0;
            pos=0;
            for(i=0;i<n;i++)
            {
                if(arr[i]>maxi)
                {
                    maxi=arr[i];
                    pos=i;
                }
            }
            if(maxi<=1)
            {
                break;
            }
            arr[pos]--;
            sum--;
            printf("%c",(65+pos));
            for(i=0;i<n;i++)
            {
                if(arr[i]>(sum/2))
                {
                    arr[i]--;
                    sum--;
                    printf("%c",(65+i));
                    break;
                }
            }
            printf(" ");
        }
        if(maxi==1)
        {
            cnt=0;
            for(i=0;i<n;i++)
            {
                if(arr[i]==1)
                    cnt++;
            }
            while(cnt>2)
            {
                for(i=0;i<n;i++)
                {
                    if(arr[i]==1)
                    {
                        printf("%c ",(65+i));
                        arr[i]--;
                        cnt--;
                        sum--;
                        break;
                    }
                }
            }
            for(i=0;i<n;i++)
            {
                if(arr[i]==1)
                {
                    sum--;
                    arr[i]--;
                    printf("%c",(65+i));
                }
            }

        }
        printf("\n");
    }
    return 0;
}

