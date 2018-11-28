#include<iostream>
#include<cstdio>
#include<cmath>
using namespace std;
long long m[]={
1LL,
4LL,
9LL,
121LL,
484LL,
10201LL,
12321LL,
14641LL,
40804LL,
44944LL,
1002001LL,
1234321LL,
4008004LL,
100020001LL,
102030201LL,
104060401LL,
121242121LL,
 123454321LL
, 125686521LL,
 400080004LL,
404090404LL,
 10000200001LL,
 10221412201LL ,
  12102420121LL,
 12345654321LL,
40000800004LL,
 1000002000001LL,
 1002003002001LL,
  1004006004001LL,
  1020304030201LL
, 1022325232201LL,
 1024348434201LL,
 1210024200121LL,
  1212225222121LL,
   1214428244121LL
   ,1230127210321LL,
     1232346432321LL
, 1234567654321LL,
 4000008000004LL,
 4004009004004LL};
int main()
 {
        long long t,i,a,b,ans=0,ans1=0,j;
        int st,end;
        freopen("3.txt","r",stdin);
        freopen("3a.txt","w",stdout);
        cin>>t;
        for(int xx=1;xx<=t;xx++)
        {
            ans=0;ans1=0;
            scanf("%lld%lld",&a,&b);
            //a;b;
         //   if(a==b) ans=0;
         //   else
            {
                for(int i=0;i<40;i++)
                {
                    if(m[i]<a&&m[i]<b)
                        continue;
                    else if(m[i]==a)
                        ans++;
                    else if(m[i]<b)
                        ans++;
                    else if(m[i]==b)
                        ans++;
                    else break;
                }
            }
            cout<<"Case #"<<xx<<": "<<ans<<endl;

        }
        return 0;
}
