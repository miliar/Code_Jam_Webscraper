#include<cstdio>
using namespace std;
#define zero(n) memset(n,0,sizeof(n))
#define init(n) memset(n,-1,sizeof(n))
#define REP(x, n) for(int x = 0; x < (n); x++)
#define FOR(x, b, e) for(int x = (b); x <= (e); x++)
#define FORD(x,b,e) for(int x= (b); x>=e; x--)
#define min(a,b) ((a<b)?(a):(b))
#define max(a,b) ((a>b)?(a):(b))
#define MP make_pair
#define PB push_back

int smax;
char str[1000+10];
int standing;

int main(){
	//freopen("input.in","r",stdin);
	//freopen("output.out","w",stdout);
	int t, cur, cnt;
	scanf("%d",&t);
	REP(T,t){
		scanf("%d %s",&smax,str);
		standing = 0;
		cnt = 0;
		REP(i,smax+1){
			cur = int(str[i]-'0');
			if(standing >= i){
				standing += cur;
			}
			else{
				cnt += i - standing;
				standing += i - standing;
				standing += cur;
			}
		}
		printf("Case #%d: %d\n",T+1,cnt);
	}
	return 0;
}

