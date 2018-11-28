#include<cstdio>
using namespace std;
int a[10][10],b[20][2];
int main(){
	freopen("A--small-attempt1.in","r",stdin);
	freopen("A--small-attempt1.out","w",stdout);
    int T,fn,sn;
	scanf("%d",&T);
	for(int kase=0;kase<T;kase++){ 
	      scanf("%d",&fn);
		  for(int i=0;i<4;i++)
			  for(int j=0;j<4;j++){
				  scanf("%d",&a[i][j]);
				  b[a[i][j]][0]=i+1;
			  }
		  scanf("%d",&sn);
		  for(int i=0;i<4;i++)
			  for(int j=0;j<4;j++){
				  scanf("%d",&a[i][j]);
				  b[a[i][j]][1]=i+1;
			  }
		  int cnt=0,temp=-1;
		  for(int i=1;i<=16;i++)
			  if(b[i][0]==fn && b[i][1]==sn){ 
			      cnt++;
				  temp=i;
			  }
		  printf("Case #%d: ",kase+1);
		  if(cnt==1){
			  printf("%d\n",temp);
		  }else if(cnt>1){ 
		      printf("Bad magician!\n");
		  }else if(cnt==0){ 
		      printf("Volunteer cheated!\n");
		  }
    }
	return 0;
}
