#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <numeric>
#include <algorithm>
#include <sstream>
#include <fstream>

#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>

#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <assert.h>

#define decltype(X) __typeof(X)
#define REP(i, n) for(int i=0; i<(int)n; i++)
#define FOR(it, c) for(decltype((c).begin()) it = (c).begin(); it!=(c).end(); it++)
#define ALL(c) (c).begin(), (c).end()
typedef long long ll;

using namespace std;

#define MOD 1000002013

struct oep_t{
    oep_t(ll o_, ll e_, ll p_):o(o_), e(e_), p(p_){;};
    ll o;
    ll e;
    ll p;
};

bool oep_less(oep_t left, oep_t right)
{
    if(left.o == right.o){
        return (left.e > right.e);
    }
    return left.o < right.o;
}
ll total_pay(vector<oep_t> oeps, ll N)
{
    ll totalpay = 0;
    for(auto oep:oeps){
        ll dist = oep.e - oep.o;
        ll pay = dist * N - dist * (dist - 1 + 0) / 2;
        pay = pay % MOD;
        ll pay_p = (pay * oep.p) % MOD;
        totalpay = (totalpay + pay_p )%MOD;
    }
    return totalpay;
}
void print_oeps(vector<oep_t> oeps){
    ;
#if 0
    for(auto oep: oeps){
        printf("o=%lld, e=%lld, p=%lld\n", oep.o, oep.e, oep.p);
    }
#endif
}
void testcase(int t)
{
	string result_str = "OK";
    ll N, M;
    cin >> N >> M;
    
    vector<oep_t> oeps;
    for(int m=0;m<M;m++){
        ll o, e, p;
        cin >> o >> e >> p;
        oep_t oep(o, e, p);
        oeps.push_back(oep);
    }

    vector<oep_t> init_oeps = oeps;
    vector<oep_t> final_oeps;
    while(! oeps.empty()){
        // printf("current...\n");
        print_oeps(oeps);
        /* longest path */
        vector<oep_t> next;
        vector<oep_t> oep_sorted = oeps;
        sort(oep_sorted.begin(), oep_sorted.end(), oep_less);
        
        oep_t cur_item = *(oep_sorted.begin());
        for(auto it = oep_sorted.begin(); it!=oep_sorted.end(); it ++){
            if(it == oep_sorted.begin()){
                continue;
            }
            if(it->o <= cur_item.e && it->e > cur_item.e){
                // printf("match!\n");
                // next.push_back(cur_item);
                // next.push_back(oep_t(cur_item.o, it->e, min(it->p, cur_item.p)));
                if(it->o != cur_item.e){
                    // printf("test1 it->o=%lld, it->e=%lld, cur_item.o=%lld, cur_item.e=%lld \n", it->o, it->e, cur_item.o, cur_item.e);
                    next.push_back(oep_t(it->o, cur_item.e, max(it->p, cur_item.p)));
                }
                if(it->p > cur_item.p && it->e != cur_item.e){
                    // printf("test2\n");
                    next.push_back(oep_t(cur_item.e, it->e, it->p - cur_item.p));
                }else if(it->p < cur_item.p && it->o != cur_item.o){
                    // printf("test3\n");
                    next.push_back(oep_t(cur_item.o, it->o, cur_item.p - it->p));
                }else{
                    ;
                }
                cur_item = oep_t(cur_item.o, it->e, min(it->p, cur_item.p));
            }else{
                // printf("no match!\n");
                next.push_back(*it);
            }
            
        }
        final_oeps.push_back(cur_item);
        oeps = next;
    }
    
    ll start = total_pay(init_oeps, N);
    // printf("start_oeps\n");
    print_oeps(init_oeps);
    ll end = total_pay(final_oeps, N);
    // printf("final_oeps\n");
    print_oeps(final_oeps);
    ll diff = (start - end + MOD) % MOD;
    // printf("start=%lld, end=%lld, diff=%lld\n", start, end, diff);
    
	cout << "Case #" << (t+1) << ": " << diff << endl;
}

int main(int argc, char *argv[]) {
	int T;
	// ios::sync_with_stdio(false);

    if(argc >= 2){
        int fd = open(argv[1], O_RDONLY);
        if(fd == -1){
            fprintf(stderr, "failed to open [%s]\n", argv[1]);
            exit(1);
        }
        int ret = dup2(fd, 0);
        if(ret == -1){
            fprintf(stderr, "failed to dup2[%s]\n", argv[1]);
            exit(1);
        }
    }
	cin >> T;
	for(int t=0;t<T;t++){
		testcase(t);
	}
	return 0;
}

