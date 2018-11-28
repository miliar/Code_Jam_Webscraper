#include <bits/stdc++.h>

#define INF 0x3F3F3F3F
#define rep(i, a, b) for (int i = int(a); i < int(b); i++)
#define pb push_back
#define pi 3.1415926535897932384626433832795028841971
#define debug(x) cout << #x << " = " << x << endl;
#define debug2(x,y) cout << #x << " = " << x << " --- " << #y << " " << y << "\n";
#define debugM( x, l, c ) { rep( i, 0, l ){ rep( j, 0, c ) printf("%d ", x[i][j]); printf("\n");}}
#define all(S) (S).begin(), (S).end()
#define MAXV 1010000
#define MAXN 110
#define F first
#define S second
#define EPS 1e-9
#define mk make_pair

// freopen("B-small-attempt0.in", "r", stdin);
// freopen("B.sol", "w", stdout);


using namespace std;

typedef pair <int, int> ii;
typedef long long int ll;

ll readInt();

int main(){
	
//	freopen("B-large.in", "r", stdin);
//	freopen("B.txt", "w", stdout);

	char s[110];
	int n = readInt();
	rep( test, 1, n+1 ){
		scanf("%s", s );
		printf("Case #%d: ", test );
		int tam = strlen( s );
		int cont = 0;
		bool aux = 1, aux2 = 0;
		rep( i, 0, tam ){
			if( s[i] == '-' && aux  ) cont += ( 1 + aux2 ), aux = 0;
			if( s[i] == '+' ) aux = 1, aux2 = 1; 
		}
		printf("%d\n", cont );
	}

}

ll readInt () {
    bool minus = false;
    ll result = 0; char ch;

    ch = getchar();
    while (true) {
        if (ch == '-')
            break;
        if (ch >= '0' && ch <= '9') break;
        ch = getchar();
    }
    if (ch == '-')  minus = true;
    else result = ch-'0';
    while (true) {
        ch = getchar();
        if (ch < '0' || ch > '9') break;
        result = result*10 + (ch-'0');
    }
    if (minus) return -result;
    else return result;
}

