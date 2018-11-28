#include <cstdio>
#include <cstring>
using namespace std;

#define abs(x) ((x)>0 ? (x) : -(x))
#define mp(x, y) make_pair((x), (y))

typedef long long ll;

int q;
char s[2][42];
int n;
ll mip[2][42], mis[2][42], map[2][42], mas[2][42];
ll mie[42];
ll t[42];

void f1(char *s, int n, int id)
{
	for(int i=n-1; i>=0; i--) {
		if(s[i]=='?') {
			mis[id][i]=(i==n-1 ? 0 : mis[id][i+1]);
			mas[id][i]=9*t[n-1-i]+(i==n-1 ? 0 : mas[id][i+1]);
		} else {
			mis[id][i]=(s[i]-'0')*t[n-1-i]+(i==n-1 ? 0 : mis[id][i+1]);
			mas[id][i]=(s[i]-'0')*t[n-1-i]+(i==n-1 ? 0 : mas[id][i+1]);
		}
	}
	for(int i=0; i<=n-1; i++) {
		if(s[i]=='?') {
			mip[id][i]=0+(i==0 ? 0 : mip[id][i-1]);
			map[id][i]=9*t[n-1-i]+(i==0 ? 0 : map[id][i-1]);
		} else {
			mip[id][i]=(s[i]-'0')*t[n-1-i]+(i==0 ? 0 : mip[id][i-1]);
			map[id][i]=(s[i]-'0')*t[n-1-i]+(i==0 ? 0 : map[id][i-1]);
		}
	}
}

int chk[42];
ll bc, bj;

void submit(ll _bc, ll _bj)
{
	if(abs(_bc-_bj)<abs(bc-bj) || (abs(_bc-_bj)==abs(bc-bj) && _bc<bc) || (abs(_bc-_bj)==abs(bc-bj) && _bc==bc && _bj<bj)) {
		bc=_bc;
		bj=_bj;
	}
}

int main()
{
	t[0]=1;
	for(int i=1; i<=18; i++) t[i]=10*t[i-1];
	scanf("%d\n", &q);
	for(int x=1; x<=q; x++) {
		scanf("%s %s\n", s[0], s[1]);
		printf("Case #%d: ", x);
		n=strlen(s[0]);
		f1(s[0], n, 0);
		f1(s[1], n, 1);
		bc=mip[0][n-1];
		bj=mip[1][n-1];
		for(int i=0; i<n; i++) {
			if(s[0][i]=='?' || s[1][i]=='?' || s[0][i]==s[1][i]) {
				chk[i]=(i==0 ? 1 : chk[i-1]);
			} else {
				chk[i]=0;
			}
		}
		for(int i=0; i<n; i++) {
			if(chk[i]) {
				if(s[0][i]=='?' && s[1][i]=='?') {
					mie[i]=(i==0 ? 0 : mie[i-1]);
				} else if(s[0][i]=='?') {
					mie[i]=(i==0 ? 0 : mie[i-1])+(s[1][i]-'0')*t[n-1-i];
				} else {
					mie[i]=(i==0 ? 0 : mie[i-1])+(s[0][i]-'0')*t[n-1-i];
				}
			}
		}
		if(chk[n-1]) {
			submit(mie[n-1], mie[n-1]);
		}
		for(int i=n-1; i>=0; i--) {
			if(i>0 && !chk[i-1]) continue;
			for(int d1=0; d1<=9; d1++) {
				for(int d2=0; d2<=9; d2++) {
					if((s[0][i]=='?' || s[0][i]-'0'==d1) && (s[1][i]=='?' || s[1][i]-'0'==d2)) {
						if(d1>d2) {
							ll n1=(i==0 ? 0 : mie[i-1])+d1*t[n-1-i]+(i==n-1 ? 0 : mis[0][i+1]);
							ll n2=(i==0 ? 0 : mie[i-1])+d2*t[n-1-i]+(i==n-1 ? 0 : mas[1][i+1]);
							submit(n1, n2);
						} else if(d1<d2) {
							ll n1=(i==0 ? 0 : mie[i-1])+d1*t[n-1-i]+(i==n-1 ? 0 : mas[0][i+1]);
							ll n2=(i==0 ? 0 : mie[i-1])+d2*t[n-1-i]+(i==n-1 ? 0 : mis[1][i+1]);
							submit(n1, n2);
						}
					}
				}
			}
		}
		for(int i=0; i<n; i++) printf("%lld", (bc/t[n-1-i])%10);
		printf(" ");
		for(int i=0; i<n; i++) printf("%lld", (bj/t[n-1-i])%10);
		printf("\n");
	}

	return 0;
}
