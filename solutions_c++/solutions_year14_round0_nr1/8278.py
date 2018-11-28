#include<iostream>
#include<fstream>

using namespace std;


int main(){
	int n=0;
	int numberOfCases;
	cin>>numberOfCases;
	while(n<numberOfCases){
		/**
		*Each test case 
		*/
		int r1,r2;
		int grid1[4][4];
		int grid2[4][4];
		
		cin>>r1;
		r1--;
		for(int i=0;i<4;i++){
				for(int j=0;j<4;j++){
					cin>>grid1[i][j];
				}
		}
		
		cin>>r2;
		r2--;
		for(int i=0;i<4;i++){
				for(int j=0;j<4;j++){
					cin>>grid2[i][j];
				}
		}
		
		bool BadMagician=false;
		int choseNumber=-1;
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				if(grid1[r1][i]==grid2[r2][j]){
					if(choseNumber==-1){
						choseNumber=grid1[r1][i];
					}
					else{
						BadMagician=true;
					}
				}
			}
		}
		
		if(BadMagician){
			cout<<"Case #"<<++n<<": Bad magician!"<<endl; 
		}
		else if(choseNumber==-1){
			cout<<"Case #"<<++n<<": Volunteer cheated!"<<endl;
			
		}else{
			cout<<"Case #"<<++n<<": "<<choseNumber<<endl;
		}
	}

	
	return 0;


}


