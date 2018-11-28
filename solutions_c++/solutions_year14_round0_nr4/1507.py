#include <cstdio>
#include <cstring>
#include <cctype>
#include <cmath>
#include <algorithm>
#include <functional>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <map>
#include <utility>
#include <bitset>
#include <list>
#define FOR(i, a, b) 	for (i=a; i<b; i++)
#define REV(i, a, b) 	for (i=a; i>=b; i--)
#define TR(tipo, c, it) for (tipo::iterator it=(c).begin(); it!=(c).end(); it++)
#define SET(var, c)		memset(var, c, sizeof(var))
#define READ(file)		freopen(file, "r", stdin)
#define WRITE(file)		freopen(file, "w", stdout)
#define pb 				push_back
#define mp              make_pair
#define X				first
#define Y				second
#define PI				(acos(0.0)*2.0)
#define EPS             1e-10
#define INF 			1000000000
#define LIM             1005

using namespace std;
typedef long long 		ll;
typedef vector<int> 	vi;
typedef pair<int, int> 	ii;
typedef vector<ii> 		vii;

double a[LIM], b[LIM];
int n;

int main(void){
	int i, caso, ncasos, n, j, low;
	int cont1, cont2;
	bool vis[LIM];
	setvbuf(stdin, NULL, _IOFBF, 1<<18);
	setvbuf(stdout, NULL, _IOFBF, 1<<18);
	READ("D-large.in");
	WRITE("D-large.out");
	scanf("%d", &ncasos);
	fprintf(stderr, "%d\n", ncasos);
	FOR(caso, 0, ncasos){
		scanf("%d", &n);
		//fprintf(stderr, "n=%d\n", n);
		FOR(i, 0, n){
			scanf("%lf", &a[i]);
		}
		FOR(i, 0, n){
			scanf("%lf", &b[i]);
		}
		sort(a, a+n);
		sort(b, b+n);
		cont1=cont2=0;
		//Deceitful War
		j=0;
		FOR(i, 0, n){
			if (a[n-1-j]>b[n-1-i]){
				cont1++; j++;
				continue;
			}
			if (a[i-j]>b[n-1-i]) cont1++;
		}
		//REAL WAR
		low=0;
		SET(vis, false);
		/*if (caso==3){
			fprintf(stderr, "   a       b\n");
			FOR(i, 0, n) fprintf(stderr, "%.5lf %.5lf\n", a[i], b[i]);
		}
		*/
		FOR(i, 0, n){
			FOR(j, low, n){
				if (!vis[j] && b[j]>a[n-1-i]){
					vis[j]=true;
					cont2++;
					break;
				}
			}
			if (j==n){
				while(vis[low]) low++;
				j=low;
				vis[j]=true;
				low++;
			}
			//fprintf(stderr, "%.5lf vs %.5lf i=%d j=%d cont2=%d\n", a[n-1-i], b[j], i, j, cont2);
		}
		cont2=n-cont2;
		printf("Case #%d: %d %d\n", 1+caso, cont1, cont2);
		fprintf(stderr, "Case #%d: %d %d\n", 1+caso, cont1, cont2);
	}
	return 0;
}

