#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <iostream>
using namespace std;
#define LL long long
#define Times 10  
#define MAXN 32
#define C   240  
#define TIME 10  
#define LL long long  
int s[MAXN];
int N,J;
int cnt = 0;

LL ans;  
LL gcd(LL a, LL b){  
    if(a==0) return 1;  
    if(a<0) return gcd(-a,b);  
    return b==0?a:gcd(b,a%b);  
}  
LL MultMod(LL a,LL b,LL n){  
    a%=n;  
    b%=n;  
    LL ret=0;  
    while(b){  
        if(b&1){  
            ret+=a;  
            if(ret>=n) ret-=n;  
        }  
        a=a<<1;  
        if(a>=n) a-=n;  
        b=b>>1;  
    }  
    return ret;  
}  
LL PowMod(LL a,LL n,LL m){  
    LL ret=1;  
    a=a%m;  
    while(n>=1){  
        if(n&1)  
            ret=MultMod(ret,a,m);  
        a=MultMod(a,a,m);  
        n=n>>1;  
    }  
    return ret;  
}  
bool Witness(LL a,LL n){  
    LL t=0,u=n-1;  
    while(!(u&1)){  
        t++;  
        u/=2;  
    }  
    LL x0=PowMod(a,u,n);  
    for(int i=1;i<=t;i++){  
        LL x1=MultMod(x0,x0,n);  
        if(x1==1&&x0!=1&&x0!=(n-1))  
            return true;  
        x0=x1;  
    }  
    if(x0!=1)  
        return true;  
    return false;  
}  
bool Miller_Rabin(LL n,int t){  
    if(n==2) return true;  
    if((n&1)==0)  return false;  
    srand(time(NULL));  
    for(int i=0;i<t;i++){  
        LL a=rand()%(n-1)+1;  
        if(Witness(a,n))  
            return false;  
    }  
    return true;  
}  
LL Pollard_Rho(LL n,LL c){  
    LL i=1,x=rand()%n,y=x,k=2;  
    while(1){  
        i++;  
        x=(MultMod(x,x,n)+c)%n;  
        LL d=gcd(y-x,n);  
        if(d!=1&&d!=n)  
            return d;  
        if(x==y)  
            return n;  
        if(i==k){  
            y=x;  
            k*=2;  
        }  
    }  
}  
void get_small(LL n,LL c){  
    if(n==1) return;  
    if(Miller_Rabin(n,TIME)){  
        ans=min(n,ans);  
        return ;  
    }  
    LL p=n;  
    while(p>=n) p=Pollard_Rho(p,c--);  
    get_small(p,c);  
    get_small(n/p,c);  
}  

LL inter(int n) {
	LL ans = 0;
	LL base = 1;
	for(int i = N-1; i >= 0; i--) {
		ans += base*(s[i]);
		base *= n;
	}
	return ans;
}

void digit(int n) {
	s[0] = s[N-1] = 1;
	int t = N-2;
	while(n && t) {
		s[t] = n % 2;
		n /= 2;
		t--;
	}
}

void output() {
	for(int i = 0 ; i < N ; i++) {
		printf("%d", s[i]);
	}
	printf(" ");
	for(int j = 2; j <= 10; j++) {
		LL x = inter(j);
		ans=x; 
        get_small(x,C);
		// printf("%lld = %lld * %lld)  %c",x,  ans, x/ans,  j!=10?' ': '\n');
		printf("%lld%c", ans, j!=10?' ': '\n');
	}
}

int main() {

	int t, cas = 0;
	srand(time(NULL));  
	scanf("%d", &t);
	while(t -- ){
		cas++;
		printf("Case #%d: \n", cas);
		scanf("%d%d", &N, &J);
		LL max_count = (LL) 1 << (N-2);

		for(int i = 0; i < max_count; i++) {
			memset(s, 0, sizeof(s));
			digit(i);
			bool flag = true;
			for(int j = 2; j <= 10; j++) {
				LL x = inter(j);
				if(Miller_Rabin(x,TIME)) {
					flag = false;
					break;
				} 
			}
			if(flag) {
				output();
				cnt++;
				if(cnt >= J) break;
			}
		}
	}
}