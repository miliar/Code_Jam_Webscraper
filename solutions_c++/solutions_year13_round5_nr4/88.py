#include <cstdio>
#include <cstring>

int main()
{
  int T;
  scanf("%d",&T);
  for(int C=1;C<=T;C++){
    char s[201];
    scanf("%s",s);
    int n=strlen(s);
    static double dp[1<<20];
    dp[0]=0;
    for(int i=1;i<1<<20;i++){
      int c=0;
      for(int k=n-1;!((i>>k)&1);k--){
	c++;
      }
      dp[i]=0;
      for(int j=0;j<n;j++){
	if(!((i>>j)&1)){
	  c++;
	}
	else{
	  /*if(i==3){
	    printf("%lf %d\n",dp[i^(1<<j)],c);
	    }*/
	  dp[i]+=dp[i^(1<<j)]*(c+1)/n+(double)(n+n-c)*(c+1)/2/n;
	  c=0;
	}
      }
    }
    int I=0;
    for(int i=0;i<n;i++){
      if(s[n-i-1]=='.'){
	I=2*I+1;
      }
      else{
	I=2*I;
      }
    }
    printf("Case #%d: %.10lf\n",C,dp[I]);
  }
  return 0;
}
