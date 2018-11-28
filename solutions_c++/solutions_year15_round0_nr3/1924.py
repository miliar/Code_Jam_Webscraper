#include <iostream>
#include <cstdio>
#include <algorithm>

#define LL long long

using namespace std;
char s[23333333],xt;
int s1[23333333],s2[23333333],T;
LL n,x;

int work(char c,int ans);

void check(){
    int ans;
    for(LL i=0;i<=n-1;i++){
        ans=work(s[i],ans);
        s1[i]=ans;
    }
}
int work(char c,int ans){
     if(ans==1){
          if(c=='i')ans=2;
          else if(c=='j')ans=3;
          else if(c=='k')ans=4;
     }
     else if(ans==2){
          if(c=='i')ans=-1;
          else if(c=='j')ans=4;
          else if(c=='k')ans=-3;
     }
     else if(ans==3){
          if(c=='i')ans=-4;
          else if(c=='j')ans=-1;
          else if(c=='k')ans=2;
     }
     else if(ans==4){
          if(c=='i')ans=3;
          else if(c=='j')ans=-2;
          else if(c=='k')ans=-1;
     }
     else if(ans==-1){
          if(c=='i')ans=-2;
          else if(c=='j')ans=-3;
          else if(c=='k')ans=-4;
     }
     else if(ans==-2){
          if(c=='i')ans=1;
          else if(c=='j')ans=-4;
          else if(c=='k')ans=3;
     }
     else if(ans==-3){
          if(c=='i')ans=4;
          else if(c=='j')ans=1;
          else if(c=='k')ans=-2;
     }
     else if(ans==-4){
          if(c=='i')ans=-3;
          else if(c=='j')ans=2;
          else if(c=='k')ans=1;
     }
     return ans;
}
int main()
{
	 freopen("c.in","r",stdin);
	 freopen("c.out","w",stdout);
     scanf("%d",&T);
for(int t=1;t<=T;t++){
     int ans=1;
     scanf("%lld %lld",&n,&x);
     scanf("%s",s);
     if(x>13)for(LL i=13;i<=x;i++)if(i%(LL)4==x%(LL)4){x=i;break;}
     for(LL i=n;i<=n*x-1;i++)s[i]=s[i-n];n=n*x;
     check();
     for(LL i=0;i<=n-1;i++){
        ans=work(s[i],ans);
        s1[i]=ans;
    }
     if(s1[n-1]!=-1){printf("Case #%d: NO\n",t);continue;}
     ans=1;
     for(LL i=n-1;i>=0;i--){
            int now;
            if(s[i]=='i')now=2;
            else if(s[i]=='j')now=3;
            else if(s[i]=='k')now=4;
            if(ans==1)ans=now;
            else if(ans==2)ans=work('i',now);
            else if(ans==3)ans=work('j',now);
            else if(ans==4)ans=work('k',now);
            else if(ans==-1)ans=-now;
            else if(ans==-2)ans=-work('i',now);
            else if(ans==-3)ans=-work('j',now);
            else if(ans==-4)ans=-work('k',now);
            s2[i]=ans;
    }
    LL i,j;
    for(i=0;i<=n;i++)if(s1[i]==2)break;
    if(s1[i]!=2){
        printf("Case #%d: NO\n",t);
        continue;}
    for(j=i+1;j<=n;j++)if(s2[j]==4)break;
    if(s2[j]!=4){printf("Case #%d: NO\n",t);continue;}
       printf("Case #%d: YES\n",t);}
     return 0;
}
