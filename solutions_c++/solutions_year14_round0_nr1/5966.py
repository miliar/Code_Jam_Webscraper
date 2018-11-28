#include<iostream>
#include<fstream>
#include<sstream>
using namespace std;

int main()
{
	ifstream in("A-small-attempt1.in");
	ofstream out("A-small-attempt1.out");
	string s;
	getline(in,s);
	istringstream sin(s);
	int T;
	sin>>T;
	int one[4][4];
	int two[4][4];
	int row1,row2;
	for(int i=0;i<T;i++)
	{
		getline(in,s);
		istringstream sin(s);
		sin>>row1;
		for(int j=0;j<4;j++)
		{
			getline(in,s);
			istringstream sin(s);
			for(int k=0;k<4;k++){
				sin>>one[j][k];
			}
			
		}
		getline(in,s);
		istringstream sin2(s);
		sin2>>row2;
		for(int j=0;j<4;j++)
		{
			getline(in,s);
			istringstream sin(s);
			for(int k=0;k<4;k++){
				sin>>two[j][k];
			}
			
		}
		int num=0;
		int data;
		for(int j=0;j<4;j++){
			if(num>=2) break;
			for(int k=0;k<4;k++){
				if(one[row1-1][j]==two[row2-1][k]){
					num++;
					if(1==num) data=two[row2-1][k];
					break;
				}
			}
		}
		if(0==num) out<<"Case #"<<1+i<<": "<<"Volunteer cheated!"<<endl;
		else if(1==num) out<<"Case #"<<1+i<<": "<<data<<endl;
		else out<<"Case #"<<1+i<<": "<<"Bad magician!"<<endl;

	}
	system("pause");
}