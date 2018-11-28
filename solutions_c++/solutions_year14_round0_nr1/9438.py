#include<iostream>
#include<fstream>
using namespace std; 
int main(){
	int t=0,test,ans,grid[4][4],row1[4],row2[4],i,j,flag[100],num[100];
	for(i=0;i<100;i++){
		flag[i]=0;
		num[i]=0;
	}
	ifstream infile("A-small-attempt0.in");
	ofstream ofile("output.txt");
	infile>>test;
//	cin>>test;
	while(t<test){
		infile>>ans;
	//	cin>>ans;
		for(i=0;i<4;i++){
			for(j=0;j<4;j++){
				infile>>grid[i][j];
			//	cin>>grid[i][j];
				if(i==(ans-1)){
					row1[j]=grid[i][j];
				}
			}
		}
		infile>>ans;
	//	cin>>ans;
		for(i=0;i<4;i++){
			for(j=0;j<4;j++){
				infile>>grid[i][j];
			//	cin>>grid[i][j];
				if(i==(ans-1)){
					row2[j]=grid[i][j];
				}
			}
		}
		
		for(i=0;i<4;i++){
			for(j=0;j<4;j++){
				if(row1[i]==row2[j]){
					flag[t]++;
					num[t]=row1[i];
				}
			}
		}
		t++;
	}
	
	
	for(i=0;i<test;i++){
		ofile<<"Case #"<<(i+1)<<": ";
		if(flag[i]==1){
			ofile<<num[i];
		}else if(flag[i]==0){
			ofile<<"Volunteer cheated!";
		}else if(flag[i]>1){
			ofile<<"Bad magician!";
		}
		ofile<<"\n";
	}
	
	return 0;
}
