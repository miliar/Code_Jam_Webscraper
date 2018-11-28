#include<iostream>
#include<stdio.h>
#include<algorithm>
#include<vector>
#include<cstring>
#define MAX(a,b) (a>b?a:b)
#define MIN(a,b) (a<b?a:b)
#define pb push_back
#define mp make_pair
#define F first
#define S second
using namespace std;
int i,j,n,t,ans,T,cur;
long long a[13],X;

main()
{freopen("A-small-attempt8.in","r",stdin);
 freopen("out.txt","w",stdout);
 scanf("%d",&T);
 for(t=1;t<=T;t++){
      scanf("%lld%d",&X,&n);
       for(i=1;i<=n;i++)scanf("%lld",&a[i]);
       sort(a+1,a+n+1);
       ans=0;
       if(X==1){cout<<"Case #"<<t<<": "<<n<<endl;continue;}
       for(i=1;i<=n;i++){
          cur=ans;
          while(X<=a[i])X+=X-1,ans++;
          X+=a[i];

       if(cur+n-i+1<ans){ans=cur+n-i+1;break;}
       }

     cout<<"Case #"<<t<<": "<<ans<<endl;
    // system("pause");
   }

}
