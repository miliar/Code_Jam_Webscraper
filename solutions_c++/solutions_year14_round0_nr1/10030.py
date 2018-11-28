#include<iostream>
using namespace std;
int main(){
	int t;
	freopen("A-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);
	cin>>t;
	for(int test=1;test<=t;test++){
		int initialchoice;
		cin>>initialchoice;
		initialchoice--;
		int grid1[4][4];
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				cin>>grid1[i][j];
			}
		}
		int finalchoice;
		cin>>finalchoice;
		finalchoice--;
		int grid2[4][4];
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				cin>>grid2[i][j];
			}
		}
		int matched=0;
		int matchednumber;
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				if(grid1[initialchoice][i]==grid2[finalchoice][j])
				{
					matched++;
					matchednumber=grid1[initialchoice][i];
				}
			}
		}
		
		if(matched==1){
			cout<<"Case #"<<test<<": "<<matchednumber<<"\n";
			continue;
		}
		else if(matched==0){
			cout<<"Case #"<<test<<": "<<"Volunteer cheated!"<<"\n";
			continue;
		}
		else{
			cout<<"Case #"<<test<<": "<<"Bad magician!"<<"\n";
			continue;
		}
		
		
	}
}
