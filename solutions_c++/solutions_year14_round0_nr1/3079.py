#include <bits/stdc++.h>
using namespace std;
int main(){
	int t;
	cin>>t;
	for(int ii=1;ii<=t;ii++){
		int n;
		cin>>n;
		int a[4][4];
		int i,j;
		for(i=0;i<4;i++){
			for(j=0;j<4;j++)
				cin>>a[i][j];
		}
		int m;
		cin>>m;
		int b[4][4];
		for(i=0;i<4;i++){
			for(j=0;j<4;j++)
				cin>>b[i][j];
		}
		int ans;
		int flag=0;
		for(i=0;i<4;i++){
			for(j=0;j<4;j++){
				if(a[n-1][i]==b[m-1][j]){
					flag++;
					ans=a[n-1][i];
					break;
				}
			}
		}
		printf("Case #%d: ",ii);
		if(flag==0)
			printf("Volunteer cheated!\n");
		else if(flag==1)
			printf("%d\n",ans);
		else
			printf("Bad magician!\n");

	}
}