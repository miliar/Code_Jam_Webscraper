#include <iostream>
#include <vector>

using namespace std;

void visit(vector<int> &ext, long long x, int &total)
{
	while (x > 0)
	{
		int t = x % 10;
		if (ext[t] == 0)
		{
			total ++;
			ext[t] = 1;
		}
		x /= 10;
	}
}

int main()
{
	freopen("test.in", "r", stdin);
	freopen("test.out", "w", stdout);
	int n; cin >> n;
	vector<int> ext(10, 0);
	int total = 0;
	for (int T = 1; T < n+1; T++)
	{
		int x; cin >> x;
		if ( x == 0 )
		{
			cout << "Case #" << T << ": " << "INSOMNIA" << endl;
			continue;
		}
		long long tmp = 0;
		while (total < 10)
		{
			tmp += x;
			visit(ext, tmp, total);
		}
		for (int i = 0; i < 10; i++) ext[i] = 0;
		total = 0;
		cout << "Case #" << T << ": " << tmp << endl;
	}
	return 0;
}