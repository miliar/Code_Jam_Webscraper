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

lli power(lli a, lli b)
{
    lli prod=1;
    for(lli i =0;i<b;i++)
    {
        prod*=a;
    }
    return prod;
}

int main()
{
	freopen ("C-small-attempt0.in","r",stdin);
    freopen ("out.txt","w",stdout);
    lli res[9];
    lli t,tt,n,reqd,i,j,indx,flag,num,k;
    cin>>t;
    for(tt=1;tt<=t;tt++)
    {
        cin>>n;
        cin>>reqd;
        printf("Case #1:\n");
        for(i=32769;i<=65535;i+=2)//32769
        {
            string binary = bitset<16>(i).to_string();
            for(j=2;j<=10;j++)
            {
                num=0;
                indx=0;
                for(k=binary.length()-1;k>=0;k--)
                {
                    num+=(power(j,indx))*(binary[k]-'0');
                    indx++;
                }
                flag=0;
                for(k=2;k<=sqrt(num);k++)
                {
                    if(num%k==0)
                    {
                        flag=1;
                        res[j-2]=k;
                        break;
                    }
                }
                if(flag==0)
                {
                    break;
                }
                else
                {
                    if(j==10)
                    {
                        reqd--;
                        cout<<binary<<" ";
                        for(k=0;k<8;k++)
                            printf("%lld ",res[k]);
                        printf("%lld\n",res[8]);
                    }
                }
            }
            if(reqd<=0)
                break;
        }
    }
    return 0;
}

