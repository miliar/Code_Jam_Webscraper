#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <algorithm>
#include <fstream>
#include <map>

using namespace std;

int main()
{
	int t = 0;
	ifstream fin("test.in",ios::in);
	ofstream fout("result.out",ios::out);

	fin>>t;

	for(int i = 0; i < t; i++)
	{
		int n = 0;
		fin >> n;

		if(n == 0)
		{
			fout << " Case #" << i+1 << ": INSOMNIA" << endl;
			continue;
		}

		bool arr[10];
		for(int j = 0; j < 10; j++)
			arr[j] = false;

		int cnt = 0;
		long long temp = 0;
		while(cnt < 10)
		{
			temp += n;
			// convert number to string
			ostringstream ss;
			ss << temp;
			string str = ss.str();

			int len = str.length();
			for(int j = 0; j < len; j++)
			{
				if(!arr[str[j]-'0'])
				{
					cnt++;
					arr[str[j] - '0'] = true;
				}
			}
		}

		fout << " Case #" << i+1 << ": " << temp << endl;

	}
	


	return 0;
}
