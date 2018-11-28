#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <string>
#include <algorithm>
#include <queue>

using namespace std;

#define sf(a) scanf("%d", &a)
#define sfl(a) scanf("%lld", &a)
#define pf(a) printf("%d", a)
#define pfl(a) printf("%lld", a)
#define pln() printf("\n")
#define FOR(i,a,b) for(i=a; i<b; i++)
#define pb push_back

typedef long long int LL;

int main(void){
	int t;
	sf(t);
	int i;
	FOR(i,1,t+1){
		double c, f, x;
		scanf("%lf", &c);
		scanf("%lf", &f);
		scanf("%lf", &x);
//printf("Hello\n");
		double r = 2.0;
		double nr = 2.0;
		double t = 0.0;
		if(c >= x){
			t = x/r;
		}
		else{
			while(true){
				t += c/r;
				nr = r + f;
				if(x/nr < (x-c)/r){
					r = nr;
				}
				else{
					t += (x-c)/r;
					break;
				}
			}
		}
		printf("Case #%d: ", i);
		printf("%lf\n", t);
	}

	//system("pause");
	return 0;
}
