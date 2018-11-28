#include<cstdio>
#include<cstring>
#include<algorithm>

using namespace std;

const int MAXN = 65,MAXM = 3005,Mo = int(1e9) + 7,G = 5959741;
const int Sta[9] = {2,3,5,7,11,13,17,19,23};

typedef long long LL;
typedef long double ld;

LL Fac[MAXN],SEAD;
int Ti[MAXN],C[MAXM][MAXM],B[MAXM],X,Y,cnt,c,c1;

LL Mul(LL a,LL b,LL c)
{
	a %= c;b %= c;
	return (a * b - LL(ld(a) / c * b) * c + c) % c;
}

LL gcd(LL a,LL b)
{
	return b ? gcd(b,a % b) : a;
}

LL Pow(LL a,LL b,LL mo)
{
	a %= mo;
	LL tmp = 1;
	for(;b;b >>= 1,a = LL(a) * a % mo) if (b & 1) tmp = tmp * LL(a) % mo;
	return tmp;
}

LL Pow1(LL a,LL b,LL mo)
{
	LL tmp = 1;
	for(;b;b >>= 1,a = Mul(a,a,mo)) if (b & 1) tmp = Mul(tmp,a,mo);
	return tmp;
}

LL Pow(LL a,LL b)
{
	return Pow(a,b,Mo);
}

void Berno()
{
	int M = 3001;
	for(int i = 1;i <= M;i ++) C[i][0] = C[0][i] = 1;
	for(int i = 1;i <= M;i ++)
		for(int j = 1;j <= i;j ++)
			C[i][j] = (C[i - 1][j - 1] + C[i - 1][j]) % Mo;
	B[0] = 1;
	for(int i = 1;i <= M;i ++)
	{
		int tmp = i + 1;
		for(int j = 0;j < i;j ++) tmp = (tmp - B[j] * 1ll * C[i + 1][j] % Mo + Mo) % Mo;
		B[i] = tmp * Pow(i + 1,Mo - 2,Mo) % Mo;
		c1 ++;
	}
}

bool Test(LL N)
{
	LL P = N;
	N --;
	int t = 0;
	for(;!(N & 1);N >>= 1,t ++);
	for(int i = 0;i < 9;i ++)
	{
		if (Sta[i] >= N) break;
		LL cur;
		if (cur = Pow1(Sta[i],N,P),cur == 1 || cur == (P - 1)) continue;
		bool ok = 0;
		for(int i = 1;i <= t;i ++)
		{
			cur = Mul(cur,cur,P);
			if (cur == (P - 1)) {ok = 1;break;}
		}
		if (!ok) return 0;
	}
	return 1;
}

void Add(LL ft)
{
	for(int i = 1;i <= cnt;i ++) if (Fac[i] == ft) {Ti[i] ++;return;}
	Fac[++ cnt] = ft,Ti[cnt] = 1;
}

bool Prime(LL N)
{
	return Test(N);
}

int RAND()
{
	SEAD = (SEAD * 3 + G);
	while (SEAD >= 998244353) SEAD -= 998244353;
	return SEAD;
}

LL Rho(LL N)
{
	if (N == 1) return -1;
	if (Prime(N)) {return -1;}
	while (1)
	{
		LL X = 2,Y = 2,P = 1;
		int C = RAND();
		while (P == 1)
		{
			X = (Mul(X,X,N) + C) % N;
			Y = (Mul(Y,Y,N) + C) % N;
			Y = (Mul(Y,Y,N) + C) % N;
			P = gcd(abs(X - Y),N);
		}
		if (P != N)
			return P;
	}
}

int A[MAXN],N,K;

void Test()
{
	static long long Out[15];
	for(int i = 2;i <= 10;i ++)
	{
		long long cur = 0;
		for(int j = N;j;j --)
			cur = cur * i + A[j];
		long long v = Rho(cur);
		if (v == -1) return;
		Out[i] = v;
	}
	K --;
	for(int i = N;i;i --) printf("%d", A[i]);
	for(int i = 2;i <= 10;i ++) printf(" %I64d", Out[i]);
	printf("\n");
}

void Dfs(int Now)
{
	if (!K) return;
	if (Now == N) Test(); else
	{
		for(int i = 1;i + 1;i --) 
			A[Now] = i,Dfs(Now + 1);
	}
}

void Work(int Case)
{
	scanf("%d%d", &N, &K);
	A[1] = A[N] = 1;
	printf("Case #%d:\n", Case);
	Dfs(2);
}

int main()
{
//	freopen("data.in","r",stdin),freopen("data.out","w",stdout);
	int T;
	scanf("%d", &T);
	for(;T;T --) Work(T);
	return 0;
}
