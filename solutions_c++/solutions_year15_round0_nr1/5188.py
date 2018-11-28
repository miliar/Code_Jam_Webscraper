#include <iostream>
using namespace std;

int main()
{
	int N; cin >> N;
	for (int trial = 1; trial <= N; ++trial)
	{
		int sm, r = 0, p = 0; cin >> sm;
		for (int s = 0; s <= sm; ++s)
		{
			char n; cin >> n; n -= '0';
			if (p < s)
			{
				r += s-p;
				p = s;
			}
			p += n;
		}
		cout << "Case #" << trial << ": " << r << endl;
	}
	return 0;
}
