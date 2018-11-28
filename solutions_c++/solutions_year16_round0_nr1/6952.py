#include <bits/stdc++.h>
#define ll long long int
#define pii pair <int,int>
#define f first
#define s second
#define pi acos(-1.0)
#define pb push_back
using namespace std;

template < class T > inline T gcd(T a, T b) {while(b) {a %= b; swap(a, b);} return a;}
inline int nxt() {int wow; scanf("%d", &wow); return wow;}
inline ll lxt() {ll wow; scanf("%lld", &wow); return wow;}

int main()
{
  //  freopen("out.txt","w",stdout);
	int t = nxt(), cse=0;
	while(t--){
        ll i, n, c = 0, hit[15] = {0}, k, j, x, rem;
        n = lxt();
        if(n == 0){
            printf("Case #%d: INSOMNIA\n", ++cse);
            goto mara;
        }
        for(i=1;  ;i++){
            k = i * n;
            x = k;
            while(x){
                rem = x % 10;
                hit[rem] = 1;
                x /= 10;
            }
            c = 0;
            for(j=0; j<10; j++) if(hit[j] == 1) c++;
            if (c == 10){
                printf("Case #%d: %lld\n", ++cse, k);
                goto mara;
            }
        }
        mara:;
	}
	return 0;
}
