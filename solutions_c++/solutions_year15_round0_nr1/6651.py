#include<fstream>
#include<string>
#include<cstdlib>
using namespace std;

int solve(const string& s)
{
	int sz = s.size();
	
	int ans = 0;
	int total = 0;
	
	for(int i = 0;i < sz;++i)
	{
		int nr = s[i] - '0';
		
		if(total >= i)
		{
			total += nr;
		}
		else
		{
			ans += i - total;
			total = i + nr;
		}
	}
	
	return ans;
}

int main()
{
	ifstream in("A.in");
	ofstream out("A.out");
	
	int t;
	string s;
	
	getline(in, s);
	t = atoi(s.c_str());
	
	for(int i = 0;i < t;++i)
	{
		getline(in, s);
		
		int ans = solve(s.substr(2, s.size() - 2));
		out<<"Case #"<<i + 1<<": "<<ans<<"\n";
	}
	
	in.close();
	out.close();
}
