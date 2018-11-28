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
#define MIN(a, b) (((a) < (b))? (a): (b))
#define MAX(a, b) (((a) < (b))? (b): (a))
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

const int NPRIMES = 9;

int primes[NPRIMES] = {2, 3, 5, 7, 11, 13,  17, 19, 23};
vector <int> rem[11];
vector <int> now;
int add[13][40][NPRIMES];
int t, n, J;
map <LL, char> used;

void dp(int nowstep)
{
	if (nowstep == n - 1 Or J == 0)
		return;

	bool f = true;
	FOR(base, 2, 10)
	{
		bool g = false;
		MFOR(primeIND, 0, NPRIMES)
			g |= (rem[base][primeIND] == 0);

		if (!g)
		{
			f = false;
			break;
		}
	}

	if (f)
	{
		LL x = 0;
		LL SS = 1;
		MFOR(i, 0, now.size())
		{
			x += SS * now[i];
			SS <<= 1;
		}
		if (used[x] == 0)
		{
			used[x] = 1;
			DFOR(i, now.size() - 1, 0)
				printf("%d", now[i]);

			FOR(i, 2, 10)
			{
				MFOR(j, 0, NPRIMES)
				{
					if (rem[i][j] == 0)
					{
						printf(" %d", primes[j]);
						break;
					}
				}
			}
			cout << endl;
			J--;
		}
	}

	FOR(base, 2, 10)
	{
		MFOR(i, 0, NPRIMES)
			rem[base][i] = (rem[base][i] + add[base][nowstep][i]) % primes[i];
	}
	now[nowstep] = 1;
	dp(nowstep + 1);


	FOR(base, 2, 10)
	{
		MFOR(i, 0, NPRIMES)
			rem[base][i] = (rem[base][i] + primes[i] - add[base][nowstep][i]) % primes[i];
	}

	now[nowstep] = 0;
	dp(nowstep + 1);
}

void solution()
{
	cin >> t >> n >> J;

	FOR(base, 2, 10)
	{
		MFOR(primeIND, 0, NPRIMES)
			add[base][0][primeIND] = 1;
	}

	now.resize(n - 1);
	now.PB(1);
	now[0] = 1;
	FOR(i, 2, 10)
		rem[i].resize(NPRIMES);
	MFOR(step, 1, n)
	{
		FOR(base, 2, 10)
		{
			MFOR(primeIND, 0, NPRIMES)
			{
				int nowprime = primes[primeIND];
				add[base][step][primeIND] = 
					(add[base][step - 1][primeIND] * base) % nowprime;
				if (step == n - 1)
					rem[base][primeIND] = (1 + add[base][step][primeIND]) % nowprime;
			}
		}
	}
	printf("Case #1:\n");
	dp(1);
	cout << J << endl;
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