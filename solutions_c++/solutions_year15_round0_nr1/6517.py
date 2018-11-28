#include <iostream>
#include <string>
#include <fstream>
using namespace std;

int main()
{
	int T;
	string if_name ="A-large.in",of_name = "answer.txt";
	ifstream input(if_name.c_str());
	ofstream output(of_name.c_str());
	input>>T;
	for (int i = 0;i < T;i++)
	{
		int s_max;
		input>>s_max;
		input.get();
		int sj,stand = 0,f_num = 0;
		for(int j = 0;j <= s_max;j++)
		{
			sj = input.get()-'0';
			if (stand < j && sj>0) f_num += j-stand,stand += j-stand;
			stand += sj;
		}
		output<<"Case #"<<i+1<<": "<<f_num<<endl;
	}

	return 0;
}