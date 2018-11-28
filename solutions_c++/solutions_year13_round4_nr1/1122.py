#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
#define ABS(a) (a) < 0 ? -(a) : (a)

struct p_t
{
    int p;
    int t;
    int n;
    p_t(){}
    p_t(int a, int b,int c) : p(a), t(b), n(c){}
    bool operator<(const p_t& that) const
    {
        return this->p < that.p;
    }
};

int N;
int cost(int o, int e)
{
    int i = ABS(e-o);
    int ret = 0;
    int j = 0;
    while(i--)
        ret += (N-j++);
    return ret;
}

int _cost[101][101];
int nn[101];
int out[20010];
int main()
{
    int T;
    scanf("%d", &T);
    for(int tcase=1; tcase<=T; ++tcase){
        fprintf(stderr, "Case #%d\n", tcase);
        int M;
        scanf("%d %d", &N, &M);
        vector<p_t> pp;
        long long org = 0ll;
        for(int i=0; i < M; ++i){
            int o, e, n;
            p_t p;
            scanf("%d %d %d", &o, &e, &n);
            //for(int i=0; i < n; ++i){
            //    pp.push_back(p_t(o, 0));
            //    pp.push_back(p_t(e, 1));
            //}
            pp.push_back(p_t(o, 0, n));
            pp.push_back(p_t(e, 1, n));
            org += (cost(o, e) * n);
        }
        int n = (int)pp.size();

        for(int i=0; i < 101; ++i){
            for(int j=0; j < 101; ++j){
                _cost[i][j] = cost(i, j);
            }
        }
        //if(tcase==4)
        //fprintf(stderr, "%lld\n", org);

        sort(pp.begin(), pp.end());
        long long new_charge = 0;
        while(true){
            int idx_i = -1;
            int idx_j = -1;
            int dist = 987654321;
            for(int i=0; i < n; ++i){
                if(!pp[i].n)continue;
                if(pp[i].t == 1) continue;
                for(int j=0; j < n; ++j){
                    if(pp[i].p > pp[j].p) continue;
                    if(!pp[j].n) continue;
                    if(pp[j].t == 0) continue;
                    if(pp[j].p - pp[i].p < dist){
                        dist = pp[j].p - pp[i].p;
                        idx_i = i;
                        idx_j = j;
                    }
                }
            }
            if(idx_i != -1){
                int co = _cost[pp[idx_i].p][pp[idx_j].p];
                new_charge += co;
        //if(tcase==4)
         //       fprintf(stderr, "hit %d %d %d %lld\n", idx_i, idx_j, co, new_charge);
                pp[idx_i].n -= 1;
                pp[idx_j].n -= 1;
            }
            else
                break;
        }
        long long ans=org-new_charge;
        printf("Case #%d: %lld\n", tcase, ans);
        //if(tcase==4)break;
    }
    return 0;
}
