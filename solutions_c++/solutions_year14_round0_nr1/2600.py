#include <cstdio>

int main()
{
  int T;
  scanf("%d",&T);
  for(int t=1;t<=T;t++){
    int S[16]={0};
    int b,a[4][4];
    scanf("%d",&b);
    for(int i=0;i<4;i++){
      for(int j=0;j<4;j++){
	scanf("%d",a[i]+j);
      }
    }
    for(int j=0;j<4;j++){
      S[a[b-1][j]-1]++;
    }
    scanf("%d",&b);
    for(int i=0;i<4;i++){
      for(int j=0;j<4;j++){
	scanf("%d",a[i]+j);
      }
    }
    for(int j=0;j<4;j++){
      S[a[b-1][j]-1]++;
    }
    int k=-1;
    for(int i=0;i<16;i++){
      if(S[i]==2){
	if(k==-1){
	  k=i;
	}
	else{
	  k=-2;
	}
      }
    }
    printf("Case #%d: ",t);
    if(k==-2){
      printf("Bad magician!\n");
    }
    else if(k==-1){
      printf("Volunteer cheated!\n");
    }
    else{
      printf("%d\n",k+1);
    }
  }
  return 0;
}
