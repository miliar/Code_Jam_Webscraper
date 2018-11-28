#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
using namespace std;

typedef int ll;

const int MAXN = 10000000;
int f[MAXN+10];

bool is_pal(int t)
{
    int num[20];
    int l = 0;
    memset(num, 0, sizeof(num));
    while(t){
	    num[l++] = t%10;
        t /= 10;
	}
    for(int i = 0, j = l-1; i < j; i++, j--)
        if(num[i] != num[j])
            return false;
    return true;
}

int main()
{
    ll A, B;
    int T, cas = 1;
    f[0] = 0;
    for(ll i = 1; i <= 100000; i++) {
	    f[i] = f[i-1];
        if(is_pal(i) && is_pal(i*i))
            f[i]++;
	}
    freopen("C-small-attempt1.in", "r", stdin);
    freopen("C-small-attempt1.out", "w", stdout);
    scanf("%d", &T);
    while(T--){
        scanf("%d %d", &A, &B);        
        ll sa = (ll)sqrt(A*1.0);
        if(sa*sa < A) sa++;
        ll sb = (ll)sqrt(B*1.0); 
		printf("Case #%d: %d\n", cas++, f[sb]-f[sa-1]);
	}
    return 0;
}
