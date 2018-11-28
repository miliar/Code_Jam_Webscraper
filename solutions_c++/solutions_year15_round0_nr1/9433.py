#include <fstream>
#include <iostream>
#include <string>

using namespace std;

int main(void)
{
	ifstream fin("A.in");
	ofstream fout("out.txt");
	int T;
	fin>>T;
	for (int i=0;i<T;i++)
	{
		int Sm;
		fin>>Sm;
		string s;
		fin>>s;
		int cnt = 0;
		int sum = s[0]-'0';
		for (int k=1;k<Sm+1;k++)
		{ 
			if (sum<k)
			{
				cnt+=(k-sum);
				sum=k;
			}
			sum+=(s[k]-'0');
		}
		fout<<"Case #"<<i+1<<": "<<cnt<<endl;	
	}
	return 0;
}
