#include <iostream>
#include <fstream>
#include <vector>
#include <string>
using namespace std;

vector<int> result;
int arrage[16];
int main()
{
	ifstream infile;
	infile.open("A-small-attempt1.in");
	int T,ans1,ans2;
	infile>>T;
	while(T--)
	{
		infile>>ans1;
		int tmp;
		for(int i=0;i<16;i++)
		{
			infile>>tmp;
			arrage[tmp]=i/4;
		}
		infile>>ans2;
		int ret=0,flag=0;
		for(int i=0;i<16;i++)
		{
			infile>>tmp;
			if(flag)
				continue;
			if(i/4 == ans2 - 1)
			{
				if(ret && arrage[tmp] == ans1 - 1)
				{
					result.push_back(-1);     //Bad magician!
					flag=1;
				}
				else if(!ret && arrage[tmp] == ans1 - 1)
					ret = tmp;
			}
		}
		if(!flag && ret)
			result.push_back(ret);
		else if(!flag && !ret)
			result.push_back(-2);    //Volunteer cheated!
	}
	infile.close();
	ofstream outfile;
	outfile.open("A-small-attempt1.out");
	for(int i=0;i<result.size();i++)
	{
		if(result[i] == -1)
			outfile<<"Case #"<<i+1<<": Bad magician!"<<endl;
		else if(result[i] == -2)
			outfile<<"Case #"<<i+1<<": Volunteer cheated!"<<endl;
		else outfile<<"Case #"<<i+1<<": "<<result[i]<<endl;
	}
	return 0;
}