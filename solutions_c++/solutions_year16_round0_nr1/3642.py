#include <iostream>
#include <vector>
#include <set>
#include <cstdint>
using namespace std;

void solve(int test_case)
{
	int n;
	cin >> n;
	if (n == 0)
	{
		cout << "Case #" << test_case << ": " << "INSOMNIA" << endl;
		return;
	}
	set<int> q;
	int64_t p = n;
	while (true)
	{
		int64_t w = p;
		while (w)
		{
			q.insert(w % 10);
			w /= 10;
		}
		if (q.size() == 10)
			break;
		p += n;
	}
	cout << "Case #" << test_case << ": " << p << endl;
}

int main(void)
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for (int i = 0; i < t; ++i)
	{
		solve(i+1);
	}
}