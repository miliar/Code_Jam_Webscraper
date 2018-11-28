#include <cstdio>
#include <cstring>
#include <ctime>
#include <cstdlib>
using namespace std;
typedef long long LL;
const int MAXN = 100000005;
int prime[MAXN];
int tot;
bool valid[MAXN];
void get_prime(){
	int i, j;
	int n = MAXN;
	memset(valid, true, sizeof(valid));
	for (i = 2; i <= n; ++i)
	{
		if (valid[i])
			prime[tot++] = i;
		for (j = 0; j < tot && i*prime[j] < n; ++j)
		{
			valid[i*prime[j]] = false;
			if (i%prime[j] == 0)
				break;
		}
	}
}
LL change_base(int base, LL n){
	LL ret = 0;
	LL cnt = 1;
	while (n)
	{
		ret += (n % 10) * cnt;
		n /= 10;
		cnt *= base;
	}
	return ret;
}
LL inc(LL n){
	LL b = 1;
	while (n % 10 == 1)
	{
		b *= 10;
		n /= 10;
	}
	return (n + 1)*b;
}
LL modular_multi(LL x,LL y,LL mo){
	LL t;
	x%=mo;
	for(t=0;y;x=(x<<1)%mo,y>>=1)
		if (y&1)
			t=(t+x)%mo;
	return t;
}
 
LL modular_exp(LL num,LL t,LL mo){
	LL ret=1,temp=num%mo;
	for(;t;t>>=1,temp=modular_multi(temp,temp,mo))
		if (t&1)
			ret=modular_multi(ret,temp,mo);
	return ret;
}
 
bool miller_rabbin(LL n){
	if (n==2)return true;
	if (n<2||!(n&1))return false;
	int t=0;
	LL a,x,y,u=n-1;
	while((u&1)==0) t++,u>>=1;
	int S=80;
	for(int i=0;i<S;i++)
	{
		a=rand()%(n-1)+1;
		x=modular_exp(a,u,n);
		for(int j=0;j<t;j++)
		{
			y=modular_multi(x,x,n);
			if (y==1&&x!=1&&x!=n-1)
				return false;
			x=y;
		}
		if (x!=1)
			return false;
	}
	return true;
}
LL get_divisor(LL n){
	if (miller_rabbin(n))
		return -1;
	for (int j = 0; j < tot; ++j)
	{
		if (n % prime[j] == 0)
			return prime[j];
	}
}
int main(){
	//freopen ("c.in","r",stdin);
	//freopen ("c.out","w",stdout);
	get_prime();
	int N, J, T, cas;
	LL num;
	int i, j;
	LL Mod;
	LL divisor[12];
	scanf("%d", &T);
	for (cas = 1; cas <= T; ++cas)
	{
		scanf("%d %d", &N, &J);
		printf("Case #%d:\n", cas);
		num = 1;
		for (i = 1; i < N; ++i)
			num *= 10;
		Mod = num;
		//printf("%lld\n",num);
		for (i = 0; i < J; ++i)
		{
			num = inc(num);
			int ttt = num & 1;
			if (num / Mod != 1 || ttt != 1)		
			{
				--i;
				continue;
			}
			for (j = 2; j <= 10; ++j)
			{
				LL cnt = change_base(j, num);
				LL tmp = get_divisor(cnt);
				if (tmp == -1)
					break;
				divisor[j] = tmp;
			}
			if (j < 11)
				--i;
			else
			{
				printf("%lld ", num);
				for (j = 2; j <= 10; ++j)
					printf("%lld ", divisor[j]);
				printf("\n");
			}
		}
	}
	return 0;
}

 
