#include <iostream>
#include <stdio.h>
#include <fstream>

using namespace std;
int main(){
	ofstream output;
	ifstream input;
	input.open("C:\\Workspace\\A-small-attempt1.in");
	output.open("C:\\Workspace\\output.txt");
	int T;
	input>>T;
	int a[4][4];
	for(int i=0;i<T;i++){
		int row1;
		input>>row1;
		for(int j=0;j<4;j++)
			for(int k=0;k<4;k++)
				input>>a[j][k];
		int b[4]={0,0,0,0};
		for(int j=0;j<4;j++)
			b[j]=a[row1-1][j];
		int row2;
		input>>row2;
		for(int j=0;j<4;j++)
			for(int k=0;k<4;k++)
				input>>a[j][k];
		int count=0,correctans;
		for(int j=0;j<4;j++)
		{
			int t=a[row2-1][j];
			for(int k=0;k<4;k++)
				if(b[k]==t){
					count++;
					correctans = t;
				}
		}
		if(count==0)
			output<<"Case #"<<i+1<<": "<<"Volunteer cheated!"<<endl;
		else if(count>1)
			output<<"Case #"<<i+1<<": "<<"Bad magician!"<<endl;
		else
			output<<"Case #"<<i+1<<": "<<correctans<<endl;
	}
	input.close();
	output.close();
	return 0;
}