#include "stdafx.h"
#include <vector>
#include <queue>
#include <map>
#include <list>
#include <queue>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>

using namespace std;

/* tipos */
typedef pair<int,int> pint;
typedef long long tint;
typedef unsigned int mint;
typedef unsigned long long mtint;

typedef vector<int> vint;
typedef vector<vint> vvint;

typedef long double tipo;

/* "funciones" */
#define forn(i,n) for(int ___n=n, i=0;i<___n;++i)
#define dforn(i,n) for(int i=(n)-1;i>=0;--i)
#define forsn(i,s,n) for(int ___n=n, i=s;i<___n;++i)
#define dforsn(i,s,n) for(int i = (int)(n)-1; i>=((int)s); i--)
#define forall(it,X) for(typeof((X).begin()) it = (X).begin(); it != (X).end(); ++it)
#define dforall(it,X) for(typeof((X).rbegin()) it = (X).rbegin(); it != (X).rend(); ++it)
#define all(X) (X).begin(), (X).end()
#define esta(e, c) (c.find(e) != c.end())
#define DBG(a) cerr << #a << " = " << a << endl;

template<class T> string itos(const T&x) { ostringstream o; o<<x; return o.str(); }

string wrd[5050];
char mp[256][15];

tint mcd(tint a, tint b){return (b==0)?a:mcd(b, a%b);}
char MAPA[100][100];

int esPalindromo(long long n)
{
	char nro[100];
	char t=0,i=0;
	while(n!=0)
	{
		nro[t]=n%10;
		n/=10;
		t++;
	}
	for(i=0;i<(long long)(t/2);i++)
	{
		if(nro[i]!=nro[t-i-1])
			return 0;
	}
	return 1;
}

long Calcular(long long A,long long B)
{
	long long i;
	long pal=0;
	long double val;
	for(i=A;i<=B;i++)
	{
		if(esPalindromo(i))
		{
			val=sqrt((long double)i);
			if(!(val-(long double)((long long)val)))
				if(esPalindromo(val))
					pal++;
		}
	}
	return pal;
}

int main() {
	int casos;	
	long long A, B;
	long ret;
	cin >> casos;
	
	for(int i=0; i < casos; i++)
	{
		cin >> A;
		cin >> B;
		ret=Calcular(A,B);
		cout << "Case #"<< i+1 << ": " << ret << endl;
		
	}
	
	return 0;
}

