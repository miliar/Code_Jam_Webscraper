#include <iostream>
#include <fstream>
#include <vector>

using namespace std;


int main()
{
	ifstream fin("A-small-0.in");
	ofstream fout("A-small-0.out");
	int t;
	fin>>t;
	int r1,r2;
	int s;
	vector<vector<int>> a,b;
	vector<int> temp;
	int num,count=0;
	for(int i=0;i<t;++i)
	{
		count=0;
		temp.clear();
		a.clear();
		b.clear();
		fin>>r1;
		//cout<<r1<<endl;
		for(int j=0;j<4;++j)
		{
			for(int k=0;k<4;++k)
			{
				fin>>s;
				//cout<<s<<" ";
				temp.push_back(s);
			}
			//cout<<endl;
			a.push_back(temp);
			temp.clear();
		}
		fin>>r2;
		
		for(int j=0;j<4;++j)
		{
			for(int k=0;k<4;++k)
			{
				fin>>s;
				//cout<<s<<" ";
				temp.push_back(s);
			}
			//cout<<endl;
			b.push_back(temp);
			temp.clear();
		}
		//fin>>r1;
		for(int j=0;j<4;++j)
		{
			for(int k=0;k<4;++k)
			{
				if(a[r1-1][j]==b[r2-1][k])
				{	
					count++;
					num=a[r1-1][j];
				}
			}
		}
		if(count==1)
		{
			fout<<"Case #"<<i+1<<": "<<num<<endl;
		}
		else if(count==0)
		{
			fout<<"Case #"<<i+1<<": "<<"Volunteer cheated!"<<endl;
		}
		else if(count>1)
		{
			fout<<"Case #"<<i+1<<": "<<"Bad magician!"<<endl;
		}
	}




	return 0;
}