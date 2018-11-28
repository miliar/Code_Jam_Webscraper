#include <cstdio>
#include <algorithm>
#include <cstring>
using namespace std;

typedef long long LL;
const int N = 33, S = 20;
int n, k, tot;
int a[N];
LL factor[N];

LL muti_mod(LL a,LL b,LL c){    //返回(a*b) mod c,a,b,c<2^63
    a%=c;
    b%=c;
    LL ret=0;
    while (b){
        if (b&1){
            ret+=a;
            if (ret>=c) ret-=c;
        }
        a<<=1;
        if (a>=c) a-=c;
        b>>=1;
    }
    return ret;
}

LL pow_mod(LL x,LL n,LL mod){  //返回x^n mod c ,非递归版
    if (n==1) return x%mod;
    int bit[90],k=0;
    while (n){
        bit[k++]=n&1;
        n>>=1;
    }
    LL ret=1;
    for (k=k-1;k>=0;k--){
        ret=muti_mod(ret,ret,mod);
        if (bit[k]==1) ret=muti_mod(ret,x,mod);
    }
    return ret;
}

bool check(LL a,LL n,LL x,LL t){   //以a为基，n-1=x*2^t，检验n是不是合数
    LL ret=pow_mod(a,x,n),last=ret;
    for (int i=1;i<=t;i++){
        ret=muti_mod(ret,ret,n);
        if (ret==1 && last!=1 && last!=n-1) return 1;
        last=ret;
    }
    if (ret!=1) return 1;
    return 0;
}

bool Miller_Rabin(LL n){
    LL x=n-1,t=0;
    while ((x&1)==0) x>>=1,t++;
    bool flag=1;
    if (t>=1 && (x&1)==1){
        for (int k=0;k<S;k++){
            LL a=rand()%(n-1)+1;
            if (check(a,n,x,t)) {flag=1;break;}
            flag=0;
        }
    }
    if (!flag || n==2) return 0;
    return 1;
}

LL gcd(LL a,LL b){
    if (a==0) return 1;
    if (a<0) return gcd(-a,b);
    while (b){
        LL t=a%b; a=b; b=t;
    }
    return a;
}

LL Pollard_rho(LL x,LL c){
    LL i=1,x0=rand()%x,y=x0,k=2;
    while (1){
        i++;
        x0=(muti_mod(x0,x0,x)+c)%x;
        LL d=gcd(y-x0,x);
        if (d!=1 && d!=x){
            return d;
        }
        if (y==x0) return x;
        if (i==k){
            y=x0;
            k+=k;
        }
    }
}

void findfac(LL n){           //递归进行质因数分解N
    if (!Miller_Rabin(n)){
        factor[tot++] = n;
        return;
    }
    LL p=n;
    while (p>=n) p=Pollard_rho(p,rand() % (n-1) +1);
    findfac(p);
    findfac(n/p);
}

bool Checkdfs()
{
	for (int base = 2; base <= 10; ++ base)
	{
		LL cur = 0;
		for (int i = 1; i <= n; ++ i) cur = cur * 1ll * base + 0ll + a[i];
		if (!Miller_Rabin(cur)) return 0;
	}
	return 1;
}

void Write()
{
	for (int i = 1; i <= n; ++ i) printf("%d", a[i]);
	printf(" ");
	for (int base = 2; base <= 10; ++ base)
	{
		LL cur = 0;
		for (int i = 1; i <= n; ++ i) cur = cur * 1ll * base + 0ll + a[i];
		tot = 0;
		findfac(cur);
		printf("%lld ", factor[0]);
	}
	puts("");
}

void dfs(int dep)
{
	if (dep >= n)
	{
		if (Checkdfs())
		{
			Write();
			-- k;
		}
		return;
	}
	a[dep] = 0;
	dfs(dep + 1);
	if (!k) return;
	a[dep] = 1;
	dfs(dep + 1);
}

int main()
{
	//freopen("3.in", "r", stdin);
	//freopen("3.out", "w", stdout);
	int T;
	scanf("%d", &T);
	int Case = 0;
	while (T --)
	{
		++ Case;
		scanf("%d%d", &n, &k);
		printf("Case #%d:\n", Case);
		a[1] = a[n] = 1;
		dfs(2);
	}
}