#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <string.h>
#include <bitset>
#include <queue>
#include <map>
#include <string>
#include <stack>
#include <utility>
#include <queue>
#include <cmath>
#define mp make_pair
#define pii pair<int,int> 
#define ff first
#define ss second
#define ll long long 
#define ull unsigned long long
#define vi vector<int>
#define vii vector<pii>
#define vvi vector <vi>
#define rep(x,a,b,c) for(int x=a;x<=b;x+=c)
#define repp(x,a,b) rep(x,a,b,1)
#define rev(x,a,b,c) for(int x=a;x>=b;x-=c)
#define revv(x,a,b) rev(x,a,b,1)
#define OO (int)2e9
#define INF (ll)9e18
 
using namespace std;


ll _sieve_size; 
bitset<10000010> bs; 
int n,j,cur,tc,temp,bases;
ll int hasil[15],base,store[20];
vi primes; 
void sieve(ll upperbound) { 
_sieve_size = upperbound + 1; 
bs.set(); 
bs[0] = bs[1] = 0; 
for (ll i = 2; i <= _sieve_size; i++) if (bs[i]) {
for (ll j = i * i; j <= _sieve_size; j += i) bs[j] = 0;
primes.push_back((int)i);
} } 

bool isPrime(unsigned long long n) 
{
    for (unsigned i = 0; primes[i]*primes[i] <= n; i++) 
	{
        if (n % primes[i] == 0) 
		{
			hasil[bases]=primes[i];
            return false;
        }
    }
 
    return true;
}


bitset<14> s;
bitset<16> list;

void findbase(ll int left)
{
	if(left>=bases)
	{
		store[cur]=left%bases;
		//printf("%d",store[cur]);
		cur++;
		findbase(left/bases);
	}
	else
	{
	store[cur]=left;
	//printf("\n");
	}
}
bool prime;
//void base(int b,int c,)
int curs=1;
int main()
{
	sieve(100000);
	scanf("%d",&tc);
	scanf("%d %d",&n,&j);
	printf("Case #1:\n");
	temp=0;
	while(curs<=j)
	{
		memset(hasil,-1,sizeof(hasil));
		s=bitset<14>(temp);
		temp++;
		list[0]=1;
		list[15]=1;
		//cout<<temp<<"\n";
		revv(x,14,1)
		{
			list[x]=s[x-1];
		}
		//cout<<list<<"\n";
		prime=false;
		revv(x,10,2)
		{
			base=0;
			bases=x;
			revv(y,15,0)
			{
				base+=list[y];
				if(y!=0)
				base*=bases;
			}
			//printf("%lld\n",base);	
			if(isPrime(base))
			{
				prime=true;
				break;
			}
		}
		
		/*prime=false;
		revv(x,9,2)
		{
			bases=x;
			base=0;
			cur=0;
			findbase(base10);
			revv(y,cur,0)
			{
				base+=store[y];
				if(y!=0)
				base*=10;
			}
			if(isPrime(base))
			{
				prime=true;
				break;
			}
			//printf("%lld ",base);
		}*/
		if(prime)continue;
		cout<<list<<" ";
		repp(a,2,9)
		{
			printf("%lld ",hasil[a]);
		}
		printf("%lld\n",hasil[10]);
		curs++;
	}
	return 0;
}
