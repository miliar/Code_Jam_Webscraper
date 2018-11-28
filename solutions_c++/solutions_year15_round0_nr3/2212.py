#include <cstdio>
#include <cstring>
using namespace std;

int cvt(char c)
{
	switch(c)
	{
		case 'i':
		return 2;
		case 'j':
		return 3;
		case 'k':
		return 4;
	}
	return 0;
}

int mul(int v, char c)
{
	// -k -j -i -1 0 1 i j k
	int cv = cvt(c);

	int ov = v;
	if (ov < 0) ov = -ov;

	int ret = 0;
	if (ov == 1) ret = cv;
	else if (cv == ov) ret = -1;
	else if (cv == ((ov - 1) % 3 + 2)) ret = ((ov) % 3 + 2);
	else if (cv == ((ov) % 3 + 2)) ret = -((ov - 1) % 3 + 2);
	return v < 0 ? -ret : ret ;
}

int main()
{
	freopen("c_in.txt", "r", stdin);
	freopen("c_out.txt", "w", stdout);

	int t;
	scanf("%d", &t);
	for (int cas = 0; cas < t; ++cas)
	{
		int l;
		long long x;
		scanf("%d %lld", &l, &x);
		char str[10005];
		scanf("%s", str);

		if (x >= 8) x = 4 + x % 4;

		int ret = 0;
		int v = 1;
		for (int i=0; i<x; ++i)
		{
			for (int j=0; j<l; ++j)
			{
				v = mul(v, str[j]);
				if (ret == 0 && v == 2) ret += 1;
				if (ret == 1 && v == 4) ret += 1;
			}
		}
		if (ret == 2 && v == -1) printf("Case #%d: YES\n", cas + 1);
		else printf("Case #%d: NO\n", cas + 1);
	}
}