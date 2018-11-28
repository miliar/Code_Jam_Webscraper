#include <iostream>
#include <fstream>
using namespace std;
int main(){
	int cases,row1,row2;
	int arr[4][4];
	int arr2[4][4];
	
	ifstream fin("A-small-attempt0.in");
	fin>>cases;
	ofstream fout("output.txt");
	for (int k=0;k<cases;k++){
	fin>>row1;
	int counter=0;
	for (int i=0;i<4;i++){
		for (int j=0;j<4;j++)
		fin>>arr[i][j];

	}

    fin>>row2;

	for (int i=0;i<4;i++){
		for (int j=0;j<4;j++)
		fin>>arr2[i][j];

	}

	
	int temp;
 
	  for (int i=0;i<4;i++){
		  int card=arr[row1-1][i];
		  for (int j=0;j<4;j++){
			  if (card==arr2[row2-1][j]){
				counter++;
				temp=card;
			  }

		  }


	  }
	  if (counter>1){
		  fout<<"Case #"<<k+1<<": "<<"Bad magician!"<<endl;

	  }
	  else if (counter==0){
		  fout<<"Case #"<<k+1<<": "<<"Volunteer cheated!"<<endl;

	  }
	  else if (counter==1){
		   fout<<"Case #"<<k+1<<": "<<temp<<endl;

	  }


  
	}



}