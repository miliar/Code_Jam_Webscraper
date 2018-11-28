#include<iostream>
using namespace std;
int main()
{
	int tc,num1,num2,i,j,k;
	int grid1[4][4]={0};
	int grid2[4][4]={0};
	cin>>tc;
	for(k=0;k<tc;k++){
		cin>>num1;
		for(i=0;i<4;i++){
			for(j=0;j<4;j++)
				cin>>grid1[i][j];
		}
		cin>>num2;
		for(i=0;i<4;i++){
			for(j=0;j<4;j++)
				cin>>grid2[i][j];
		}
		int count=0,ans;
		for(i=0;i<4;i++)
			for(j=0;j<4;j++)
				if(grid1[num1-1][i]==grid2[num2-1][j]){
					count++;
					ans=grid1[num1-1][i];
				}
		if(count==0)
			cout<<"Case #"<<k+1<<": "<<"Volunteer cheated!"<<endl;
		else if(count>1)
			cout<<"Case #"<<k+1<<": "<<"Bad magician!"<<endl;
		else if(count==1)
			cout<<"Case #"<<k+1<<": "<<ans<<endl;					
	}
}

