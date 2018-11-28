#include <algorithm>  
#include <bitset>  
#include <cctype>  
#include <cmath>  
#include <complex>  
#include <cstdio>  
#include <cstdlib>  
#include <cstring>  
#include <ctime>  
#include <deque>  
#include <functional>  
#include <iomanip>  
#include <iostream>  
#include <fstream>
#include <list>  
#include <map>  
#include <numeric>  
#include <queue>  
#include <set>  
#include <sstream>  
#include <stack>  
#include <string>  
#include <utility>  
#include <vector>   
using namespace std;

ifstream ifile;
ofstream ofile;

int T,cases;

int g[110][110];

string s[110];

int N;

void solve()
{
	memset(g,-1,sizeof(g));
	ifile>>N;

	for(int i = 0; i < N; i++)
		ifile>>s[i];

	int cur = 0;

	bool sign = true;

	while(sign)
	{
		int end = 0;
		char test = s[0][0];
		for(int i = 0; i < N; i++)
		{
			int st = 0;
			if(s[i][st]!=test)
			{
				sign=false;
				break;
			}
			int num = 0;
			while(s[i][st]==test)
			{
				st++;
				num++;
			}
			g[i][cur]=num;
			s[i]=s[i].substr(num);
			if(s[i].size()==0)
				end++;
		}
		cur++;
		if(end>0&&end<N)
		{
			sign = false;
		}
		if(end==N)
		{
			break;
		}
	}
	
	if(!sign)
		ofile<<"Case #"<<cases<<": "<<"Fegla Won"<<endl;
	else
	{
		int res = 0;
		for(int i = 0; i < cur; i++)
		{
			int sum = 0;
			for(int j = 0; j < N; j++)
			{
				sum+=g[j][i];
			}
			int a = sum/N;
			int b = sum/N+1;

			int sa =0;
			int sb =0;
			for(int j = 0; j < N; j++)
			{
				sa+=abs(g[j][i]-a);
				sb+=abs(g[j][i]-b);
			}
			res+=min(sa,sb);
		}
		ofile<<"Case #"<<cases<<": "<<res<<endl;
	}
}

int main(void)
{
	ifile.open("input.txt");
	ofile.open("output.txt");

	ifile>>T;
	for(int i = 0; i < T; i++)
	{
		cases=i+1;
		solve();
	}

	ifile.close();
	ofile.close();
	return 0;
}