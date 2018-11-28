#include<bits/stdc++.h>
#define pb push_back
#define tr(c,i) for(typeof((c).begin() )i = (c).begin(); i != (c).end(); i++)
#define mod 1000000007
#define ii  pair<int,int>

using namespace std;
typedef long long ll;



using namespace std;




int main()
{
    int i,tst,t,j,k,sm,ans,n;
    char s[1010];

freopen("A-large.in", "r", stdin);
freopen("AOUT-large.txt", "w", stdout);
scanf("%d",&t);
for(tst=1;tst<=t;tst++)
{
     scanf("%d %s",&n,&s);
     sm=ans=0;
     sm+=s[0]-'0';
     for(i=1;s[i]!='\0';i++)
     {
         if(sm<i)
         {
             ans+=(i-sm);
             sm=i;
         }
         sm+=(s[i]-'0');
     }

     printf("Case #%d: %d\n",tst,ans);
}



    return 0;
}
