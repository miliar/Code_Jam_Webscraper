#include <iostream>
#include <vector>
using namespace std;

bool isPalindrome(long long num)
{
	long long n = num;
	long long res = 0;
	while(num > 0)
	{
		int cur = num % 10;
		res = res * 10 + cur;
		num /= 10;
	}
	return n == res;
}

void printFairAndSquare()
{
	int cnt = 0;
	for(long long i = 0; i <= 10000000; i++)
	{
		if(isPalindrome(i))
		{
			long long square = i * i;
			if(isPalindrome(square))
			{
				cnt++;
				cout << square << endl;
			}
		}
	}
	cout << cnt << endl;
}

long long prec[39] = {1,
4,
9,
121,
484,
10201,
12321,
14641,
40804,
44944,
1002001,
1234321,
4008004,
100020001,
102030201,
104060401,
121242121,
123454321,
125686521,
400080004,
404090404,
10000200001,
10221412201,
12102420121,
12345654321,
40000800004,
1000002000001,
1002003002001,
1004006004001,
1020304030201,
1022325232201,
1024348434201,
1210024200121,
1212225222121,
1214428244121,
1232346432321,
1234567654321,
4000008000004,
4004009004004};

int main()
{
	//freopen("input.in", "r", stdin);
	//freopen("output.txt", "w", stdout);
	//printFairAndSquare();
	int T;
	cin >> T;
	for(int test = 1; test <= T; test++)
	{
		long long a, b;
		cin >> a >> b;
		int cnt = 0;
		for(int i = 0; i < 39; i++)
		{
			if(prec[i] >= a && prec[i] <= b)
				cnt++;
		}
		cout << "Case #" << test << ": " << cnt << endl;
	}
	return 0;
}