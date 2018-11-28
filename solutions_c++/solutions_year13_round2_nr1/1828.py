#include<cstdio>
#include<algorithm>
#include<cstring>
#define INF 1<<28
using namespace std;


int N,DP[105];
int motes[105];

int func(int indx,int armin)
{
   if(indx==N) return 0;
   if(DP[indx]!=-1) return DP[indx];
   int tmp1,tmp2,Ans;
   if(armin>motes[indx])
   {
      tmp1=func(indx+1,armin+motes[indx]);
      Ans=tmp1;                  
   }
   else
   {
      if(armin==1) tmp1=INF;
      else
      {
        tmp1=func(indx,armin+armin-1);//increasing
        tmp1++;
      }
      tmp2=func(N,armin);
      
      tmp2+=(N-indx); 
      Ans=min(tmp1,tmp2);
      
   }
   return DP[indx]=Ans;
}
int main()
{
    int T,i,it,cnt,ind,Ans,arm;
    freopen("A-large.in","r",stdin);
    freopen("A-large.in.out","w",stdout);
    scanf("%d",&T);
    for(it=1; it<=T;it++)
    {
       scanf("%d%d",&arm,&N);
       for(i=0; i<N; i++) scanf("%d",&motes[i]);
       
       sort(motes,motes+N);
       memset(DP,-1,sizeof(DP));
       Ans=func(0,arm);
       printf("Case #%d: %d\n",it,Ans);      
    }
    return 0;
}
