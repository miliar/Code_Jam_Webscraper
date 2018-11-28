
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <cstring>
#include <cctype>
#include <map>
#include <list>
#include <cmath>
#include <algorithm>

using namespace std;

typedef unsigned long long ull;
typedef long long ll;

void main()
{
	int T;
	ifstream in;
	ofstream out;
	in.open("A-large.in", ios_base::in);
	out.open("outA.out", ios_base::app);
	in>>T;
	for(int t = 0; t < T; ++t)
	{
		string s;
		int n, ans = 0, cur = 0;
		in>>n;
		in>>s;
		for(int i = 0; i < s.size(); ++i)
		{
			if(s[i] != '0' && cur < i)
			{
				ans += i - cur;
				cur = i;
			}
			cur += s[i] - '0';
		}
		out<<"Case #"<<t + 1<<": "<<ans<<endl;
	}
	in.close();
	out.close();
	system("pause");
}
