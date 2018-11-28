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
#define LIM 100005

using namespace std;

typedef long long large;
typedef pair<int,int> ii;
typedef pair<int,ii> tri;
typedef deque<int> di;
typedef deque<ii> dii;

int main(void){
	int nc, caso;
	large n, a, b, m;
	set<int> nu;
	//READ("A.txt");
	scanf("%d", &nc);
	loop(caso, 0, nc){
		scanf("%lld", &n);
		printf("Case #%d: ", 1+caso);
		if (n==0) puts("INSOMNIA");
		else{
			nu.clear();
			a=1;
			do{
				b=n*a++;
				m=b;
				while (m>0){
					nu.insert(m%10);
					m/=10;
				}
			}while (nu.size()<10);
			printf("%lld\n", b);
		}
	}
	return 0;
}

