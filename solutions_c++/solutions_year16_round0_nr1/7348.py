#include "fstream"
#include "sstream"

using namespace std;

int main ()
{
	ifstream in ("in.txt");
	ofstream out ("out.txt");
	
	int n;
	in >> n;
	
	int ans;
	
	for (int t = 1;t <= n;t++)
	{
		int k;
		in >> k;
		
		if (k == 0)
		{
			out << "Case #" << t << ": INSOMNIA\n";
			continue;
		}
		
		bool used[10];
		memset (used, 0, sizeof (used));
		ans = -1;
		
		for (int a = 1;;a++)
		{
			stringstream ss;
			ss << k * a;
			
			string s;
			ss >> s;
			
			for (int b = 0;b < s.length ();b++)
			{
				used[s[b] - '0'] = true;
			}
			
			bool flag = true;
			for (int b = 0;b < 10;b++)
				if (!used[b])
					flag = false;
			
			if (flag)
			{
				ans = a * k;
				break;
			}
		}
		
		if (ans != -1)
			out << "Case #" << t << ": " << ans << '\n';
		else
			out << "Case #" << t << ": INSOMNIA\n";
	}
	
	return 0;
}