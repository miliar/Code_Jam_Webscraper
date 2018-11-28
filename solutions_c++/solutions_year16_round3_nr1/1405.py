#include <iostream>
#include <algorithm>
using namespace std;
const int MAXN = 26;
const char letters[27] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
struct party
{
	int c;
	char s;
} p[MAXN];
bool compare(party p1, party p2)
{
	return p1.c >= p2.c;
}
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t, i, n, j;
	cin >> t;
	for(i = 1; i <= t; i++)
	{
		cin >> n;
		for(j = 0; j < n; j++)
		{
			cin >> p[j].c;
			p[j].s = letters[j];
		}
		sort(p, p + n, compare);
		cout << "Case #" << i << ": ";
		int temp = p[0].c - p[1].c;
		for(j = 0; j < temp; j++)
			cout << p[0].s << " ";
		for(j = 2; j < n; j++)
			for(int k = 0; k < p[j].c; k++)
				cout << p[j].s << " ";
		for(j = 0; j < p[1].c; j++)
			cout << p[0].s << p[1].s << " ";
		cout << endl;
	}
	return 0;
}

