#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

int main(void)
{
	int test,x=0,i,j;
	int row1,row2;
	int mat1[5][5];
	int mat2[5][5];
	int count,num;
	vector<int> v1,v2;
	//ofstream cout("ans.out");
	//ifstream cin("A-small-attempt2.in");
	cin>>test;
	while(x++<test)
	{
		count=0;
		cin>>row1;
		for(i=1;i<=4;i++)
			for(j=1;j<=4;j++)
			   cin>>mat1[i][j];
		for(i=1;i<=4;i++)
			v1.push_back(mat1[row1][i]);
		cin>>row2;
		for(i=1;i<=4;i++)
			for(j=1;j<=4;j++)
			   cin>>mat2[i][j];
		for(i=1;i<=4;i++)
			v2.push_back(mat2[row2][i]);
		for(i=0;i<4;i++)
			for(j=0;j<4;j++)
				if(v1[j]==v2[i])
				{
					count++;
					num=v1[j];
					break;
				}
		cout<<"Case #"<<x<<": ";
		if(count==0)
			cout<<"Volunteer cheated!"<<endl;
		else if(1==count)
			cout<<num<<endl;
		else if(count>1)
			cout<<"Bad magician!"<<endl;
		v1.clear();
		v2.clear();
	}
	return 0;
}