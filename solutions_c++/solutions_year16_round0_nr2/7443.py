#include "fstream"
#include "sstream"

using namespace std;

int main ()
{
	ifstream in ("in.txt");
	ofstream out ("out.txt");
	
	int n;
	in >> n;
	
	for (int t = 1;t <= n;t++)
	{
		out << "Case #" << t << ": ";
		string s;
		in >> s;
		
		int ans;
		
		ans = 0;
		for (int a = 0;a < s.length () - 1;a++)
			if (s[a] != s[a + 1])
				ans++;
		
		if (s[s.length () - 1] == '-')
			ans++;
		
		out << ans << '\n';
	}
	
	in.close ();
	out.close ();
	
	return 0;
}