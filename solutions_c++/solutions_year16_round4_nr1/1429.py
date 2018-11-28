#include <cstdio>
#include <queue>
#include <algorithm>
#include <cstring>

struct Matrix
{
	long long d[3][3];
	Matrix ()
	{
		memset(d, 0, sizeof(d));
	}
	Matrix operator *(const Matrix &m) const
	{
		Matrix r;
		for (int i=0; i<3; ++i)
			for (int j=0; j<3; ++j)
			{
				long long c = 0;
				for (int k=0; k<3; ++k)
				{
					c += d[i][k] * m.d[k][j];
				}
				r.d[i][j] = c;
			}
		return r;
	}
};

void win(Matrix &m, int w, int l)
{
	m.d[w][w] = 1;
	m.d[w][l] = 1;
}

void strwin(char *str)
{
	if (str[0] > str[1])
		std::swap(str[0],str[1]);
}

#define _P 0
#define _R 1
#define _S 2

char swin[3][3];
char SS[2][3][1<<12+4];
int si[3];

bool cmp(int a, int b)
{
	return strcmp(swin[a], swin[b]) < 0;
}

int main()
{
	Matrix m;
	win(m, _R, _S);
	win(m, _S, _P);
	win(m, _P, _R);
	strcat(swin[_R], "RS");
	strcat(swin[_S], "SP");
	strcat(swin[_P], "PR");

	for (int i=0; i<3; ++i)
	{
		strwin(swin[i]);
		si[i] = i;
	}
	std::sort(si, si+3, cmp);
	/*for (int i=0; i<3; ++i)
	{
		printf("%s\n",swin[si[i]]);
	}*/

	int T;
	long long N, P, R, S;
	scanf("%d\n", &T);
	for (int t=0; t<T; ++t)
	{
		scanf("%lld%lld%lld%lld", &N, &R, &P, &S);
		Matrix p;
		p.d[0][0] = 1;
		p.d[1][1] = 1;
		p.d[2][2] = 1;
		strcpy(SS[1][_S], swin[_S]);
		strcpy(SS[1][_R], swin[_R]);
		strcpy(SS[1][_P], swin[_P]);
		Matrix r = m;
		for (int i=1; i<N; ++i)
		{
			p = r;
			r = r * m;
			if (strcmp(SS[i&1][_R], SS[i&1][_S]) < 0)
			{
				strcpy(SS[(i&1)^1][_R], SS[i&1][_R]);
				strcat(SS[(i&1)^1][_R], SS[i&1][_S]);
			}
			else
			{
				strcpy(SS[(i&1)^1][_R], SS[i&1][_S]);
				strcat(SS[(i&1)^1][_R], SS[i&1][_R]);
			}
			if (strcmp(SS[i&1][_S], SS[i&1][_P]) < 0)
			{
				strcpy(SS[(i&1)^1][_S], SS[i&1][_S]);
				strcat(SS[(i&1)^1][_S], SS[i&1][_P]);
			}
			else
			{
				strcpy(SS[(i&1)^1][_S], SS[i&1][_P]);
				strcat(SS[(i&1)^1][_S], SS[i&1][_S]);
			}
			if (strcmp(SS[i&1][_P], SS[i&1][_R]) < 0)
			{
				strcpy(SS[(i&1)^1][_P], SS[i&1][_P]);
				strcat(SS[(i&1)^1][_P], SS[i&1][_R]);
			}
			else
			{
				strcpy(SS[(i&1)^1][_P], SS[i&1][_R]);
				strcat(SS[(i&1)^1][_P], SS[i&1][_P]);
			}
			/*for (int y=0; y<3; ++y)
			{
				for (int x=0; x<3; ++x)
					printf("%lld ", r.d[y][x]);
				printf("\n");
			}*/
		}
		int j;
		for (j=0; j<3; ++j)
		{
			if (r.d[j][_P] == P
			 && r.d[j][_R] == R
			 && r.d[j][_S] == S)
				break;
		}
		printf("Case #%d: ", t+1);
		if (j == 3)
		{
			printf("IMPOSSIBLE\n");
		}
		else
		{
			/*for (int i=0; i<3; ++i)
			{
				int x = si[i];
				for (int k=0; k<p.d[j][x]; ++k)
				{
					putc(swin[x][0], stdout);
					putc(swin[x][1], stdout);
				}
			}*/
			printf("%s\n", SS[N&1][j]);
		}
	}
	return 0;
}
