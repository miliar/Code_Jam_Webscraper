// Template v2
#define pb push_back
#define mp make_pair
#define first x
#define second y
#define l(x) x<<1
#define r(x) x<<1 | 1
#define lsb(x) x & -x
#include<bits/stdc++.h>
#include <bitset>
using namespace std;
 
typedef long long LL;
typedef long double LD;
typedef vector<int> VI;
typedef pair<int, int> PII;
typedef pair<LL, LL> PLL;
typedef pair<double, double> PKK;
// primes less than 100
const int PRIM[] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97};
const int CMAX = 10005;
const int MOD = 700001;
const int CIUR = 100000000;
const int NMAX = 10666;
const short INF16 = 32000;
const int INF = 2*1e9 + 6661369;
const LL INF64 = LL(1e18);
const LD EPS = 1e-9, PI = acos(-1.0);

ifstream fin("jam.in");
ofstream fout("jam.out");

bool equal(int A[], int B)
{
	int d, i=1;
	while(B)
	{
		d=B%10;
			if(d != A[i])
				return false;
		B/=10;
		i++;
	}
	return true;
}

void add(int A[], int B[])
{
      int i, t = 0;
      for (i=1; i<=A[0] || i<=B[0] || t; i++, t/=10)
              A[i] = (t += A[i] + B[i]) % 10;
      A[0] = i - 1;
}

void mul(int A[], int B)
{
      int i, t = 0;
      for (i = 1; i <= A[0] || t; i++, t /= 10)
              A[i] = (t += A[i] * B) % 10;
      A[0] = i - 1;
}
int mod(int A[], int B)
{
      int i, t = 0;
      for (i = A[0]; i > 0; i--)
              t = (t * 10 + A[i]) % B;
      return t;
}


int p[150], s[150], aux[150], sum;
bool q;
int check(LL x, int b)
{
	sum=0;
	memset(p, 0, sizeof(p));
	memset(s, 0, sizeof(s));
	p[0]=1;
	s[0]=1;
	s[1]=0;
	p[1]=1;
	for(int i=0; i<32; ++i)
	{
		if(x & (1LL<<(i)))
			add(s, p);
		mul(p, b);
	}
	for(int i=0; i<25; ++i)
	{
		memcpy(aux, s, sizeof(aux));
		if(!mod(aux, PRIM[i]))
			return PRIM[i];
	}
	
	return 0;
}

int nr;
void read()
{
	fout<<"Case #1:\n";
	int k=32;
	int cnt;
	LL i;
	for(i=(1LL<<31); i<(1LL<<32) && nr<500; ++i)
	{
		if(i&1)
		{
			if(check(i,2) && check(i,4) && check(i,6) && check(i,8) && check(i,10) && check(i,3) && check(i,5) && check(i,7) && check(i,9))
			{
				nr++;
				bitset<32> b(i);
				fout<<b<<" ";
				fout<<check(i, 2)<<" "<<check(i, 3)<<" "<<check(i, 4)<<" "<<check(i, 5)<<" "<<check(i, 6)<<" "<<check(i, 7)<<" "<<check(i,8)<<" "<<check(i, 9)<<" "<<check(i,10)<<"\n";
			}
		}
	}
    
}
 
int main(){
	cin.sync_with_stdio(false);
    read();
    return 0;
}