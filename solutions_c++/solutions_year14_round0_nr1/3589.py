#include<iostream>
#include<fstream>
using namespace std;
int main()
{
	ifstream fin("input1.txt");
	ofstream fout("outpu1.txt");
	int times;
	fin>>times;
	for(int i=1;i<=times;i++){
		
		int row1,row2;
		fin>>row1;
		int a[4][4],b[4][4];
		string temp;
		for(int j=0;j<4;j++){
				for(int k=0;k<4;k++)
					fin>>a[j][k];
		}
		fin>>row2;
		for(int j=0;j<4;j++){
				for(int k=0;k<4;k++)
					fin>>b[j][k];
		}
		/*cout<<"row1="<<row1<<" row2="<<row2<<endl;
		for(int k=0;k<4;k++){
		for(int j=0;j<4;j++)
			cout<<a[k][j]<<" ";
			cout<<endl;
		}
		for(int k=0;k<4;k++){
		for(int j=0;j<4;j++)
			cout<<b[k][j]<<" ";
			cout<<endl;
		}*/
		
		int count=0,number;
		for(int j=0;j<4;j++){
			for(int k=0;k<4;k++){
				if(a[row1-1][j]==b[row2-1][k]){
					count++;
					number=b[row2-1][k];
				}
			}
		}
		
		
		if(count==0)
		fout<<"Case #"<<i<<": Volunteer cheated!"<<endl;
		else if(count==1)
		fout<<"Case #"<<i<<": "<<number<<endl;	
		else
		fout<<"Case #"<<i<<": Bad magician!"<<endl;
		
		/*Case #1: 7
		Case #2: Bad magician!
		Case #3: Volunteer cheated!
		*/
				
		
		}
		
		
}


