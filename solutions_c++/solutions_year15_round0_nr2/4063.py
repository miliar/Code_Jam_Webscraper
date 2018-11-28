#include <bits/stdc++.h>
using namespace std;
int p[6];
#define AA first
#define BB second
#define PB push_back
#define MP make_pair
typedef pair< vector<int> , int> PI;
set<long long> s;
const long long MOD = (1e12) + 7;
long long h(vector<int> v){
    int t = 0;
    for(int i = 0; i < v.size(); i ++) {
        t += v[i];
        t *= 10;
        t %= MOD;
    }
    return t;
}
void pv(vector<int> v){
    printf("%d :",v.size());
    for(auto i : v)
        cout << " " << i;
    cout << endl;
}
int bfs(vector<int> v)
{
    sort(v.begin(), v.end());
    queue< PI > Q;
    Q.push(MP(v, 0));
    s.insert(h(v));
    while(!Q.empty()) {
        vector<int> t = Q.front().AA;
        int ti = Q.front().BB, n = t.size();
        Q.pop();
        int x = t[n - 1];
        if(x == 0) return ti;
        vector<int> pp(t);
        for(int i = 0;i < n;i ++) pp[i] --;
        if(!s.count(h(pp))) {
            s.insert(h(pp));
            Q.push(MP(pp, ti + 1));
        }
        t.pop_back();
        for(int i = 1; i < x; i ++) {
            vector<int> qp(t);
            qp.PB(i);
            qp.PB(x - i);
            sort(qp.begin(), qp.end());
            if(!s.count(h(qp))) {
                s.insert(h(qp));
                Q.push(MP(qp, ti + 1));
            }
        }
    }
}
int main()
{
    int T, __case = 0, d;
    freopen("out3.txt","w",stdout);
    scanf("%d", &T);
    while(T--) {
        s.clear();
        scanf("%d", &d);
        for(int i = 0; i < d; i ++)
            scanf("%d", &p[i]);
        int maxx = *max_element(p, p + d), ans;
        if(maxx <= 3)
            ans = maxx;
        else {
            vector<int> temp(p, p + d);
            ans = bfs(temp);
        }
        printf("Case #%d: %d\n",++__case,ans);
    }
    return 0;
}
