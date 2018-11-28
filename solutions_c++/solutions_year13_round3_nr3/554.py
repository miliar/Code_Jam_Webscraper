//--BY--©--WA-
#include<iostream> //cout, cin, getline

#include<algorithm> //find, reaplce, swap, sort, lower_bound, uper_bound, binnary_search...
#include<vector> //push_back, size, resize, 
#include<string>
#include<queue> //empty, front, back, push
#include<stack> //push, top, empty
#include<map>
#include<set>
#include<list> //spajazny zoznam .. vsetko v O(1)

#include<stdio.h> //printf, scanf, getchar, putchar
#include<math.h> //cos, sin, exp, pow, sqrt,  flnoor, cell
#include<stdlib.h> //atio, atl, strtod, strtol, atof, abs, 
#include<ctype.h> //isalnum, isalpha, isdigit, islower, isupper, toupper, tolower, 
#include<string.h> //strcm, strstr, strlen,

using namespace std;

#define FOREACH(obj,it) for(__typeof(obj.begin()) it = (obj).begin(); it != (obj).end(); (it)++)
#define FOR(i,a,b) for(int i=a; i<=b; i++)
#define FORD(i,a,b) for(int i=a; i>=b; i--)
#define REP(i,a,b) for(int i=a; i<b; i++)
#define DEBUG(V,S) FOR(i,0,S-1){cout << i << ". " << V[i] << endl;}

#define PB push_back
#define PII pair<int,int>
#define PLL pair<ll,ll>
#define MP make_pair
#define fi first
#define se second

#define SIZE(s) (int) (s).size()

#define INF 987654321
#define EPS 1e-9
#define ld long double // %Lf, double %lf
#define ll long long   // %llf

//--------------------------------------------------------------------------------------

#define MAX 11

int T, n_tribes;
int d[MAX], n[MAX], w[MAX], e[MAX], s[MAX], delta_d[MAX], delta_p[MAX], delta_s[MAX];
int wall[1202];
vector<PII> days[676065];

int main()
{	
	scanf("%d", &T);
	FOR (caser, 1, T) {
		FOR (i, 0, 676064) days[i].clear();
		FOR (i, 0, 1200) wall[i] = 0;

		scanf("%d", &n_tribes);
		FOR (i, 0, n_tribes-1) {
			scanf("%d %d %d %d %d %d %d %d", &d[i], &n[i], &w[i], &e[i], &s[i], &delta_d[i], &delta_p[i], &delta_s[i]);
			FOR (j, 0, n[i]-1) {
				days[d[i]+j*delta_d[i]].PB(MP(i,j));
			}
		}

		int res = 0;

		FOR(i, 0, 676060) {
			FOR (j, 0, SIZE(days[i])-1) {
				PII t = days[i][j];
				int tribe = t.fi;
				int n_att = t.se;
				int west = w[tribe] + delta_p[tribe]*n_att;
				int east = e[tribe] + delta_p[tribe]*n_att;
				int str = s[tribe] + delta_s[tribe]*n_att;

				//printf("%d, %d, %d\n", west, east, str);

				FOR (z, west*2, east*2) {
					if (wall[z+600] < str) {
						res++;
						break;
					}
				}
			}

			FOR (j, 0, SIZE(days[i])-1) {
				PII t = days[i][j];
				int tribe = t.fi;
				int n_att = t.se;
				int west = w[tribe] + delta_p[tribe]*n_att;
				int east = e[tribe] + delta_p[tribe]*n_att;
				int str = s[tribe] + delta_s[tribe]*n_att;

				FOR (z, west*2, east*2) {
					wall[z+600] = max(wall[z+600], str);
				}
			}
		}

		printf("Case #%d: %d\n", caser, res);
	}
	return 0;
}
