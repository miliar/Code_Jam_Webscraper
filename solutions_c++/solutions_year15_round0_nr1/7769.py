#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <string>
#include <sstream> 
#include <numeric>
using namespace std;

int main()
{
	int test_case;
	int max;
	string line;
	ifstream myfile ("A-small-practice.in");
	ofstream outf ("result1.out");
	myfile>>test_case;

	for(int i=0; i<test_case; i++)
	{
		myfile>>max;
		myfile>>line;

		int cnt=0;
		int sum=0;

		vector<int> data;
		for(int j=0; j<max+1; j++)
		{
			data.push_back(line[j]-'0');
		}
		for(int j=0; j<max+1; j++)
		{
			if(cnt>=j)
				cnt+=data[j];
			else
			{
				if(data[j]!=0)
				{
					int temp=j-cnt;
					sum+=temp;
					cnt+=data[j];
					cnt+=temp;
				}
			}
		}
		outf<<"Case #"<<i+1<<": "<<sum<<endl;
	}

	myfile.close();
	outf.close();
	return 0;
}
