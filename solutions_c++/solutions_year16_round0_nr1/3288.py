#include<fstream>
#include<vector>
#include<string>
#include<cstring>

using namespace std;

long long solve(long long n)
{
	bool seen[10];
	
	for(int i = 0;i < 10;++i)
	{
		seen[i] = false;
	}
	
	int counter = 1;
	long long save_nr;
	for(;;)
	{
		long long nr = n * counter;
		save_nr = nr;
		
		while(nr)
		{
			int dig = nr % 10;
			seen[dig] = true;
			nr /= 10;
		}
		
		bool ok = true;
		for(int i = 0;i < 10;++i)
		{
			if(seen[i] == false)
			{
				ok = false;
				break;
			}
		}
		if(ok)
		{
			break;
		}
		++counter;
	}
	
	return save_nr;
}

int main()
{
	ifstream in("A.in");
	ofstream out("A.out");
	
	int t;
	in >> t;
	
	int n;
	for(int i = 0;i < t;++i)
	{
		in >> n;
		
		if(n == 0)
		{
			out<<"Case #"<<i + 1<<": "<<"INSOMNIA\n";
		}
		else
		{
			long long ans = solve(n);
			out<<"Case #"<<i + 1<<": "<<ans<<"\n";
		}
	}
	
	in.close();
	out.close();
}
