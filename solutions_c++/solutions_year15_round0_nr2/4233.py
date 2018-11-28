#include <algorithm>
#include <cstdio>
#include <cstring>
#define FOR(i,a,b) for(i=a; i<=b; i++)
#define FOR2(i,n) FOR(i,0,n-1)
#define TFOR(i,a,b) for(i=a; i>=b; i--)
#define f first
#define s second
#define pb push_back
#define all(x) x.begin(),x.end() 
#define MAXN 10005
using namespace std;
typedef pair < int , int > pii;
int read(){ int res(0),sign(1); char c;
	while(1){ c = getchar(); if('0' <= c && c <= '9') { res = c - '0'; break; } else if(c == '-') { sign = -1; break; } }
	while(1){ c = getchar(); if('0' <= c && c <= '9') res = res*10 + c - '0'; else break; }
	return res * sign;
}
int A[MAXN];
int hesapla()
{
	int a,i,maxi(0),mini(1001),res,s;
	int N = read();
	FOR(i,1,N)
		A[i] = read();

	FOR(a,1,1000)
	{
		s = 0;
		FOR(i,1,N)
			s += (A[i]-1)/a;
		if(a == 1) res = s + a;
		else res = min( res , s + a );
	}

	return res;
}
int main()
{
	int T = read(),i;
	FOR(i,1,T)
		printf("Case #%d: %d\n" , i , hesapla() );
	return 0;
}
