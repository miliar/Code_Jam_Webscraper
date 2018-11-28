#include <iostream>
#include <string>

using namespace std;

const int maxn = 10010;

int T, L, X;
string s;

//i=2, j=3, k=4
int mat[5][5] = {
	{0, 0, 0, 0, 0},
	{0, 1, 2, 3, 4},
	{0, 2, -1, 4, -3},
	{0, 3, -4, -1, 2},
	{0, 4, 3, -2, -1} 
};

int chartoijk(char x)
{
	return x-'i'+2;
}

int a[maxn];
int head[maxn];
int tail[maxn];

int main()
{

	// freopen("a.in", "r", stdin);
	// freopen("b.out", "w", stdout);
	
	cin>>T;
	for (int kase = 1; kase <= T; kase++)
	{
		cin>>L>>X;
		cin>>s;
		printf("Case #%d: ", kase);

		//长度不够
		if (L*X < 3)
		{
			puts("NO");
			continue;
		}

		for (int i = 0; i < L; ++i)
			a[i] = chartoijk(s[i]);

		for (int i = 1; i < X; ++i)
			for (int j = 0; j < L; ++j)
				a[i*L + j] = a[j];
		L = L*X;

		int p = head[0] = a[0], q, tmp;
		for (int i = 1; i < L; ++i)
		{
			q = a[i];
			tmp = mat[abs(p)][q];
			if (p < 0)	tmp = -tmp;
			p = tmp;
			head[i] = p;
		}

		// i*j*k 等于 -1
		if (p != -1)
		{
			puts("NO");
			continue;
		}

		p = tail[0] = a[L-1];
		for (int i = 1; i < L; ++i)
		{
			q = a[L-1-i];
			tmp = mat[q][abs(p)];
			if (p < 0)	tmp = -tmp;
			p = tmp;
			tail[i] = p;
		}

		int l=0, r=L-1;
		bool ans = false;
		while(l < r)
		{
			if (head[l] != 2)
			{
				l++;
				continue;
			}

			while(l<r && tail[L-1-r] != 4) 
				r--;

			if (l<r)
			{
				ans = true;
				break;
			}
		}

		printf("%s\n", ans ? "YES" : "NO");
	}
	return 0;
}

/**
 * head[i]*tail[L-1-i] = 
 */