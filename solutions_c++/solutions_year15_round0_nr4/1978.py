#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <set>
#include <cstdio>
#include <cstring>
#include <string>
#include <map>
#include <fstream>

#include <cstdlib>

#include <iomanip>
#define SZ(X) ((int)(X).size())
#define ALL(X) (X).begin(), (X).end()
#define REP(I, N) for (int I = 0; I < (N); ++I)
#define REPP(I, A, B) for (int I = (A); I < (B); ++I)
#define RI(X) scanf("%d", &(X))
#define RII(X, Y) scanf("%d%d", &(X), &(Y))
#define RIII(X, Y, Z) scanf("%d%d%d", &(X), &(Y), &(Z))
#define DRI(X) int (X); scanf("%d", &X)
#define DRII(X, Y) int X, Y; scanf("%d%d", &X, &Y)
#define DRIII(X, Y, Z) int X, Y, Z; scanf("%d%d%d", &X, &Y, &Z)
#define RS(X) scanf("%s", (X))
#define CASET int ___T, case_n = 1; scanf("%d ", &___T); while (___T— > 0)
#define MP make_pair
#define PB push_back
#define MS0(X) memset((X), 0, sizeof((X)))
#define MS1(X) memset((X), -1, sizeof((X)))
#define LEN(X) strlen(X)
#define PII pair<int,int>
#define VPII vector<pair<int,int> >
#define PLL pair<long long,long long>
#define F first
#define S second
typedef long long LL;
using namespace std;
const int MOD = 1e9 + 7;
const int SIZE = 1e6 + 10;

vector<vector<int>> g;

int res = 0;

vector<char> used;

void dfs(int v)
{
	used[v] = 1;

	int n = g[v].size();

	REP(i, n)
	{
		if (g[v][i]!=-1)
		if (!used[g[v][i]])
		{


			dfs(g[v][i]);
		}
		else
		if (used[g[v][i]] == 2)
			res--;

		
			

	}

	used[v] = 2;

}

LL gcd(LL a, LL b)
{
	if (a > b)
		swap(a, b);
	return (a ? gcd(a, b%a) : b);
}

LL pow1(LL a, LL b)
{
	return b ? b % 2 ? a*pow1(a, b - 1)%MOD : pow1(a*a, b / 2)%MOD : 1;
}

LL factorial(LL a,LL mod)
{
	return a ? a*factorial(a-1,mod) % mod : 1;
}

bool is_prime(LL a)
{
	for (LL i = 2; i*i <= a;i++)
	if (!(a%i))
		return 0;

	return 1;


}

int main()
{

	ifstream in("input.txt");
	ofstream out("output.txt");


	int T;
	in >> T;

	REP(i, T)
	{
		int X, R, C;
		in >> X >> R >> C;

		if (X >= 7)out << "Case #" << (i + 1) << ": " << "RICHARD" << endl;
		else
		{


			if (X==1)
				out << "Case #" << (i + 1) << ": " << "GABRIEL" << endl;
			else if (X == 2)
			{
				if (!(R*C%2))
					out << "Case #" << (i + 1) << ": " << "GABRIEL" << endl;
				else
					out << "Case #" << (i + 1) << ": " << "RICHARD" << endl;
			}
			else if (X == 3)
			{
				if (!(R*C % 3)&&(!(R==1||C==1)))
					out << "Case #" << (i + 1) << ": " << "GABRIEL" << endl;
				else
					out << "Case #" << (i + 1) << ": " << "RICHARD" << endl;
			}
			else if (X == 4)
			{
				if (!(R*C % 4) && (!(R == 1 || C == 1))&&(!(R==2||C==2)))
					out << "Case #" << (i + 1) << ": " << "GABRIEL" << endl;
				else
					out << "Case #" << (i + 1) << ": " << "RICHARD" << endl;

			}
			else if (X == 5)
			{
				if (!(R*C % 5) && (!(R == 1 || C == 1)))
					out << "Case #" << (i + 1) << ": " << "GABRIEL" << endl;
				else
					out << "Case #" << (i + 1) << ": " << "RICHARD" << endl;
			}
			else
			{
				if (!(R*C % 6) && (!(R == 1 || C == 1)) && (!(R == 2 || C == 2)))
					out << "Case #" << (i + 1) << ": " << "GABRIEL" << endl;
				else
					out << "Case #" << (i + 1) << ": " << "RICHARD" << endl;

			}
		}

	}

	in.close();
	out.close();



	return 0;
}