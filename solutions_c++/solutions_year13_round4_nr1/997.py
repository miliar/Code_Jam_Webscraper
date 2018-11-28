#include <queue>
#include <algorithm>
#include <cstdio>
using namespace std;

const int den = 1000002013;

int testcase() {
    int n, m;
    int ocz = 0, res = 0;
    scanf("%d %d", &n, &m);
    pair<int, int> wyd[2*m];
    priority_queue<pair<int, int> > pula;
    for(int i = 0; i < m; i ++) {
        int o, e, p;
        scanf("%d %d %d", &o, &e, &p);
        wyd[2*i] = make_pair(o, -p);
        wyd[2*i + 1] = make_pair(e, p);
        int dis = e - o;
        long long add = dis * n - (dis*(dis-1)) / 2;
        add *= (long long)p;
//         printf("\t%d pasażerów z %d do %d, płacą %lld\n", p, o, e, add);
        add %= (long long)den;
        ocz += add;
        ocz %= den;
    }
    sort(wyd, wyd+2*m);
    for(int i = 0; i < 2*m; i ++) {
        if(wyd[i].second < 0)
            pula.push(make_pair(wyd[i].first, -wyd[i].second));
        else {
            int e = wyd[i].first;
            int p = wyd[i].second;
            while(p>0) {
                pair<int, int> ost = pula.top();
                pula.pop();
                int mi = min(ost.second, p);
                ost.second -= mi;
                p -= mi;
                int dis = e - ost.first;
                long long add = dis * n - (dis*(dis-1)) / 2;
                add *= (long long)mi;
//                 printf("\t%d biletów z %d do %d, płacą %lld\n", mi, ost.first, e, add);
                add %= (long long)den;
                res += add;
                if(ost.second > 0)
                    pula.push(ost);
            }
        }
    }
    ocz += den;
    ocz -= res;
    ocz %= den;
    return ocz;
}

int main() {
    int t;
    scanf("%d", &t);
    for(int i = 1; i <= t; i ++)
        printf("Case #%d: %d\n", i, testcase());
}
