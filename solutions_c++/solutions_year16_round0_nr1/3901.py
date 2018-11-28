#include<iostream>
#include<fstream>
#include<string>
#include<deque>
#include<queue>
#include<algorithm>
#include<iostream>
#include<stack>
#include<map>
#include<vector>
#include<list>
using namespace std;
#define uint unsigned int
#define ull unsigned long long
#define ll long long
#define cin fin
#define cout fout



ull solve(ull a)
{
	int A[10] = { 0 };

	if (a == 0)
		return 0;
	for (ull i = 1;; i++)
	{
		ull t = i * a;
		while (t != 0)
		{
			A[t % 10] = 1;
			t /= 10;
		}
		int count = 0;
		for (int j = 0; j < 10; j++)
		{
			count += (A[j] == 1);
		}
		if (count == 10)
			return i*a;
	}

}

int main()
{
	fstream fin("A.in");
	fstream fout("A.out");
	ull T, N;
	cin >> T;
	for (int i = 1; i <= T; i++)
	{
		cin >> N;
		ull res = solve(N);
		if (res == 0)
			cout << "Case #" << i << ": INSOMNIA" << endl;
		else
			cout << "Case #" << i << ": " << res << endl;
	}

	system("pause");
	return 0;
}