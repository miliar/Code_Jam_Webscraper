#include<stdio.h>
int main(){
  int t;
  //for small input N<=10 AND M<=10
  int a[100][100];
  
  scanf("%d",&t);
  for(int k=1;k<(t+1);k++){
    int N,M;
    bool status=true;
    scanf("%d %d",&N,&M);
    for(int i=0;i<N;i++)
      for(int j=0;j<M;j++)
	scanf("%d",&a[i][j]);
    
    for(int i=0;i<N;i++){
      for(int j=0;j<M;j++){
	bool flag = true;
	for(int m=0;m<M;m++)
	  if(a[i][m]>a[i][j]){
	    flag=false;
	    break;
	  }
	if(flag)
	  continue;
	flag=true;
	for(int m=0;m<N;m++)
	  if(a[m][j]>a[i][j]){
	    flag=false;
	    break;
	  }
	if(flag)
	  continue;
	printf("Case #%d: NO\n",k);
	status=false;
	break;
      }
      if(!status)
	break;
    }
    if(status)
      printf("Case #%d: YES\n",k);
  }
}
