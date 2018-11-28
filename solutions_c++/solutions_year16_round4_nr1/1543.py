#include <list>
#include <map>
#include <set>
#include <algorithm>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <memory.h>
#include <ctime>
#include <bitset>
#include <vector>
#include <stack>
#include <string>
#include <queue>
  
using namespace std;
  
#define ABS(a) (((a) > 0)? (a): -(a))
#define Min(a, b) (((a) < (b))? (a): (b))
#define Max(a, b) (((a) < (b))? (b): (a))
#define MFOR(i, a, n) for (int i = (a); i < (n); i++)
#define FOR(i, a, n) for (int i = (a); i <= (n); i++)
#define DFOR(i, a, n) for (int i = (a); i >= (n); i--)
#define SQR(a) (a) * (a)
#define All(a) (a).begin(), (a).end()
#define PI 3.1415926535897932384626433832795
#define MEMS(a, b) memset((a), (b), sizeof(a))
#define MP make_pair
#define PB push_back
#define endl '\n'
#define LL long long
#define UN unsigned
#define Or ||
#define And &&
/////////////////////////////////////////////

int N, R, P, S;

char winner(char a, char b)
{
	if (a == b)
		return 0;

	if (a < b)
		swap(a, b);

	if (a == 'S' And b == 'R')
		return 'R';
	else if (a == 'S' And b == 'P')
		return 'S';

	if (a == 'R')
		return 'P';
}

void solution()
{
	int T;
	cin >> T;

	FOR(test, 1, T)
	{
		printf("Case #%d: ", test);
		cin >> N >> R >> P >> S;
		vector <char> Q;
		Q.clear();
		FOR(i, 1, P)
			Q.PB('P');
		FOR(i, 1, R)
			Q.PB('R');
		FOR(i, 1, S)
			Q.PB('S');

		bool flag = false;

		do
		{
			vector <char> A, B;
			A = Q;
			flag = true;
			while (A.size() > 1)
			{
				B.clear();
				MFOR(i, 0, A.size())
				{
					char f = A[i];
					char s = A[i + 1];
					i++;
					char wn = winner(f, s);
					if (wn == 0)
					{
						flag = false;
						break;
					}
					B.PB(wn);
				}
				A.clear();
				A = B;
				if (!flag)
					break;
			}
			if (flag)
				break;
		} while (next_permutation(Q.begin(), Q.end()));

		if (flag)
		{
			MFOR(i, 0, Q.size())
				printf("%c", Q[i]);
		}
		else
			printf("IMPOSSIBLE");
		cout << endl;
	}
}

/*-------------------*/
  
int main()
{
#ifdef Files
freopen("input.txt", "r", stdin);
freopen("output.txt", "w", stdout);
/*Test*/
//freopen("input.txt", "w", stdout);
long double OcZ2X = clock();
#else
//freopen("laboratory.in", "r", stdin);
//freopen("laboratory.out", "w", stdout);
#endif
/*
 　　　　　　　　　　　 　∧__∧
　　　　　　　　　　　 　( ° ͜ʖ°)
　　　　　　　　　　　 　⊂　　 つ
　　　　　　　　　　　　　(つ ﾉ
　　　　　　　　　　　　　 (ノ
　　　　　＼　　　　　　☆
　　　　　　　　　　　　　|　　　　　☆
　　　　　　　　　　(⌒ ⌒ヽ　　　/
　　　　＼　　（´⌒　　⌒　　⌒ヾ　　　／
　　　　　 （’⌒　;　⌒　　　::⌒　　）
　　　　　（´*/    solution();   /*:::　）　／
　　☆─　（´⌒;:　　　　::⌒`）　:;　　）
　　　　　（⌒::　　　::　　　　　::⌒　）
　　 　／　（　　　　ゝ　　ヾ　丶　　ソ　─
*/
#ifdef Time
long double P2HxQ = clock();
printf("\n*** Total time = %.3f sec ***\n", (P2HxQ - OcZ2X) / CLOCKS_PER_SEC);
#endif
}