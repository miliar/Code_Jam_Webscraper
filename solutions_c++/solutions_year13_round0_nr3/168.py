#include <algorithm>
#include <iostream>
#include <cassert>
#include <cstring>
#include <cstdio>
#include <vector>
#include <cmath>
#include <map>
#include <set>

#define SIZE(A) ((int)A.size())
#define LENGTH(A) ((int)A.length())
#define MP(A,B) make_pair(A,B)
#define PB(A) push_back(A)

typedef long long ll;
typedef double ld;

int	fx[] = {-1, 0, +1, 0}, fy[] = {0, +1, 0, -1},
	ex[] = {-1, -1, 0, +1, +1, +1, 0, -1}, ey[] = {0, +1, +1, +1, 0, -1, -1, -1};

using namespace std;

int test_num, case_number;

#define gout case_number++, printf("Case #%d: ",case_number), cout

int t;

struct pal
{
	vector <int> a;

	bool operator < (const pal &b) const
	{
	 	if (SIZE(a) != SIZE(b.a)) return SIZE(a) < SIZE(b.a);
	 	for (int i = 0; i < SIZE(a); i++)
	 		if (a[i] != b.a[i]) return a[i]<b.a[i];
	 	return 0;	
	}
	bool operator == (const pal &b) const
	{
	 	return a==b.a;
	}
};
vector <pal> q;
pal a, b, c;
int s[2000];

void main2()
{
	string aa, bb;
	cin >> aa >> bb;

	a.a.clear(); b.a.clear();
	for (int i = 0; i < SIZE(aa); i++) a.a.PB(aa[i]-'0');
	for (int i = 0; i < SIZE(bb); i++) b.a.PB(bb[i]-'0');

	int ans = lower_bound(q.begin(), q.end(), b)-lower_bound(q.begin(), q.end(), a);
	if (lower_bound(q.begin(), q.end(), b)!=q.end() && *lower_bound(q.begin(), q.end(), b)==b) ans++;

/*	a = *lower_bound(q.begin(), q.end(), a);
	b = *lower_bound(q.begin(), q.end(), b);

	for (int i = 0; i < SIZE(a.a); i++)
		printf("%d", a.a[i]);
	puts("");
	for (int i = 0; i < SIZE(b.a); i++)
		printf("%d", b.a[i]);
	puts("");*/

	gout << ans << endl;
}


void gen(int u, int L)
{
//	cerr << u << " " << L << endl;
/*	if (SIZE(a.a)==3)
	{
	 	if (a.a[0]==1)
	 	{
	 	 	cerr << "HERE u=" << u << " " << L << endl;
	 	}
	}*/
	for (int i = 0; i < 2*L-1; i++) if (s[i] > 9) return;
	if (u+u >= L)
	{
		c.a.resize(2*L-1);
		for (int i = 0; i < L; i++)
			c.a[i] = c.a[2*L-2-i] = s[i];
//		for (int i = 0; i < 2*L-1; i++)
//			printf("%d", c.a[i]);
//		puts("");
//		for (int i = 0; i < L; i++)
//			printf("%d", a.a[i]);
//		puts("");
		q.PB(c);
	}
	else
	{
		for (int i = !u; i < 10; i++)
		{
			a.a[u] = i;
			a.a[L-1-u] = i;
			int mul;
			for (int j = 0; j <= u; j++)
			{
				mul = 2; if (j==u) mul = 1;
				s[u+j] += mul*i*a.a[j];
				if (2*u+1!=L && u!=j)
					s[L-1-u+j] += mul*i*a.a[j];
				if (2*u+1!=L)
					s[2*L-2-u-j] += mul*i*a.a[j];
				if (2*u+1!=L || j!=u)
					s[u+L-j-1] += 2*i*a.a[j];
			}
			gen(u+1, L);
			for (int j = 0; j <= u; j++)
			{
				mul = 2; if (j==u) mul = 1;
				s[u+j] -= mul*i*a.a[j];
				if (2*u+1!=L && u!=j)
					s[L-1-u+j] -= mul*i*a.a[j];
				if (2*u+1!=L)
					s[2*L-2-u-j] -= mul*i*a.a[j];
				if (2*u+1!=L || j!=u)
					s[u+L-j-1] -= 2*i*a.a[j];
			}
		}
	}
}

int main()
{
	for (int i = 1; i <= 50; i++)
	{
		memset(s, 0, sizeof(s));
		a.a.resize(i);
		gen(0, i);
		cerr << "Gened for L=" << i << endl;
//		if (i ==5) break;
	}
	sort(q.begin(), q.end());
/*	for (int i = 0; i < SIZE(q); i++)
	{
	 	for( int j = 0; j < SIZE(q[i].a); j++)
	 		printf("%d", q[i].a[j]);
	 	puts("");
	}*/
//	return 0;

	scanf("%d", &test_num);

	for (int i = 0; i < test_num; i++)
		main2();

	return 0;
}
