#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<fstream>

using namespace std;

int main(){
	int t,x=0;
	scanf("%d",&t);
	while(t--){
		x++;
		int ans1,ans2,i,j,cnt=0,temp;
		int a[4][4], b[4][4];
		scanf("%d",&ans1);
		for(i=0;i<4;i++){
			for(j=0;j<4;j++){
				scanf("%d",&a[i][j]);
			}
		}
		scanf("%d",&ans2);
		for(i=0;i<4;i++){
			for(j=0;j<4;j++){
				scanf("%d",&b[i][j]);
			}
		}
		for(i=0;i<4;i++){
			for(j=0;j<4;j++)
			{
				if(a[ans1-1][i]==b[ans2-1][j])
				{	
					temp=a[ans1-1][i];
					cnt++;
				}
			}
		}
		if(cnt==0){
			printf("Case #%d: Volunteer cheated!\n",x);
		}
		else if(cnt==1){
			printf("Case #%d: %d\n",x,temp);
		}
		else 
			printf("Case #%d: Bad magician!\n",x);
	
	}
	return 0;
}
