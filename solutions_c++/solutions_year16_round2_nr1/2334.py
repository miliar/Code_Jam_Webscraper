#include <iostream>
#include <vector>
#include <algorithm>
#include <stdio.h>
#include <string>
#include <cmath>
#include <functional>

#define MAX(a,b) (a>b?a:b)
#define MIN(a,b) (a<b?a:b)
#define INF 987654321

using namespace std;

int z, e, r, o, n, t, w, h, f, u, i, v, s, x, g = 0;


bool compare(int a, int b)
{
	return a < b;
}

void alpha(char ss)
{
	switch (ss)
	{
	case 'Z': ++z; break;
	case 'E': ++e; break;
	case 'R': ++r; break;
	case 'O': ++o; break;
	case 'N': ++n; break;
	case 'T': ++t; break;
	case 'W': ++w; break;
	case 'H': ++h; break;
	case 'F': ++f; break;
	case 'U': ++u; break;
	case 'I': ++i; break;
	case 'V': ++v; break;
	case 'S': ++s; break;
	case 'X': ++x; break;
	case 'G': ++g; break;
	}
}


int main()
{
	freopen("large.txt", "r", stdin);
	freopen("large_answer.txt", "w", stdout);

	int T;

	int tc = 1;

	scanf("%d", &T);

	while (T >= tc)
	{

		int phone[10] = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
		z, e, r, o, n, t, w, h, f, u, i, v, s, x, g, h = 0;

		char S[3000];
		vector<int> number;

		scanf("%s", S);

		for (int i = 0; S[i] != '\0'; ++i)
		{
			char ss = S[i];
			alpha(ss);
		}

		while (z > 0)
		{
			++phone[0];
			--z;
			--e;
			--r;
			--o;
		}

		while (w > 0)
		{
			++phone[2];
			--t;
			--w;
			--o;
		}

		while (u > 0)
		{
			++phone[4];
			--f;
			--o;
			--u;
			--r;
		}

		while (x > 0)
		{
			++phone[6];
			--s;
			--i;
			--x;
		}

		while (g > 0)
		{
			++phone[8];
			--e;
			--i;
			--g;
			--h;
			--t;
		}

		while (o > 0)
		{
			++phone[1];
			--o;
			--n;
			--e;
		}

		while (r > 0)
		{
			++phone[3];
			--t;
			--h;
			--r;
			--e;
			--e;
		}

		while (f > 0)
		{
			++phone[5];
			--f;
			--i;
			--v;
			--e;
		}

		while (s > 0)
		{
			++phone[7];
			--s;
			--e;
			--v;
			--e;
			--n;
		}

		while (i > 0)
		{
			++phone[9];
			--n;
			--i;
			--n;
			--e;
		}

		for (int a = 0; a < 10; ++a)
			for (int b = 0; b < phone[a]; ++b)
				number.push_back(a);

		printf("Case #%d: ", tc);

		for (int i = 0; i < number.size(); ++i)
			printf("%d", number[i]);

		printf("\n");

		++tc;
	}

	return 0;
}