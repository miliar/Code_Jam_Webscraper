#include<cstdio>
using namespace std;
int main(){
	int t1;
	int i,j,t;
	scanf("%d",&t1);
	for(t=0;t<t1;t++){
		
	
		int n1,n2;scanf("%d",&n1);
		int a[4][4],b[4][4];
		for(i=0;i<4;i++) for(j=0;j<4;j++) scanf("%d",&a[i][j]);
		scanf("%d",&n2);
		for(i=0;i<4;i++) for(j=0;j<4;j++) scanf("%d",&b[i][j]);
		int c[4];
		for(i=0;i<4;i++) c[i]=a[n1-1][i];
		int cnt=0,ans=0;
		for(i=0;i<4;i++){
			int ch=c[i];
			for(j=0;j<4;j++){
				if(c[i]==b[n2-1][j]){  cnt++;ans=c[i];}
			}
		}
		
		if(cnt==1)
		{
			printf("Case #%d: %d\n",t+1,ans);
		}
		else if(cnt>1)
		{
			printf("Case #%d: Bad magician!\n",t+1);
		}
		else 
		{
			printf("Case #%d: Volunteer cheated!\n",t+1);	
		}	
	}
	return 0;
}
