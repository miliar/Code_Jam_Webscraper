#include <cstdio>
#include <sstream>
#include <algorithm>
#include <cmath>
using namespace std;

bool test(int t)
{
	int root;
	stringstream a, b;
	string tmp1, tmp2;
	a<<t;
	tmp1 = tmp2 = a.str();
	reverse(tmp2.begin(), tmp2.end());
	if (tmp1 != tmp2) return false;
	root = sqrt(double(t));
	if (root * root != t) return false;
	b<<root;
	tmp1 = tmp2 = b.str();
	reverse(tmp2.begin(), tmp2.end());
	if (tmp1 != tmp2) return false;
	return true;
}

int main()
{
	int i, k, T, a, b, cnt;
	scanf("%d", &T);

	for (k=1; k<=T; k++)
	{
		scanf("%d %d", &a, &b);
		cnt = 0;
		for (i=a; i<=b; i++)
			cnt += test(i);
		printf("Case #%d: %d\n", k, cnt);
	}
}