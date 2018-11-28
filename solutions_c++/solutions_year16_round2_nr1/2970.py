#include "iostream"
#include "vector"
#include "algorithm"
#define int long long
using namespace std;
struct _ { ios_base::Init i; _() { cin.sync_with_stdio(0), cin.tie(0); } }_;

int calc (int n)
{
	int sum=0;
	for (int i=1; i<=sqrt(n); i++)
	{
		if (n%i) continue;
		int divisor = n/i;
		if (i%2) sum+=i;
		if (i!=divisor)
			if (divisor%2) sum+=divisor;
	}
	return sum;
}

int solve(string s) 
{
	int ans=0, base=1;
	for (int i=9; i>=0; i--) 
	{
		if (s[i] == '+' || s[i] == 'w')	ans = ans + base;
		base <<= 1;
	}
	return ans;
}

signed main()
{
	int tc;
	cin>>tc;
	vector<int>ph;
	string s;
	for (int i = 1;i <= tc;i++)
	{
		cin>>s;
		ph.clear();
		auto f = s.find("Z");
		while(f != string::npos)
		{
			s.replace(f,1,"");
			f = s.find("E");
			s.replace(f,1,"");
			f = s.find("R");
			s.replace(f,1,"");
						f = s.find("O");
			s.replace(f,1,"");

			f = s.find("Z");
			ph.push_back(0);
		}

		f = s.find("X");
		while(f != string::npos)
		{
			s.replace(f,1,"");
			f = s.find("S");
			s.replace(f,1,"");
			f = s.find("I");
			s.replace(f,1,"");

			f = s.find("X");
			ph.push_back(6);
		}
		f = s.find("W");
		while(f != string::npos)
		{
			s.replace(f,1,"");
			f = s.find("T");
			s.replace(f,1,"");
			f = s.find("O");
			s.replace(f,1,"");

			f = s.find("W");
						ph.push_back(2);
		}
		f = s.find("G");
		while(f != string::npos)
		{
			s.replace(f,1,"");
			f = s.find("E");
			s.replace(f,1,"");
			f = s.find("I");
			s.replace(f,1,"");
			f = s.find("H");
			s.replace(f,1,"");
			f = s.find("T");
			s.replace(f,1,"");

			f = s.find("G");
						ph.push_back(8);
		}
		f = s.find("H");
		while(f != string::npos)
		{
			s.replace(f,1,"");
			f = s.find("T");
			s.replace(f,1,"");
			f = s.find("R");
			s.replace(f,1,"");
			f = s.find("E");
			s.replace(f,1,"");
			f = s.find("E");
			s.replace(f,1,"");

			f = s.find("H");
						ph.push_back(3);

		}
		f = s.find("F");
		while(f != string::npos)
		{
			if(s.find("U") != string::npos)
			{
				s.replace(f,1,"");
				f = s.find("U");
				s.replace(f,1,"");
				f = s.find("O");
				s.replace(f,1,"");
				f = s.find("R");
				s.replace(f,1,"");
				ph.push_back(4);

			}
			else
			{
				s.replace(f,1,"");
				f = s.find("I");
				s.replace(f,1,"");
				f = s.find("V");
				s.replace(f,1,"");
				f = s.find("E");
				s.replace(f,1,"");
				ph.push_back(5);


			}
			f = s.find("F");
		}

		f = s.find("V");
		while(f != string::npos)
		{
				s.replace(f,1,"");
				f = s.find("S");
				s.replace(f,1,"");
				f = s.find("E");
				s.replace(f,1,"");
				f = s.find("E");
				s.replace(f,1,"");
				f = s.find("N");
				s.replace(f,1,"");
				f = s.find("V");

				ph.push_back(7);

		}
		f = s.find("O");
		while(f != string::npos)
		{
				s.replace(f,1,"");
				f = s.find("N");
				s.replace(f,1,"");
				f = s.find("E");
				s.replace(f,1,"");
				f = s.find("O");
				ph.push_back(1);
			  
		}
		f = s.find("N");
		while(f != string::npos)
		{
				s.replace(f,1,"");
				f = s.find("I");
				s.replace(f,1,"");
				f = s.find("N");
				s.replace(f,1,"");
				f = s.find("E");
				s.replace(f,1,"");
				f = s.find("N");
				ph.push_back(9);

		}
	  sort(ph.begin(),ph.end());

	  cout << "Case #"<<i<<": ";
	  for(int j=0;j<ph.size();j++)
			cout << ph[j];
	  cout << '\n';
}}