#include <iostream>
#include <stdio.h>
#include <iomanip>
#include <fstream>
#include <math.h>
using namespace std;
int x1[4][4];
int x2[4][4];
int main(){
	int T;

	ifstream fin("D:/A-small-attempt0.in");
	fin>>T;
	for(int t=0;t<T;t++)
	{
		int row1,row2;
		fin>>row1;
		for(int i=0;i<4;i++)
			for (int j=0;j<4;j++)
				fin>>x1[i][j];
		fin>>row2;
		for(int i=0;i<4;i++)
			for (int j=0;j<4;j++)
				fin>>x2[i][j];
		int cnt=0;
		int rec;
		for (int i=0;i<4;i++)
			for (int j=0;j<4;j++)
				if (x1[row1-1][i]==x2[row2-1][j]){
					cnt++;
					rec=x1[row1-1][i];
				}

		cout<<"Case #"<<t+1<<": ";
		if (cnt==0)
			cout<<"Volunteer cheated!"<<endl;
		if (cnt==1)
			cout<<rec<<endl;
		if (cnt>1)
			cout<<"Bad magician!"<<endl;
	}
	system("pause");
}