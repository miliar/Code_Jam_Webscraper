/*************************************
**----------------------------------**
*|**********************************|*
*|*  CODE By : Mohd. Ausaf Jafri   *|*
*|*     ECE, MNNIT , Allahabad     *|*
*|*                                *|*
*|*      ausafjafri@gmail.com      *|*
*|*   "Think Twice, Code Once"     *|*
*|**********************************|*
**----------------------------------**
**************************************/

#include<bits/stdc++.h>
using namespace std;

#define ll long long
#define vi(v,size) vector<int>v(size) 
#define upto(n) for(int i=0;i<n;i++)
#define from(a,b) for(int i=a;i<=b;i++)
#define rev(a,b) for(int i=a;i>=b;i--)
#define mp make_pair
#define pb push_back
#define mod 1000000007

#define inc(c) scanf("%c",&c);
#define ins(s) scanf("%s",s);
#define ind(n) scanf("%d",&n);
#define inlld(n) scanf("%lld",&n);
#define ind2(n,m) scanf("%d%d",&n,&m);
#define inlld2(n,m) scanf("%lld%lld",&n,&m);

#define opc(c) printf("%c\n",c);
#define ops(s) printf("%s\n",s);
#define opd(n) printf("%d\n",n);
#define oplld(n) printf("%lld\n",n);
#define opd2(n,m) printf("%d %d\n",n,m);
#define oplld2(n,m) printf("%lld %lld\n",n,m);

int main()
{
 int tt,cas=1;
    ind(tt)
        while(tt--)
        {
            ll n;
            int num;
            inlld(n)
            int arr[3000],ans[3000],k=0;
            n=2*n*n-n;
            for(int i=0;i<3000;i++)
                arr[i]=0;
            upto(n)
            {
                ind(num)
                    arr[num]++;
            }
            printf("Case #%d:",cas);
            for(int i=1;i<=3000;i++)
            {
                if(arr[i])
                {
                    if(arr[i]%2!=0)
                        cout<<" "<<i;
                }
            }
           
            cas++;
           
                
            printf("\n");
        }
}