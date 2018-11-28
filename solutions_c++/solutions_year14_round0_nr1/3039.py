#include <iostream>
#include <stdlib.h>
#include <fstream>
using namespace std;
int main()
{
	ifstream fin("A-small-attempt1.in");
	cin.rdbuf(fin.rdbuf());
	int T;
	cin>>T;
	for(int i=0;i<T;i++)
	{
		int r1,r2,num=0,choose;
		int a[4][4];
		int b[4][4];
		cin>>r1;
		for(int j=0;j<4;j++)
		{
			cin>>a[j][0]>>a[j][1]>>a[j][2]>>a[j][3];
		}
		cin>>r2;
		for(int j=0;j<4;j++)
		{
			cin>>b[j][0]>>b[j][1]>>b[j][2]>>b[j][3];
		}
		for(int k=0;k<4;k++)
		{
			for(int m=0;m<4;m++)
			{
				if(a[r1-1][k]==b[r2-1][m])
				{
					num++;
					choose=a[r1-1][k];
				}
			}
		}
		if(num==0)cout<<"Case #"<<i+1<<": "<<"Volunteer cheated!"<<endl;
		else if(num==1)cout<<"Case #"<<i+1<<": "<<choose<<endl;
		else if(num>1)cout<<"Case #"<<i+1<<": "<<"Bad magician!"<<endl;
	}
	//ifstream fin("A-small-attempt0");
	//cin.rdbuf(fin.rdbuf());
	//ofstream fout("output",ofstream::out|ofstream::app);
	system("pause");
	return 0;
}