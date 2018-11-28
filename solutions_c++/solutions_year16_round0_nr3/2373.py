#include <cstdio>
#include <iostream>
#include <cstring>
#include <cmath>
#include <cstdlib>
using namespace std;

typedef unsigned long long U64;
const U64 MAX_INDEEP = 10000;
const U64 TABLE_SIZE = 131071;
U64 sqrt_table[TABLE_SIZE] = {0};

int list[9] = {2,3,5,7,11,13,17,19,61};

U64 mod_pro(U64 x,U64 y,U64 n)
{
    U64 ret=0,tmp=x%n;
    while(y)
        {
            if(y&0x1)if((ret+=tmp)>n)ret-=n;
            if((tmp<<=1)>n)tmp-=n;
            y>>=1;
        }
    return ret;
}
U64 mod(U64 a,U64 b,U64 c)
{
    U64 ret=1;
    while(b)
        {
            if(b&0x1)ret=mod_pro(ret,a,c);
            a=mod_pro(a,a,c);
            b>>=1;
        }
    return ret;
}

bool is_prime(U64 n)
{
    if(n == 2)
        return true;
    U64 k=0,m,a,i;
    int t = 0;
    for(m=n-1;!(m&1);m>>=1,k++);
    while(t < 9)
        {
            a=mod(list[t]%(n-2)+2,m,n);
            if(a!=1)
                {
                    for(i=0;i<k&&a!=n-1;i++)
                        a=mod_pro(a,a,n);

                    if(i>=k)return false;
                }
            t++;
        }
    return true;
}




U64 gcd(U64 a,U64 b) {
    return b ? gcd(b,a % b) : a;
}


class squfof{
	U64 try_ana(U64 N){
		U64 sqrt_n = (U64) sqrt((long double) N);
		U64 P1 = sqrt_n, Q2 = 1, Q1 = N-(U64) P1*P1;
		U64 B, P, Q, step = MAX_INDEEP;
		if(Q1==0)
			return P1;
		while(sqrt_table[Q1%TABLE_SIZE]!=Q1){
            //cout << "loop1" << endl;
			B = (sqrt_n+P1)/Q1;
			P = B*Q1-P1;
			Q = Q2+B*(P1-P);
			P1 = P;
			Q2 = Q1;
			Q1 = Q;
		}
		U64 sqrt_Qi = (U64) sqrt((long double) Q1);
		B = (sqrt_n-P1)/sqrt_Qi;
		P1 = B*sqrt_Qi+P;
		Q2 = sqrt_Qi;
		Q1 = (N-(U64) P1*P1)/Q2;
		P = P1;
		P1 = 0;
		while((P!=P1)&&(step--)){
            //cout << "loop2" << step << endl;
			P1 = P;
			B = (sqrt_n+P1)/Q1;
			P = B*Q1-P1;
			Q = Q2+B*(P1-P);
			Q2 = Q1;
			Q1 = Q;
		}
		return P;
	}
public:
	void init(){
		for (U64 i = 0; i < (1 << 16); i++)
		sqrt_table[i * i % TABLE_SIZE] = i * i;
	}
	U64 analyze(U64 N){
		U64 k, t = 0;
		for(k = 1; t==0||t==1; k++){
			t = gcd(try_ana(k*N), N);
		}
		return t;
	}
};

U64 change(U64 x, U64 base) {
    U64 j = 1, s = 0;
    while (x) {
        s += (x % 2LL) * j;
        x /= 2LL;
        j *= base;
    }
    return s;
}

void output(int x) {
    char str[40];
    int i = 0;
    while (x) {
        str[i++] = (x % 2LL) + '0';
        x /= 2LL;
    }
    str[i] = '\0';
    for (int j = 0; i - j - 1 > j; ++j) {
        swap(str[j], str[i - j - 1]);
    }
    printf("%s", str);
}

int main() {
    int T, n, k;
    squfof s;
    int res[20];
    scanf("%d%d%d", &T, &n, &k);
    printf("Case #1:\n");
    for (U64 i = (1LL<<(n-1))+1; i < (1LL<<n); i += 2LL) {
        bool flag = true;
        for (U64 j = 2; j <= 10; ++j) {
            s.init();
            U64 x = change(i, j);
            if (is_prime(x)) {
                flag = false;
                break;
            }
            U64 ans = s.analyze(x);
            res[j] = ans;
        }
        if (flag) {
            output(i);
            for (int i = 2; i <= 10; ++i) {
                printf(" %d", res[i]);
            }
            printf("\n");
            if (!--k) {
                break;
            }
        }
    }
    return 0;
}
