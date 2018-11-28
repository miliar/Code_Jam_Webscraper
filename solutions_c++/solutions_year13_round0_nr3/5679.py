#include <string>
#include <cstdio>
#include <cstring>
#include <vector>

using namespace std;

bool esPalindrome (long long int num)
{
	vector<int> digits;
	while (num)
	{
		digits.push_back((num % 10));
		num /= 10;
	}

	int N = digits.size();
	for (int i = 0; i < N/2; ++i)
		if (digits[i] != digits[N-i-1])
			return false;

	return true;
}

int main ()
{
	//freopen("salidaC.txt","w",stdout);

	long long int MAX= 1000;
	vector<long long int> palin;

	for (long long int i = 1; i < MAX; ++i)
	{
		if (esPalindrome(i) && esPalindrome(i*i))
			palin.push_back(i*i);
	}

	int T;
	scanf("%d",&T);

	for (int t = 1; t<=T; ++t)
	{
		int A,B;
		scanf("%d %d",&A,&B);

		int count = 0;
		for (int i = 0; i < palin.size(); ++i)
		{
			if (palin[i] >= A && palin[i] <= B)
				++count;
		}

		printf("Case #%d: %d\n",t,count);
	}

	return 0;
}
