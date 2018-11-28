#include <stdio.h>
#include <string.h>
#include <string>
#include <sstream>
#include <math.h>


using namespace std;


int main(int argc, char *argv[])
{
	if (argc != 2) {
		printf("Invalid input\n");
		getchar();
		return 1;
	}

	freopen(argv[1], "r", stdin);

	char outname[255];
	sprintf(outname, "out-%s", argv[1]);
	freopen(outname, "w", stdout);

	int cases;
	scanf("%d\n", &cases);

	long long count;
	long long a, b;
	for (int i = 0 ; i < cases ; ++i) {
		scanf("%lld %lld", &a, &b);

		long long low = 1;
		long long upper = 100000000i64;
		long long mid = (low + upper) / 2i64;
		long long midSqr = mid * mid;

		count = 0i64;
		long long base;
		for (; low < upper;)
		{
			if (midSqr < a)
			{
				low = mid+1;
				mid = (low + upper) / 2i64;
				midSqr = mid*mid;
			}
			else if( midSqr > a)
			{
				upper = mid-1;
				mid = (low + upper) / 2i64;
				midSqr = mid*mid;
			}
			else
			{
				base = mid;
				break;
			}
		}

		if (low >= upper) base = low-1;
		if (base == 0) base++;
		
		long long baseSqr = base * base;
		while(baseSqr <= b)
		{
			if (baseSqr < a)
			{
				++base;
				baseSqr = base * base;
				continue;
			}

			ostringstream oss;
			while (baseSqr > 0)
			{
				oss << (baseSqr % 10i64);
				baseSqr /= 10i64;
			}

			bool par = true;
			string s = oss.str();
			for (int j = 0 ; j < s.length() ; ++j)
			{
				if (s[j] != s[s.length()-j-1]) {
					par = false;
					break;
				}
			}
			if (par) 
			{
				ostringstream oss2;
				long long t = base;
				while (t > 0)
				{
					oss2 << (t % 10i64);
					t /= 10i64;
				}

				string s2 = oss2.str();
				for (int j = 0 ; j < s2.length() ; ++j)
				{
					if (s2[j] != s2[s2.length()-j-1]) {
						par = false;
						break;
					}
				}

				if (par)
				{
					//printf("%s %s\n", s2.c_str(), s.c_str());
					++count;
				}
			}

			++base;
			baseSqr = base * base;
		}

		printf("Case #%d: %I64d\n", i+1, count);
	}

	return 0;
}