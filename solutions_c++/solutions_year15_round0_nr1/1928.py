#include<iostream>
#include<cstdint>

using namespace std;

int main()
{
	uint64_t T;
	cin >> T;

	for (uint64_t t = 0; t < T; ++t)
	{
		uint64_t Smax, s = 0, a = 0;
		cin >> Smax;
		for (uint64_t i = 0; i < Smax + 1; ++i)
		{
			char S;
			cin >> S;
			int v = S - '0';
			if (a >= i) {
				a += v;
			}else{
				++s;
				a += v + 1;
			}
		}
		cout << "Case #" << t + 1 << ": " << s << endl;
	}
	return 0;
}
