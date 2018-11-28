#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
using namespace std;
void main()
{
	ifstream in("LargeA.in");
	ofstream out("LargeA_Out.out");
	int testcases;
	in>>testcases;
	in.ignore();
	for(int i=0;i<testcases;i++)
	{
		string line,num;
		int maxlevel;
		getline(in,line);
		istringstream iss(line);
		iss>>num;
		maxlevel = stoi(num);
		maxlevel++;
		iss>>num;
		int * levels = new int [maxlevel];
		for(int j=0;j<maxlevel;j++)
		{
				levels[j] = num[j] - '0';
		}
		int sum = levels[0];
		int ans = 0;
		int diff = 0;
		for(int j=1;j<maxlevel;j++)
		{
			if(sum < j)
			{
				diff += (j-sum);
				sum += diff;
				ans += diff;
				diff = 0;
			}
			sum += levels[j];
			
		}
		out<<"Case #"<<i+1<<": "<<ans<<endl;
	}
	out.close();
	in.close();
}