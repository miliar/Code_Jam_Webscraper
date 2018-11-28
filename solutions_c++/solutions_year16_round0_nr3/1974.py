#include <bits/stdc++.h>
#define loop(i, a, b) for(i=a; i<b; i++)
#define rev(i, a, b) for(i=a; i>=b; i--)
#define SET(x, a) memset(x, a, sizeof(x))
#define PI (acos(-1))
#define READ(fi) freopen(fi, "r", stdin)
#define WRITE(fi) freopen(fi, "w", stdout)
#define x first
#define y second
#define pb push_back
#define pf push_front
#define LIM 120000005
#define L2 8000000

using namespace std;

typedef long long large;
typedef pair<int,int> ii;
typedef pair<int,ii> tri;
typedef deque<int> di;
typedef deque<ii> dii;
bool isp[LIM];
int pr[L2], np;

void sieve(){
	int i, j;
	large k;
	np=1; pr[0]=2;
	loop(i, 0, LIM) isp[i]=(i%2!=0);
	isp[0]=isp[1]=false;
	isp[2]=true;
	for(i=3; i<LIM; i+=2){
		if (isp[i]){
			pr[np++]=i;
			k=large(i)*i;
			if (k<LIM)
				for(j=i*i; j<LIM; j+=i)
					isp[j]=false;
		}
	}
}

int nu[35];
large k, divi[10];

large divisor(large k){
	if (k<large(LIM) && isp[int(k)]) return k;
	int i;
	large a;
	loop(i, 0, np){
		if (k%pr[i]==0) return large(pr[i]);
		a=large(pr[i]); a*=a;
		if (a>=k) break;
	}
	return k;
}

int main(void){
	int nc, caso;
	int n, j, i, a, b, ct;

	//scanf("%d", &nc);
	nc=1;
	sieve();
	printf("np=%d\n", np);
	printf("%d\n", pr[np-1]);
	WRITE("c2.txt");
	loop(caso, 0, nc){
		//scanf("%d %d", &n, &j);
		n=32; j=500;
		printf("Case #%d:\n", caso+1);
		SET(nu, 0);
		nu[0]=nu[n-1]=1;
		nu[1]=-1;
		ct=0;
		do{//todos los numeros posibles
			nu[1]++;
			i=1;
			while (nu[i]>1){
				nu[i++]=0;
				nu[i]++;
			}
			if (nu[n-1]==1){
				loop(b, 2, 11){
					loop(a, 0, np){
						k=0;
						rev(i, n-1, 0) k=(k*b+nu[i])%pr[a];
						//printf("k=%lld b=%d\n", k, b);
						if (k==0) break;
					}
					if (a==np) break;
					divi[b-2]=pr[a];
				}
				if (b==11){
					ct++;
					rev(i, n-1, 0) printf("%d", nu[i]);
					loop(b, 2, 11) printf(" %lld", divi[b-2]);
					cerr<<"number "<<ct<<endl;
					puts("");
				}
			}
		}while (nu[n]==0 && ct<j);
	}
	return 0;
}

