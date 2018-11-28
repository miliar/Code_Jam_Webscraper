#include<cstdio>
#include<cstring>
#include<vector>
#include<queue>
#include<set>
#include<map>
#include<algorithm>
using namespace std;

typedef __int64 ll;

//#define DEBUG


ll N, P;
ll max_id;

ll get_best_rank(ll tid)
{
    ll cur = tid;
    ll id = max_id;
    ll ret = 0;
    if(tid == max_id-1) return max_id;
    if(tid == 0) return 1;
    if(tid == 1) return 2;
    while(cur > 1){
        id /= 2;
        cur = cur-(cur)/2;
        if(id == cur+1) return id;
	}
    printf("tid = %I64d, N = %I64d, p = %I64d\n", tid, N, P);
    return 1;
}

ll get_worst_rank(ll tid)
{
    ll id = max_id;
    ll ret = 0;
    ll cur = tid+1;
    if(cur == 1) return 1;
    while(cur > 1){
        id /= 2;
        ret += id;
        cur /= 2;
        if(cur == 1) return ret+1;
	}
    return ret+1;
    printf("oh no 2");
}

void work()
{
    scanf("%I64d %I64d", &N, &P);
    if(P == 1){
        printf("0 0\n");
        return; 
	}
    max_id = (1LL<<N);
    ll a, b;
    //printf("%I64d\n", max_id);
    ll l = 0, r = max_id-1;
    //max id always win
    a = 0;
    while(l <= r){
        ll mid = (l+r)/2;
        ll rank = get_worst_rank(mid);
        if(rank <= P){
            a = mid;
            l = mid+1;
		}else{
            r = mid-1;
		}
	}
    l = 0;  r = max_id-1;
    while(l <= r){
        ll mid = (l+r)/2;
        ll rank = get_best_rank(mid);
        if(rank <= P){
            b = mid;
            l = mid+1;
		}else{
            r = mid-1;
		}
	}
    
	printf("%I64d %I64d\n", a, b);
}

int main()
{
    int T;
#ifndef DEBUG
    freopen("a-small.in", "r", stdin);
    freopen("a-small.out", "w", stdout);
#endif
    scanf("%d", &T);
    for(int cas = 1; cas <= T; cas++){
		printf("Case #%d: ", cas);
        work();
	}
    return 0;
}


