#include <iostream>
#include <fstream>
#include <vector>
#include <iomanip>
#include <string>
#include <iomanip>

using namespace std;

double give(double num,int & digit)
{
	digit=0;
	string s=to_string(long double(num));
	string ans="0.";
	for(int i=s.size()-1;i>=0;--i)
	{
		if(s[i]=='.')
			break;
		ans.push_back('0');
		digit++;
	}
	ans.pop_back();
	ans.push_back('1');
	return atof(ans.c_str());
}

int main()
{
	ifstream fin("B-large.in");
	
	int t;
	fin>>t;
	ofstream fout("B-large.out");
	
	long double run_time=0.0;
	double cookies;
	double c,f,x;
	long double minimum_time=0;
	for(int i=0;i<t;++i)
	{	
		run_time=0.0;
		cookies=2.0;
		fin>>c>>f>>x;
		int n=0;
		minimum_time=0;
		while(n<501)
		{
			if(x<=c)
			{
				run_time=x/cookies;
				minimum_time=run_time;
				break;
			}
			if(run_time+(x/cookies)<=(run_time+(c/cookies)+(x/(cookies+f))))
			{
				run_time+=x/cookies;
				if(minimum_time<run_time)
					minimum_time=run_time;
				break;
			}
			run_time+=(c/cookies);
			cookies+=f;
		}
		fout<<"Case #"<<i+1<<": ";
		fout<< setprecision(10) <<minimum_time<<endl;

	}
	
	



	return 0;
}