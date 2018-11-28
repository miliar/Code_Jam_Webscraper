#include <bits/stdc++.h>
using namespace std;

int main()
{
	ifstream fin("input.in");
	ofstream fout("out.txt");
	int tc;
	fin>>tc;
	for(int j = 1;j <= tc;j++)
	{
		long long len;
		fin>>len;
		string s;
		fin>>s;
		long long count = 0;
		long long ans = 0;
		for(int i = 0;i <= len;i++)
		{
			if(s[i] - '0' != 0){
			if(i - count >= 0)
			{
				ans += (i - count);
				count = count + i - count + (s[i] - '0');
			}
			else
			{
				count = count + (s[i] - '0');
			}
			}
		}
		fout<<"Case #"<<j<<": "<<ans<<endl;
	}
	return 0;
}
