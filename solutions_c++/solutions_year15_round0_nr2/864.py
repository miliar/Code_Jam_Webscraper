#include <iostream>
#define oo 1000000
#define min(a,b) ((a)<(b)?(a):(b))
using namespace std;
int p[1100]={0};
int main()
{
	int T, d, now, ans = oo;
	cin >> T;
	for (int test = 1; test <= T; ++test)
	{
		cout << "Case #" << test << ": ";
		cin >> d;
		for (int i = 0; i< d; ++i)
			cin >> p[i];
		ans = oo;
		for (int upper = 1; upper <= 1000; ++upper)
		{
			now = upper;
			for (int i = 0; i< d ; ++i)
				if (p[i] > upper)
					now += p[i]/upper + ((p[i]%upper!=0)?1:0) - 1;
			ans = min(ans, now);
		}
		cout << ans << endl;
	}
	return 0;
}
