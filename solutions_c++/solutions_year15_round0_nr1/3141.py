#include <cstdio>
#include <queue>
#include <algorithm>
#include <iostream>
#include <cstring>

using namespace std;

typedef long long ll;

const int N = 10010;
const int inf = ~0U >> 2;

int n, k;
int ans;

struct PointDivideConquer{
    struct Edges{
        int to, w, next;
    }e[N << 1];
    int size, box[N];
    bool del[N];
    int vec[N], left, right;
    int cnt[N];
    
    void init_map(){
        memset(box, -1, sizeof(box)), size = 0;
    }
    void clear(){
        memset(del, false, sizeof(del));
    }
    void add(int x, int y, int w){
        e[size].to = y;
        e[size].w = w;
        e[size].next = box[x];
        box[x] = size++;
    }
    
    int total_size, new_root, min_child_size;
    
    int get_sum(int x, int fa){
        cnt[x] = 1;
        for(int i = box[x]; ~i; i = e[i].next){
            int to = e[i].to;
            if(to == fa || del[to]) continue;
            cnt[x] += get_sum(to, x);
        }
        return cnt[x];
    }
    void dfs(int x, int fa){
        int mx = 0;
        for(int i = box[x]; ~i; i = e[i].next){
            int to = e[i].to;
            if(to == fa || del[to]) continue;
            dfs(to, x);
            mx = max(mx, cnt[to]);
        }
        mx = max(mx, total_size - cnt[x]);
        if(mx < min_child_size) min_child_size = mx, new_root = x;
    }
    int find_root(int root){
        total_size = get_sum(root, -1);
        min_child_size = inf;
        dfs(root, -1);
        return new_root;
    }
    void get_dis(int x, int fa, int dis){
        vec[right++] = dis;
        for(int i = box[x]; ~i; i = e[i].next){
            int to = e[i].to;
            if(to == fa || del[to]) continue;
            get_dis(to, x, dis + e[i].w);
        }
    }
    int get_ans(int left, int right){
        int ret = 0;
        sort(vec + left, vec + right);
        int l = left, r = right - 1;
        while(l < r){
            if(vec[l] + vec[r] < k) l++;
            else if(vec[l] + vec[r] > k) r--;
            else{
                if(vec[l] == vec[r]){
                    ret += (r - l) * (r - l + 1) / 2;
                    break;
                }
                int ll = l, rr = r;
                while(vec[ll] == vec[l]) ll++;
                while(vec[rr] == vec[r]) rr--;
                ret += (ll - l) * (r - rr);
                l = ll, r = rr;
            }
        }
        return ret;
    }
    bool solve(int root){
        root = find_root(root);
        
        del[root] = true;
        
        left = right = 1;
        for(int i = box[root]; ~i; i = e[i].next){
            int to = e[i].to;
            if(del[to]) continue;
            get_dis(to, root, e[i].w);
            ans -= get_ans(left, right);
            left = right;
        }
        ans += get_ans(0, right);
        
        if(ans) return true;
        for(int i = box[root]; ~i; i = e[i].next){
            int to = e[i].to;
            if(del[to]) continue;
            if(solve(to)) return true;
        }
        return false;
    }
};

PointDivideConquer pdc;

int main(){
    while(scanf("%d", &n), n){
        pdc.init_map();
        for(int i = 1, x, y; i <= n; ++i){
            while(scanf("%d", &x), x){
                scanf("%d", &y);
                pdc.add(i, x, y);
                pdc.add(x, i, y);
            }
        }
        while(scanf("%d", &k), k){
            pdc.clear();
            ans = 0;
            puts(pdc.solve(1) ? "AYE" : "NAY");
        }
        puts(".");
    }
    return 0;