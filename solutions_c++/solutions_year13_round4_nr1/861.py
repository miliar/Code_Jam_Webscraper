#include<cstdio>
#include<algorithm>
#include<cstring>
#include<vector>
#include<queue>
#include<map>
#include<set>
using namespace std;
#define INF (1<<29)
#define min(x,y) (((x)<(y))?(x):(y))
#define max(x,y) (((x)>(y))?(x):(y))
#define FOR(i,x,y) for(int i=(x);i<(y);++i)
#define FOE(i,x,y) for(int i=(x);i<=(y);++i)
#define CLR(i) memset(i,0,sizeof(i))
#define ll long long

struct card{
	int price, next;
	bool ok;

	card(){}
	card(int price, int next):price(price),next(next){ ok = 1; }

	bool operator<(const card &d)const{
		return price<d.price;
	}
} c[10005];

struct people{
	int o,e,num;

	people(){}
	people(int o,int e):o(o),e(e){}

	void input(){
		scanf("%d%d%d",&o,&e,&num);
	}

	bool operator<(const people &d)const{
		return o<d.o;
	}
} p[105];

int T;
int n,m,a[105],num;

int main(){
	scanf("%d",&T);
	FOE(t,1,T){
		CLR(a); num=0;

		scanf("%d%d",&n,&m);
		int origin = 0;
		for (int i=0;i<m;++i){
			p[i].input();
			int tmp = n;
			FOR(x,p[i].o,p[i].e){
				origin += tmp*p[i].num; --tmp;
			}
		}
		sort(p,p+m);

		int ans=0;
		FOE(x,1,n){
			FOR(i,0,m){
				if (p[i].o == x){
					FOR(j,0,p[i].num) c[num++] = card(0,n);
					a[p[i].e] += p[i].num;
				}
			}

			sort(c,c+num);
			int pos=0;
			FOR(i,0,a[x]){
				while (!c[pos].ok) ++pos;

				ans += c[pos].price;
				c[pos].ok = 0;
			}

			FOR(i,0,num){
				c[i].price += c[i].next;
				--c[i].next;
			}
		}
		printf("Case #%d: %d\n",t,origin - ans);
	}
	return 0;
}
