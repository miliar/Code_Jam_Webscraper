#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <stack>
#include <queue>
#include <algorithm>
#include <cmath>
#include <list>
#include <map>
#include <set>
using namespace std;

typedef long long int LL;
typedef long double LD;
typedef vector<int> VI;
typedef vector<LL> VLL;
typedef vector<LD> VLD;
typedef vector<string> VS;
typedef pair<int, int> PII;
typedef vector<PII> VPII;

const int INF = 1000000001;
const LD EPS = 10e-9;

#define FOR(x, b, e) for(int x = b; x <= (e); ++x)
#define FORD(x, b, e) for(int x = b; x >= (e); --x)
#define REP(x, n) for(int x = 0; x < (n); ++x)
#define VAR(v, n) __typeof(n) v = (n)
#define ALL(c) (c).begin(), (c).end()
#define SIZE(x) ((int)(x).size())
#define FORE(i, c) for(VAR(i, (c).begin()); i != (c).end(); ++i)
#define MP make_pair
#define PB push_back
#define ST first
#define ND second
#define abs(a) ((a)<0 ? -(a) : (a))
#define max(a, b) ((a) > (b) ? (a) : (b))
#define min(a, b) ((a) < (b) ? (a) : (b))

LL convertToDec(LL jamcoin, int base)
{
	LL res = 0;
	LL mult = 1;
	
	while(jamcoin > 0)
	{
		res += (jamcoin%2)*mult;
		mult *= base;
		jamcoin /= 2;	
	}
	
	return res;
}

LL mnozMod(LL a, LL b, LL n)
{
  LL m,w;

  w = 0; m = 1;
  while(m)
  {
    if(b & m) w = (w + a) % n;
    a = (a << 1) % n;
    m <<= 1;
  }
  return w;
}

// Miller-Rabin primality test from "Algorytmika praktyczna. Nie tylko dla mistrzow", Piotr Stanczyk
bool millerRabin(LL x, LL n)
{
	if (x >= n) return 0;
	LL d = 1, y;
	LL t = 0, l = n - 1;
	
	//cout << "przed while l " << l << endl;
	
	while(!(l&1))
	{
		//cout << "we while " << l << " " << t << endl;
		
		++t;
		l >>= 1;
	}
	
	//cout << "po while" << endl;
	
	for(; l > 0 || t--; l >>= 1)
	{
		//cout << l << " " << t << endl;
		
		if(l&1)
		{
			d = mnozMod(d, x, n);
		}
		
		//cout << "x" << endl;
		
		if(!l)
		{
			x = d;
			l = -1;
		}
		
		//cout << "x2" << endl;
		
		y = mnozMod(x, x, n);
		
		//cout << "x3" << endl;
		
		if(y == 1 && x != 1 && x != n-1)
		{
			return true;
		}
		
		//cout << "x4" << endl;
		
		x = y;
		
		//cout << "x5" << endl;
	}
	
	//cout << "x6" << endl;
	
	return x != 1;
}

bool isPrime(LL x)
{
	return !(x < 2 || millerRabin(2, x) || millerRabin(3, x) || millerRabin(5, x)
		|| millerRabin(7, x) || millerRabin(11, x) || millerRabin(13, x) || millerRabin(17, x)
		|| millerRabin(19, x) || millerRabin(23, x));
}

string toBin(LL dec)
{
	string res;
	
	while(dec > 0)
	{
		res = char((dec%2) + '0') + res;
		dec /= 2;	
	}
	
	return res;
}

void printDivisors(LL x)
{
	FOR(i, 2, 10)
	{
		LL otherBase = convertToDec(x, i);
		FOR(d, 2, otherBase-1)
		{
			if(otherBase%d == 0)
			{
				cout << d << " ";
				break;
			}
		}
	}
	cout << endl;
}

int T;
int n, j;

int main()
{
	ios_base::sync_with_stdio(0);
	cin >> T;
	FOR(t, 1, T)
	{
		cin >> n >> j;
		
		cout << "Case #" << t << ":" << endl;
		
		LL start = (1<<(n-1))+1;
		for(LL i = start; j > 0; i += 2)
		{
			bool bad = false;
			
			//cout << "considering: " << toBin(i) << endl;
			FOR(k, 2, 10)
			{
				//cout << k << endl;
				LL inBase = convertToDec(i, k);
				
				//cout << "in base " << k << " => " << inBase << " \n";
				
				if(isPrime(inBase))
				{
					//cout << "IS prime" << endl;
					bad = true;
					break;
				}
				//cout << "is NOT prime" << endl;
			}
			
			if(!bad)
			{
				cout << toBin(i) << " ";
				printDivisors(i);
				
				j--;
			}
		}
		
	}
	return 0;
}


