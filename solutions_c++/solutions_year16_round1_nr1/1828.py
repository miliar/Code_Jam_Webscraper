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
         string str,ans;
         
         int l1;
         cin>>str;
         ans+=str[0];
         for(int i=1;i<str.size();i++)
         {
             if((int)str[i]>=(int)ans[0])
             {
                 ans+='a';
                 for(int j=i+1;j>=1;j--)
                   ans[j]=ans[j-1];
                 ans[0]=str[i];
               //  cout<<ans<<"first\n";
             }
             else
             {   
                 ans+=str[i];
                 //cout<<ans<<"second\n";
             }
         }
         //string ans=ans1+ans2;
         cout<<"Case #"<<k<<": "<<ans<<"\n";
      //   printf("%s\n",ans);
            k++;
}
}