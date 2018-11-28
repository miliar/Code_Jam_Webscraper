#include <iostream>
#include<fstream>
using namespace std;
int main(){
	ifstream input;
	input.open("A-small-attempt1.in");
	ofstream output;
	output.open("output1.txt");
	int T;
	input>>T;
	int A[4][4];
	int B[4][4];
	int a,b;
	for (int i=1; i<=T; i++){
		int count =0;
		input>>a;
		for(int j=0;j<4;j++){
			for(int k=0;k<4;k++){
				input>>A[j][k];
			}
		}
		
		input>>b;
		for(int j=0;j<4;j++){
			for(int k=0;k<4;k++){
				input>>B[j][k];
			}
		}
		int temp;
		for ( int j=0;j<4;j++){
			for (int k=0;k<4;k++){
				if(A[a-1][j]==B[b-1][k]){
					count+=1;
					temp =A[a-1][j];
				}
			}
		}
		
		if(count==1){
			output<<"Case #"<<i<<": "<<temp<<endl;
		}
		else if (count==0){
			output<<"Case #"<<i<<": "<<"Volunteer cheated!"<<endl;
		}
		else if (count>1){
			output<<"Case #"<<i<<": "<<"Bad magician!"<<endl;
		}
	}
	input.close();
	output.close();
	
	
}
