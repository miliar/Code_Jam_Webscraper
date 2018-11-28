#include <iostream>
#include <string>
#include <fstream>

using namespace std;

int main()
{
	int T , max , sum = 0 , count=0;
	string s;
	ifstream fin("input.txt");
	ofstream fout("output.txt");

	fin>>T;
	int j=1;
	while(T!=0)
	{
		fin>>max;
		fin>>s;
		sum = s[0]-48;
		for(int i=1;i<s.length();i++)
		{
			if(i>sum && (s[i] -48 != 0))
			{
				count = count + (i-sum);
				sum = sum + count;
			}
			sum = sum + (s[i] -48);
		}
		fout<<"Case #"<<j<<": "<<count<<endl;
		
		T--;
		sum = 0;
		j++;
		count = 0;
	}
	return 1;
}