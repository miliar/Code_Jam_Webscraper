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
     freopen("A-large.in", "r",stdin);
     freopen("A-op-large.txt", "w" ,stdout);
     int t,c;
     s(t);
     for(c=1;c<=t;c++)
     {
          int sm;
          s(sm);

          string shy;
          cin>>shy;

          int len=sm+1;
          int i;
          ll cnt=0,req=0,tmp;
		//	cout<<len<<shy[1];
          for(i=0;i<len;i++)
          {
          //	cout<<i<<" "<<cnt<<"  ";
               if(i>cnt)
               {
                    tmp=i-cnt;
                    req+=tmp;
                    cnt+=tmp;
               }
          //     cout<<req;
               cnt+=(shy[i]-'0');
          }
         // Case #1: 0
          P("Case #%d: %lld\n",c,req);
     }
}
