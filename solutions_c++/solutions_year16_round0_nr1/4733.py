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
   int tt,test=1;
    ind(tt)
    while(tt--)
    {
        ll n,m,ans;
        inlld(n)
        int arr[10]={0},flag=0;
        if(n==0)
            printf("Case #%d: INSOMNIA\n",test);
        else
        {
         for(int i=1;i<=100;i++)
         {
            flag=1;
            m=i*n;
            while(m>0)
            {
                arr[m%10]++;
                m=m/10;
            }
             
            for(int j=0;j<10;j++)
            {
                if(arr[j]==0)
                {
                 flag=0;
                 break;
                }
                
            }
             if(flag)
             {   ans=i*n;
                 break;
             }
         }
         printf("Case #%d: %lld\n",test,ans);    
        }
        test++;
    }
}