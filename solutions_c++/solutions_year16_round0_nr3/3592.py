#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

#define LL long long
const int MAX_N = 37;
int t, n, jAns;
char str[MAX_N];

LL toBase(int base)
{
	LL sum = 0;
	for (int i = n; i >= 1; --i)
		sum += (str[i] - '0') * pow(base, n - i);

	return sum;
}

int isPrim(LL x)
{
	if (x <= 3)
		return true;

	int upper = sqrt(x);
	for (int i = 2; i <= upper ; ++i)
	{
		if (x % i == 0)
			return i;
	}

	return -1;
}

char forbide1[] = "_100011_";
char forbide2[] = "_111111_";
char forbide3[] = "_111001_";
void check()
{
	if (n == 6)
	{
		bool ok1 = false;
		bool ok2 = false;
		bool ok3 = false;
		
		for (int i = 1; i <= n; ++i)
		{
			if (str[i] != forbide1[i])
				ok1 = true;
			if (str[i] != forbide2[i])
				ok2 = true;
			if (str[i] != forbide3[i])
				ok3 = true;
		}

		if (!ok1 || !ok2 | !ok3)
			return;
	}



	std::vector<int> v;
	for (int i = 2; i <= 10; ++i)
	{
		v.push_back( isPrim(toBase(i)) );


		// for (int j = 1; j <= n; ++j)
		// 	cout << str[j];
		// cout << "\tto base " << i << " : " << toBase(i) << "\t" << isPrim(toBase(i));



		if (v.back() == -1)
		{
			// cout << "No" << endl;
			return;
		}
	}

	// cout << "Hit" << endl;
	jAns--;
	for (int i = 1; i <= n; ++i)
		cout << str[i];
	cout << " ";

	for (int i = 0; i < v.size(); ++i)
		cout << v[i] << " ";
	cout << endl;
}

void dfs(int level)
{
	if (level == n)
	{
		str[level] = '1';
		check();
		return;
	}

	str[level] = '0';
	dfs(level + 1);

	if (jAns == 0)
		return;

	str[level] = '1';
	dfs(level + 1);
}

void getInput()
{
	cin >> t;

	for (int i = 1; i <= t; ++i)
	{
		cin >> n >> jAns;

		printf("Case #%d:\n", i);
		str[1] = '1';
		dfs(2);
	}
}

int main(int argc, char const *argv[])
{
	getInput();
	return 0;
}