#include <bits/stdc++.h>
using namespace std;
//look at my code my code is amazing
#define FOR(i, a, b) for (int i = int(a); i < int(b); i++)
#define FOREACH(it, a) for (typeof(a.begin()) it = (a).begin(); it != (a).end(); it++)
#define ROF(i, a, b) for (int i = int(a); i >= int(b); i--)
#define REP(i, a) for (int i = 0; i < int(a); i++)
#define INF 1000000000
#define INFLL 1000000000000000000LL
#define ALL(x) x.begin(), x.end()
#define MP(a, b) make_pair((a), (b))
#define X first
#define Y second
#define EPS 1e-9
#define DEBUG(x)   cerr << #x << ": " << x << " "
#define DEBUGLN(x) cerr << #x << ": " << x << " \n"
typedef pair<int, int> ii;

typedef long long ll;
typedef vector<bool> vb;
//ios_base::sync_with_stdio(0);//fast entrada/salida ;-)
//cin.tie(NULL); cout.tie(NULL);

typedef unsigned __int128 uint128_t;
typedef vector<uint128_t> vi;

const uint128_t N = 32, J = 500;

inline uint128_t my_coin()
{
	return ((uint128_t)1ull<<(N-1ull)) | (((uint128_t)rand()%((uint128_t)1ull<<(N-(uint128_t)2ull)))<<(uint128_t)1ull) | (uint128_t)1ull ;
}


uint128_t base(uint128_t coin, uint128_t b)
{
	uint128_t res = (uint128_t)0;
	
	uint128_t pot = (uint128_t)1;
	while(coin)
	{
		res += (coin&(uint128_t)1)*pot;
		coin >>= (uint128_t)1;
		pot *= b;
	}

	return res;
}

uint128_t mul_mod(uint128_t a,uint128_t b,uint128_t m)
{
	uint128_t res = (uint128_t)0;
    while (a > (uint128_t)0) {
        if (a & (uint128_t)1) {
            res += b;
            if (res >= m) res -= m;
        }
        a >>= (uint128_t)1;
        b <<= (uint128_t)1;
        if (b >= m) b -= m;
    }
    return res;
}

uint128_t pow_mod(uint128_t a,uint128_t n,uint128_t m)
{
	uint128_t p=(uint128_t)1;
	for(uint128_t i=(uint128_t)1;i<=n;i<<=(uint128_t)1)
	{
		if(i&n) p=mul_mod(p,a,m);
		a=mul_mod(a,a,m);
	}
	return p;
}

bool MillerRabin(uint128_t n,int tries) //Return true if prime
{
	if(n==(uint128_t)1) 
		return false;
	if(n==(uint128_t)2||n==(uint128_t)3) 
		return true;
	if(!(n&(uint128_t)1)) 
		return false;
	uint128_t d=n-(uint128_t)1;
	uint128_t s=0;
	
	while(!(d&(uint128_t)1)) 
	{
		d>>=(uint128_t)1;s++;
	}
	
	while(tries--)
	{
		uint128_t x=pow_mod((uint128_t)rand()%(n-(uint128_t)3)+(uint128_t)2,d,n),y;
		for(uint128_t j=0;j<s;j++)
		{
			y=mul_mod(x,x,n);
			if(y==(uint128_t)1&&x!=(uint128_t)1&&x!=n-(uint128_t)1) 
				return false;
			x=y;
		}
		if(x!=(uint128_t)1) 
			return false;
	}
	return true;
}

uint128_t gcd(uint128_t a,uint128_t b)
{
	while(b)
	{
		uint128_t t=a%b;
		a=b;
		b=t;
	}
	return a;
}

uint128_t PollardRho(uint128_t n) //n shouldn't be prime
{
	if(!(n&(uint128_t)1)) return (uint128_t)2;
	while(true)
	{
		uint128_t x=(uint128_t)rand()%n,y=x;
		uint128_t c=(uint128_t)rand()%n;
		if(c==(uint128_t)0||c==(uint128_t)2) c=(uint128_t)1;
		for(uint128_t i=(uint128_t)1,k=(uint128_t)2;;i++)
		{
			x=mul_mod(x,x,n);
			if(x>=c) x-=c; else x+=n-c;
			if(x==n) x=(uint128_t)0;
			if(x==(uint128_t)0) x=n-(uint128_t)1; else x--;
			uint128_t d=gcd(x>y?x-y:y-x,n);
			if(d==n) break;
			if(d!=(uint128_t)1) return d;
			if(i==k) {y=x;k<<=(uint128_t)1;}
		}
	}
}

static char *qtoa(uint128_t n) {
    static char buf[40];
    unsigned int i, j, m = 39;
    memset(buf, 0, 40);
    for (i = 128; i-- > 0;) {
        int carry = !!(n & ((uint128_t)1 << i));
        for (j = 39; j-- > m + 1 || carry;) {
            int d = 2 * buf[j] + carry;
            carry = d > 9;
            buf[j] = carry ? d - 10 : d;
        }
        m = j;
    }
    for (i = 0; i < 38; i++) {
        if (buf[i]) {
            break;
        }
    }
    for (j = i; j < 39; j++) {
        buf[j] += '0';
    }
    return buf + i;
}

int main()
{

	map<uint128_t, vi> jamcoins;

	vector<uint128_t> divs(9);

	//uint128_t j = (uint128_t)(1ull<<60ull) * (uint128_t)(1ull<<60ull);

	//printf("%s\n", qtoa(j));



	while(jamcoins.size() < J)
	{
		uint128_t coin = my_coin() ;

		if(jamcoins.find(coin) != jamcoins.end())
			continue;

		bool has_divisors = true;

		for(uint128_t b=(uint128_t)2; b<=(uint128_t)10; b++)
		{
			uint128_t bcoin = base(coin, b);

			has_divisors = (not MillerRabin(bcoin, 13));

			if(has_divisors)
			{
				divs[b-2] = (uint128_t)PollardRho(bcoin);
			}
			else
			{
				//DEBUG(base(coin,2));
				//DEBUG(b);
				//DEBUGLN(bcoin);
				break;
			}
		}

		if(has_divisors)
			jamcoins[coin] = divs;

	}

	printf("Case #1:\n");



	for(auto &it : jamcoins)
	{
		auto coin = it.first;

		uint128_t bin_coin = (uint128_t)0ull;

		uint128_t dpot = 1;
		while(coin)
		{
			bin_coin += (coin&(uint128_t)1ull)*dpot;
			coin >>= (uint128_t)1ull;
			dpot *= (uint128_t)10ull;
		}

		printf("%s", qtoa(bin_coin));


		for(int b = 2; b <= 10; b++)
		{
			printf(" %s", qtoa((it.second)[b-2]));
		}
		printf("\n");
	}

	return 0;
}