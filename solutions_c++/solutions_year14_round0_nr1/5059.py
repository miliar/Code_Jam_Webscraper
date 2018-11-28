#include<cstdio>
using namespace std;
int main()
{
//	freopen("1.txt","r",stdin);
	freopen("2.txt","w",stdout);
	int t=0;
	int k=0;
	scanf("%d",&t);
	while(t--){
		k++;
		int a1,a2;
		int i,j;
		int a[4][4],b[4][4];
		int x[4],y[4];
		scanf("%d",&a1);
		for(i=0;i<4;i++){
			for(j=0;j<4;j++){
				scanf("%d",&a[i][j]);
				if(i==a1-1){
					x[j]=a[i][j];
				}
			}
		}
		scanf("%d",&a2);
		for(i=0;i<4;i++){
			for(j=0;j<4;j++){
				scanf("%d",&b[i][j]);
				if(i==a2-1){
					y[j]=b[i][j];
				}
			}
		}
		int ans=0;
		int count=0;
		for(i=0;i<4;i++){
			for(j=0;j<4;j++){
				if(x[i]==y[j]){
					ans=x[i];
					count++;
					break;
				}
			}
		}
		if(count==0){
			printf("Case #%d: Volunteer cheated!\n",k);
			//printf("Case #%d: Bad magician!\n",k);
			
		}else if(count == 1){
			printf("Case #%d: %d\n",k,ans);
			
		}else{
			printf("Case #%d: Bad magician!\n",k);
			//printf("Case #%d: Volunteer cheated\n",k);
		}
		
		
		
		
		
	}
	return 0;
}

