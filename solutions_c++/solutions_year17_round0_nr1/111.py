#include <cstdio>
#include <algorithm>
#include <cmath>
#include <queue>
#include <vector>
#include <map>
#include <set>

using namespace std;

typedef long long LL;
typedef pair<int , int> P2;
typedef pair<pair<int , int> , int> P3;
typedef pair<pair<int , int> , pair<int , int> > P4;
#define Fst first
#define Snd second
#define PB(a) push_back(a)
#define MP(a , b) make_pair((a) , (b))
#define M3P(a , b , c) make_pair(make_pair((a) , (b)) , (c))
#define M4P(a , b , c , d) make_pair(make_pair((a) , (b)) , make_pair((c) , (d)))
#define repp(i,a,b) for(int i = (int)(a) ; i < (int)(b) ; ++i)
#define repm(i,a,b) for(int i = (int)(a) ; i > (int)(b) ; --i)

int T;
char s[1111];
bool b[1111];
int K;

int main(){
	scanf("%d" , &T);
	repp(i,1,T+1){
		printf("Case #%d: " , i);
		scanf(" %s%d" , s , &K);
		int len = 0;
		while(s[len] != 0){
			b[len] = s[len] == '+';
			++len;
		}
		int ans = 0;
		repp(j,0,len){
			if(b[j]) continue;
			if(j > len - K){
				ans = -1;
				break;
			}
			repp(x,0,K){
				b[j+x] = !b[j+x];
			}
			++ans;
		}
		if(ans < 0) printf("IMPOSSIBLE\n");
		else printf("%d\n" , ans);
	}
	return 0;
}
