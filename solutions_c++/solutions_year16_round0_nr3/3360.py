#include <bitset>
#include <cmath>
#include <cstdio>
#include <iostream>
typedef long long lld;

const unsigned L = 1 << 16;
const int J = 50;
const int MAXC = 505;
const int N = 16;
std::bitset<20> bin;
int buffer[MAXC]{ };
lld output[12];
lld Num, Sqt, T;

inline lld toBase(const int& bit, const int& bas)
{
	lld ans = 0, two, zen;
	for(two=zen=1; two <= bit; two <<= 1, zen *= bas)
		if(two & bit) ans += zen;
	return ans;
}

int main()
{
	puts("Case #1:");
	for(int bit = 1 << (N-1) | 1; bit < L; ++bit)
	{
		bool done = true;
		for(int bas = 2; bas <= 10; ++bas)
		{
			T = toBase(bit, bas);
			Sqt = sqrt(T)+1;
			output[bas] = -1;
			for(lld dvn = 2; dvn < Sqt; ++dvn) if(!(T % dvn))
			{
				output[bas] = dvn;
				break;
			}
			if(output[bas] == -1) { done = false; break; }
		}
		if(done)
		{
			std::cout << std::bitset<N>(bit);
			for(int bas = 2; bas <= 10; ++bas)
				printf(" %d", output[bas]);
			if(++Num == J) break;
			putchar('\n');
		}
	}
	return 0;
}