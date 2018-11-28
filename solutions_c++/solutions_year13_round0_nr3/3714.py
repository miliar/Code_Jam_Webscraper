#include <fstream>

typedef unsigned long long ull;
typedef long long ll;

#define FN "gcj1c"

using namespace std;

inline bool check(ull a)
{
	char dst[100];
	ltoa(a,dst,10);
	int l = strlen(dst);
	for(int i = 0; i < l/2; i++)
		if(dst[i] != dst[l-1-i])
			return false;

	ull q = a*a;
	ltoa(q,dst,10);
	l = strlen(dst);
	for(int i = 0; i < l/2; i++)
		if(dst[i] != dst[l-1-i])
			return false;

	return true;
}

int main()
{
	ifstream in(FN ".in");
	ofstream out(FN ".out");

	int t;
	in >> t;

	for(int i = 0; i < t; i++)
	{
		ull a,b;
		in >> a >> b;

		ull ans = 0;

		ull from = (ull)sqrt((double)a-0.5)+1;
		ull to = (ull)sqrt((double)b);
		for(ull a = from; a <= to; a++)
			if(check(a))
				ans++;

		out << "Case #" << i+1 << ": " << ans << "\n";
	}

	out.close();
	return 0;
}