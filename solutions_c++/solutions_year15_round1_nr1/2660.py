#include <cstdio>
#include <algorithm>

using namespace std;

const int MAXN = 1010;

int t, n;
int a[MAXN];

int main(){
  FILE* input=freopen("mush.in","r",stdin);
    FILE* output=freopen("mush.out","w",stdout);
	scanf("%d", &t);

	for(int q=0; q<t; q++){
		scanf("%d", &n);
		for(int i=0; i<n; i++){
			scanf("%d", &a[i]);
		}
		int rate = max(a[n-2] - a[n-1], 0);
                int ratemax=0;
                for(int i=0; i<n-1; i++){
                    ratemax=max(ratemax, a[i] - a[i+1]);
                }
		int rj1=0, rj2=0;
		for(int i=0; i<n-1; i++){
            rj1 += max(0, a[i] - a[i+1]);
            rj2 += min(a[i], ratemax);
        }

        printf("Case #%d: %d %d\n", q+1,  rj1, rj2);
	}

}
