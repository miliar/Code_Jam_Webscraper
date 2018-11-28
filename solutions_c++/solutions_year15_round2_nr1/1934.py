#include <bits/stdc++.h>
#define ll long long
#define INF 2000000000
#define MAXN 3000009
using namespace std;
int dist[MAXN];
int reverse_num(int x){
    stringstream ss;
    ss << x;
    string temp = ss.str();
    reverse(temp.begin(), temp.end());
    int res = atoi(temp.c_str());
    return res;
}
int main() {
    freopen("C:\\in.txt", "r", stdin);
    freopen("C:\\out2.txt", "w", stdout);
    //ios_base::sync_with_stdio(false);
    //cin.tie(0);
    int t,n;
    int x;
    cin >> t;
    int test_case  = 1;
    while(t--){
        memset(dist, -1, sizeof(dist));
        cin >> x;
        queue<int> q;
        dist[1] = 1;
        q.push(1);
        while(!q.empty()){
            int curr = q.front(); q.pop();
            if(curr == x) break;
            int one_more = curr+1;
            int reversed = reverse_num(curr);
            if(one_more<=MAXN && dist[one_more]==-1){
                dist[one_more] = dist[curr]+1;
                q.push(one_more);
            }
            if(reversed<=MAXN  && dist[reversed] == -1){
                dist[reversed] = dist[curr]+1;
                q.push(reversed);
            }
        }
        printf("Case #%d: %d\n",test_case++, dist[x]);
    }
    return 0;
}
