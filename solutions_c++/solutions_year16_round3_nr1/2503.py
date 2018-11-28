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
    int tt,k=1;
    ind(tt)
    while(tt--)
    {
        int n,sum=0;
        char ch='A';
        vector<pair<int,char> >v;
        ind(n)
        int arr[n];
        upto(n)
        {ind(arr[i])
          sum+=arr[i];
         v.pb(mp(arr[i],ch));
         ch++;
        }
        sort(v.begin(),v.end());
        printf("Case #%d: ",k);
        for(int i=n-1;i>0;i--)
        {  int times=v[i].first-v[i-1].first;
         //  cout<<times;
           while(times--)
           {
               for(int j=n-1;j>=i;j--)
                   cout<<v[j].second<<" ";
               
           }
        }
        int last=v[0].first;
        if(n%2!=0)
        {
            upto(last)
            cout<<v[n-1].second<<" ";
            upto(last)
            for(int j=n-2;j>=0;j-=2)
            cout<<v[j].second<<v[j-1].second<<" ";
        }
        else
        {
            upto(last)
            for(int j=n-1;j>=0;j-=2)
            cout<<v[j].second<<v[j-1].second<<" ";
        }
        printf("\n");
        k++;
    }
}