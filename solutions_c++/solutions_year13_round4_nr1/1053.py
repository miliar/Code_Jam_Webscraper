#include<cstdio>
#include<cstdlib>
#include<iostream>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<vector>
#include<queue>
#include<functional>

#define mp(a,b) make_pair(a,b)
#define ms(a,b) memset(a, b, sizeof(a))

typedef struct Edge Edge;

using namespace std;

const int MOD = 1000002013;

struct Edge{
    int o, e;
    Edge(int _o, int _e){
        this->o = _o;
        this->e = _e;
    }
    bool operator < (const Edge &a) const {
        if(this->o != a.o) return (this->o < a.o);
        if(this->e != a.e) return (this->e > a.e);
        return false;
    }
};

int N, M;
vector< Edge > edge;

int findCost(void){
    int cost = 0;
    for(int i = 0; i < (int)edge.size(); i++){
        int k = edge[i].e - edge[i].o;
        cost += (2*N+1-k)*k/2;
    }
    return cost;
}

int main(){
//    freopen("pa.out", "w", stdout);
    int T;
    int cnt = 0;
    scanf("%d", &T);
    while(T--){
        scanf("%d%d", &N, &M);
        edge.clear();
        for(int i = 0; i < M; i++){
            int o, e, p;
            scanf("%d%d%d", &o, &e, &p);
            for(int j = 0; j < p; j++){
                edge.push_back(Edge(o, e));
            }
        }
        int ori = findCost();
        sort(edge.begin(), edge.end());
        for(int i = 0; i < (int)edge.size(); i++){
            for(int j = i+1; j < (int)edge.size(); j++){
/*                printf("now: %d -> %d\n", edge[i].o, edge[i].e);
                printf("tar: %d -> %d\n", edge[j].o, edge[j].e);*/
                if(edge[j].o <= edge[i].e && edge[j].e > edge[i].e){
                    int tmp = edge[j].e;
                    edge[j].e = edge[i].e;
                    edge[i].e = tmp;
                }
            }
        }
        int after = findCost();
        printf("Case #%d: %d\n", ++cnt, (ori-after)%MOD);
    }
    return 0;
}
