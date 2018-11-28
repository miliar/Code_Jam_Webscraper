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
#define LIM 2006

using namespace std;

typedef long long large;
typedef pair<int,int> ii;
typedef pair<int,ii> tri;
typedef deque<int> di;
typedef deque<ii> dii;

int ct[300], nu[10], n;
char s[LIM];
int main(void){
	int nc, caso, i, j;
	//READ("A.txt");
	scanf("%d", &nc);
	loop(caso, 0, nc){
		scanf("%s", s);
		n=strlen(s);
		SET(nu, 0);
		SET(ct, 0);
		loop(i, 0, n) ct[s[i]]+=1;
		nu[6]=ct['X'];
		ct['I']-=nu[6];
		ct['S']-=nu[6];

		nu[0]=ct['Z'];
		ct['E']-=nu[0];
		ct['R']-=nu[0];
		ct['O']-=nu[0];

		nu[2]=ct['W'];
		ct['T']-=nu[2];
		ct['O']-=nu[2];

		nu[4]=ct['U'];
		ct['F']-=nu[4];
		ct['O']-=nu[4];
		ct['R']-=nu[4];

		nu[5]=ct['F'];
		ct['I']-=nu[5];
		ct['V']-=nu[5];
		ct['E']-=nu[5];

		nu[8]=ct['G'];
		ct['E']-=nu[8];
		ct['I']-=nu[8];
		ct['T']-=nu[8];
		ct['H']-=nu[8];

		nu[3]=ct['H'];
		ct['T']-=nu[3];
		ct['R']-=nu[3];
		ct['E']-=2*nu[3];

		nu[7]=ct['V'];
		ct['S']-=nu[7];
		ct['E']-=2*nu[7];
		ct['N']-=nu[7];

		nu[1]=ct['O'];
		ct['N']-=nu[1];
		ct['E']-=nu[1];

		nu[9]=ct['I'];
		printf("Case #%d: ", caso+1);
		loop(i, 0, 10) loop(j, 0, nu[i]) putchar('0'+i);
		puts("");
	}
	return 0;
}

