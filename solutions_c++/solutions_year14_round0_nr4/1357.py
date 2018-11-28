#include <cstdio>
#include <algorithm>
#include <cstring>
#include <cmath>
#include <iostream>
#include <sstream>
#include <cstdlib>
#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <map>
#include <bitset>
#include <string>
#include <functional>
#include <utility>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int, int> ii;
typedef vector<ii> vii;

void print_vector(vi v);
void print_array(int* array, int start, int end);

#define FOR(i,a,b) for (int i = (a),_b = (b); i < _b; i++)
#define DOW(i,b,a) for (int i = (b),_a = (a); i > _a; i--)
#define fill(a,v) memset(a, v, sizeof a)
#define checkbit(n,b) ((n >> b) & 1)
#define ALL(a) (a).begin(), (a).end()
#define SZ(a) (int)(a).size()

#define s(n)                        scanf("%d",&n)
#define sc(n)                       scanf("%c",&n)
#define sl(n)                       scanf("%lld",&n)
#define sf(n)                       scanf("%lf",&n)
#define ss(n)                       scanf("%s",n)

int tc, cse = 1, n, dwar, war;
double naomi[1005], ken[1005];
deque<double> naomiq, kenq;
vector<double> naomiv, kenv;


int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	s(tc);
	while(tc--){
		s(n);
		FOR(i, 0, n) sf(naomi[i]);
		FOR(i, 0, n) sf(ken[i]);
		sort(naomi, naomi + n);
		sort(ken, ken + n);
		FOR(i, 0, n) naomiq.push_back(naomi[i]);
		FOR(i, 0, n) kenq.push_back(ken[i]);
		dwar = war = 0;
		FOR(i, 0, n){
			if(naomiq[0] < kenq[0]){
				naomiq.pop_front();
				kenq.pop_back();
			} else {
				naomiq.pop_front();
				kenq.pop_front();
				dwar++;
			}
		}
		FOR(i, 0, n) naomiv.push_back(naomi[i]);
		FOR(i, 0, n) kenv.push_back(ken[i]);
		FOR(i, 0, n){
			if(naomiv[0] > kenv[SZ(kenv)-1]){
				war += SZ(kenv);
				naomiv.clear();
				kenv.clear();
				break;
			} else {
				FOR(j, 0, SZ(kenv)){
					if(kenv[j] > naomiv[0]){
						naomiv.erase(naomiv.begin());
						kenv.erase(kenv.begin() + j);
						break;
					}
				}
			}
		}
		printf("Case #%d: %d %d\n", cse++, dwar, war);
	}
	return 0;
}

void print_array(int* array, int start, int end){
  printf("[");
  FOR(i, start, end){
	printf("%d ", array[i]);
  }
  printf("]");
  printf("\n");
}

void print_vector(vi v){
  printf("[");
  FOR(i, 0, v.size()){
	printf("%d ", v[i]);
  }
  printf("]");
  printf("\n");
}