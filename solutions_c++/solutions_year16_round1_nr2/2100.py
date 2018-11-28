#include <bits/stdc++.h>
using namespace std;

struct Node
{
    vector<int> num;
    bool operator < (const Node &cmp) const {
        return num[0] < cmp.num[0];
    }
}vec[110];
bool flag[110];
int matrix[51][51];
int n;
bool same(vector<int> &a, vector<int> &b)
{
    for(int i = 0; i < n; i++) {
        if(a[i] != b[i]) {
            return false;
        }
    }
    return true;
}
bool check(int which)
{
    /*
    printf("which=%d\n", which);
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < n; j++) {
            cout << matrix[i][j] << " " ;
        }
        cout << endl;
    }
    cout << endl;
    */
    int pt = 0;
    vector<int> tmp[51];
    bool ok[51];
    memset(ok, false, sizeof(ok));
    if(which == 1) {
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < n; j++) {
                tmp[i].push_back(matrix[j][i]);
            }
        }
        for(int i = 0; i < 2 * n - 1; i++) if(!flag[i]) {
 //           printf("i=%d\n", i);
            for(int j = 0; j < n; j++) if(!ok[j]){
                if(same(vec[i].num, tmp[j])) {
                    ok[j] = true;
                }
            }
        }
        int cnt = 0, id;
        for(int i = 0; i < n; i++) {
            if(!ok[i]) {
                cnt++;
                id = i;
            }
        }
        if(cnt == 1) {
            for(int i = 0; i < n; i++) {
                cout << " " << tmp[id][i];
            }
            cout << endl;
            return true;
        }
        return false;
    } else {
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < n; j++) {
                tmp[i].push_back(matrix[i][j]);
            }
        }
        for(int i = 0; i < 2 * n - 1; i++) if(!flag[i]) {
            for(int j = 0; j < n; j++) if(!ok[j]){
                if(same(vec[i].num, tmp[j])) {
                    ok[j] = true;
                }
            }
        }
        int cnt = 0, id;
        for(int i = 0; i < n; i++) {
            if(!ok[i]) {
                cnt++;
                id = i;
            }
        }
        if(cnt == 1) {
            for(int i = 0; i < n; i++) {
                cout << " " << tmp[id][i];
            }
            cout << endl;
            return true;
        }
        return false;
    }
}
bool dfs(int dep, int choose, int last, int which)
{
    if(choose == n) {
        return check(which);
    }
    if(dep == 2 * n - 1) return false;
    if(dfs(dep + 1, choose, last, which)) {
        return true;
    }
    if(last == -1 || vec[dep].num[0] != vec[last].num[0]) {
        flag[dep] = true;
        vector<int> tmp;
        if(which == 1) {
            for(int i = 0; i < n; i++) {
                matrix[choose][i] = vec[dep].num[i];
            }
        } else {
            for(int i = 0; i < n; i++) {
                matrix[i][choose] = vec[dep].num[i];
            }
        }
        if(dfs(dep + 1, choose + 1, dep, which)) {
            return true;
        }
        flag[dep] = false;
    }
    return false;
}
int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int t,ca=1;
    cin >> t;
    while(t--) {
        cout << "Case #" << ca << ":";
        ca++;
        cin >> n;
        map<int, int> mp;
        for(int i = 0; i < 2 * n - 1; i++) {
            for(int j = 0; j < n; j++) {
                int x;
                cin >> x;
                mp[x]++;
            }
        }
        vector<int> ret;
        for(auto it: mp) {
            if(it.second & 1) {
                ret.push_back(it.first);
            }
        }
        sort(ret.begin(), ret.end());
        for(int i = 0; i < n; i++) {
            cout << " " << ret[i];
        }
        cout << endl;
    }
    return 0;
}
