#include<iostream>
#include<fstream>
#include<string>
#include<algorithm>

using namespace std;

ifstream fin("data.in");
ofstream fout("result.out");

int main()
{
	int t;
	fin>>t;
	for(int case_no=1;case_no<=t;++case_no)
	{
		fout<<"Case #"<<case_no<<": ";
		long long a,b;
		fin>>a>>b;
		long long count=0;
		for(long long i=1;i<10000;++i)
		{
			string num=to_string(i);
			string reverse_num(num.rbegin(),num.rend());

			long long result=stoll(num+reverse_num);
			result*=result;
			string s_result=to_string(result);
			string reverse_result(s_result.rbegin(),s_result.rend());
			if(result>=a&&result<=b&&s_result==reverse_result)
				++count;

			result=stoll(num+reverse_num.substr(1));
			result*=result;
			s_result=to_string(result);
			reverse_result=string(s_result.rbegin(),s_result.rend());
			if(result>=a&&result<=b&&s_result==reverse_result)
				++count;
		}
		fout<<count<<endl;
	}
}