#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <vector>
#include <string>

using namespace std;


long long trans(vector<int>& a, long long syst)
{
	long long ans = 0, k = 1;
	for (auto it = a.rbegin(); it != a.rend(); ++it, k *= syst)
		ans += *it * k;
	return ans;
}

vector<int> binToVect(int x, int sz)
{
	vector<int> a;
	a.push_back(1);
	int count = 0;
	while (x > 0)
	{
		a.push_back(x % 2);
		x /= 2;
		++count;
	}
	for (int i = count; i < sz; ++i)
		a.push_back(0);
	a.push_back(1);
	reverse(a.begin(), a.end());
	return a;
}

void printVect(vector<int> &a)
{
	for (int i = 0; i < a.size(); ++i)
		printf("%d", a[i]);
}

void printTwoVect(vector<int>& a)
{
	for (int i = 0; i < 2; ++i)
		printVect(a);
}


void caseN(int number, int n, int j)
{
	printf("Case #%d: ", number);
	printf("\n");
	for (int i = 0; i < j; ++i)
	{
		vector<int> a = binToVect(i, n / 2 - 2);
		printTwoVect(a);
		for (int k = 2; k <= 10; ++k)
			printf(" %lld", trans(a, k));
		printf("\n");
	}
	printf("\n");
}

int main()
{
	freopen("1.in", "r", stdin);
	freopen("1.out", "w", stdout);


	int n;
	scanf("%d", &n);

	for (int i = 0; i < n; ++i)
	{
		int k, j;
		scanf("%d%d", &k, &j);
		caseN(i + 1, k, j);
	}

	return 0;
}