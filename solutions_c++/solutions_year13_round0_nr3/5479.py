# include <fstream>
# include <iostream>
# include <string>
# include <vector>
# include <math.h>
# include <algorithm>
# include <string.h>
# include <stack>
# include <queue>
# include <sstream>
# include <set>
# include <map>
# include <assert.h>
using namespace std;

long long num[20];
long long numCount;
void fact(long long n)
{
	memset(num, 0, sizeof(num));
	numCount = 0;
	while (n > 0)
	{
		num[numCount++] = n % 10;
		n /= 10;
	}
	for (long long i = 0, j = numCount - 1; i < j; i++, j--)
		swap(num[i], num[j]);
}

long long unfact()
{
	long long ans = 0;
	for (long long i = 0; i < numCount; i++)
	{
		ans *= 10;
		ans += num[i];
	}
	return ans;
}

bool isPoly(long long n)
{
	fact(n);
	for (long long i = 0, j = numCount - 1; i < j; i++, j--)
		if (num[i] != num[j])
			return false;
	return true;
}

int main()
{
    //ios_base::sync_with_stdio(false);
    ifstream cin ("input.txt");
    ofstream cout ("output.txt");

	long long tests;
	cin >> tests;
	for (long long test = 0; test < tests; test++)
	{
		long long a, b;
		cin >> a >> b;
		long long ans = 0;
		long long bound = sqrt(b);
		bound *= 2;
		fact(bound);
		bound = 0;
		for (long long i = 0; i < (numCount + 1) / 2; i++)
			bound *= 10LL, bound += num[i];
		bound += 10;
		for (long long i = 1; i <= bound; i++)
		{
			fact(i);
			for (long long j = numCount - 1; j >= 0; j--)
				num[numCount++] = num[j];
			long long first = unfact();
			first *= first;
			if (isPoly(first) && first >= a && first <= b)
				ans++;

			fact(i);
			for (long long j = numCount - 2; j >= 0; j--)
				num[numCount++] = num[j];
			long long second = unfact();
			second *= second;
			if (isPoly(second) && second >= a && second <= b)
				ans++;
		}

		cout << "Case #" << test + 1 << ": " << ans << endl;
	}
    
    //system("pause");
    return 0;
}
