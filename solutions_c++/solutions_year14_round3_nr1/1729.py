#include<iostream>
#include<string>
#include<algorithm>
#include<vector>
#include<stack>
#include<queue>
#include<list>
#include<map>
#include<set>
#include<memory.h>
#include<ctime>
#include<unordered_set>
using namespace std;
int gcd(int a, int b)
{
	if (b == 0)return a;
	return gcd(b, a%b);
}
int main()
{
	freopen("A-small-attempt1.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tc;
	cin >> tc;
	for (int cs = 1; cs <= tc; cs++)
	{
		int p, q, t;
		scanf("%d/%d", &p, &q);
		t = gcd(p, q);
		p /= t;
		q /= t;
		cout << "Case #" << cs << ": ";
		if ((q&(q - 1)) != 0)
			cout << "impossible" << endl;
		else
		{
			t = 0;
			while (p < q)
			{
				t++;
				p <<= 1;
			}
			cout << t << endl;
		}
	}
	return 0;
}