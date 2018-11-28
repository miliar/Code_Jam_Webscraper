#include<fstream>
#include<vector>
#include<string>
#include<cstring>
#include<algorithm>

using namespace std;

int solve(const string& s)
{
	string str = s;
	int sol = 0;
	
	for(;;)
	{
		int i = str.size() - 1;
		
		while(i > 0 && str[i] == '+')
		{
			--i;
		}
		if(i < 0)
		{
			break;
		}
		
		str = str.substr(0, i + 1);
		
		i = 0;
		while(i < (int) str.size() && str[i] == '+')
		{
			++i;
		}
		if(i >= (int) str.size())
		{
			break;
		}
		
		if(i > 0)
		{
			++sol;
		}
		
		str = str.substr(i, str.size() - i);
		reverse(str.begin(), str.end());
		++sol;
		
		for(int i = 0;i < (int) str.size();++i)
		{
			if(str[i] == '+')
			{
				str[i] = '-';
			}
			else
			{
				str[i] = '+';
			}
		}
	}
	
	return sol;
}

int main()
{
	ifstream in("B.in");
	ofstream out("B.out");
	
	int t;
	in >> t;
	
	for(int i = 0;i < t;++i)
	{
		string s;
		
		in >> s;
		int ans = solve(s);
		
		out<<"Case #"<<i + 1<<": "<<ans<<"\n";
	}
	
	in.close();
	out.close();
}
