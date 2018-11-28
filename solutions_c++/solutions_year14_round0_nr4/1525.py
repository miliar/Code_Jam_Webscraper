#include <iostream>
#include <algorithm>
#include <fstream>
using namespace std;

#define MAXN 1000

double Nao[ MAXN ];
double Ken[ MAXN ];
int N;

/*
int dp[ MAXN ][ MAXN ];

bool cmp(double a, double b)
{
	return a > b;
}

int score(int i, int j)
{
	if (Nao[ i - 1 ] > Ken[ j - 1 ])
	{
		return 1;
	}
	else
	{
		return 0;
	}
}
*/

int rb;
void solve(int a, int left, int right)
{
	if (a == N)
	{
		return;
	}

	if (Nao[ a ] > Ken[ left ])
	{
		rb ++;
		solve(a + 1, left + 1, right);
	}
	else
	{
		solve(a + 1, left, right - 1);
	}
}

int main()
{
	int T;

	fstream in("test.in");
	fstream out("res.out");

	in>>T;
//	scanf("%d", &T);
	for (int i = 1; i <= T; i ++)
	{
		in>>N;
//		scanf("%d", &N);
		for (int j = 0; j < N; j ++)
		{
			in>>Nao[ j ];
	//		cin>>Nao[ j ];
		}
		for (int j = 0; j < N; j ++)
		{
			in>>Ken[ j ];
	//		cin>>Ken[ j ];
		}

		sort(Nao, Nao + N);
		sort(Ken, Ken + N);
		
		int itn = 0, itk = 0;

		int ra = 0;
		while (itn < N && itk < N)
		{
			while (Ken[ itk ] < Nao[ itn ] && itk < N)
			{
				itk ++;
			}
			if (itk == N)
			{
				break;
			}
			else
			{
				ra ++;
				itk ++;
				itn ++;
			}
		}
//		printf("%d\n", N - ra);
		
		rb = 0;
		solve(0, 0, N - 1);
//		printf("%d\n", rb);
		
		out<<"Case #"<<i<<": "<<rb<<" "<<N - ra<<endl;
//		cout<<"Case #"<<i<<": "<<rb<<" "<<N - ra<<endl;
		/*
		 *	dp[ i ][ j ] = max(dp[ i - 1 ][ j ] + score(i - j, i), 
		 *						dp[ i - 1 ][ j - 1 ] + score(n - j + 1, i))
		 */
		/*
		dp[ 1 ][ 0 ] = score(1, 1);
		dp[ 1 ][ 1 ] = score(N, 1);

		for (int i = 1; i <= N; i ++)
		{
			for (int j = 0; j <= i; j ++)
			{
				if (i - 1 >= j && j - 1 >= 0)
				{
					dp[ i ][ j ] = max(dp[ i - 1 ][ j ] + score(i - j, i),
										dp[ i - 1 ][ j - 1 ] + score(N - j + 1, i));
				}
			}
		}
		*/
	}
	return 0;
}