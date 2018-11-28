#include<bits/stdc++.h>
using namespace std;
#define s(n) scanf("%d",&n)
#define sl(n) scanf("%lld",&n)
#define ss(n) scanf(" %s",n)
#define s2(a,b) scanf("%d %d",&a,&b)
#define pb push_back
#define mp make_pair
#define vi vector<int>
#define ii pair<int,int>
#define F first
#define S second
#define P printf
#define E <<endl
#define ll long long

int main()
{
  freopen("A-large1.in", "r",stdin);
     freopen("mm_op2.txt", "w" ,stdout);
       int t,c;
     s(t);
     for(c=1;c<=t;c++)
     {
       int n,i;
       s(n);
       int a[n+1];
       for(i=0;i<n;i++)
        s(a[i]);
        int md=0,d;
        ll s1=0,s2=0;
       //case 1
       for(i=1;i<n;i++)
       {
         d=a[i]-a[i-1];
          if(d<0)
            {
              s1+=abs(d);
              if(-d>md)
                md=-d;
            }
       }
//cout<<md;
       int mps10=md;
       int mps=ceil(mps10/10);
	//	cout<<mps10;
       for(i=0;i<n-1;i++)
       {
        /* d=a[i+1]-a[i];
         if(d<=0)
          s2+=min(a[i],mps10);
         else
          s2+=a[i];*/
          if(a[i]<mps10)
          s2+=a[i];
          else
          s2+=mps10;

       //   cout<<s2<<" ";
       }

        P("Case #%d: %lld %lld\n",c,s1,s2);
     }

}
