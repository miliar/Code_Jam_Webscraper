#include <bits/stdc++.h>
using namespace std;
const int INF = 1e9;
const int N = 222222;
char buf[N];
int belong0[N], belong1[N];
vector<int> A[N];
map<string, int> mp;
int n, m;
int h(string s)
{
        if (mp.find(s) == mp.end()) mp[s] = m++;
        return mp[s];
}

void get(vector<int> &A)
{
        A.clear();
        gets(buf); 
        istringstream in(buf);
        string t; 
        while (in>> t){
                A.push_back(h(t));
        }
}

int ret;
void dfs(int k = 2){
        if (k == n){
                int z = 0;
                for(int i = 0 ; i < m; i++) if (belong0[i] && belong1[i]){
                        ++z;
                }
                if(z < ret) ret = z;
        }
        else{
                for(auto it : A[k])  {
                        ++belong0[it];
                }
                dfs(k+1);
                for(auto it : A[k]) {
                        --belong0[it];
                }
                for(auto it : A[k]) {
                        ++belong1[it];
                }
                dfs(k+1);
                for(auto it : A[k]) {
                        --belong1[it];
                }
        }
}

int main(){

#ifndef ONLINE_JUDGE
        freopen("C-small-attempt0.in", "r", stdin);
        freopen("out.txt", "w", stdout);
#endif


        int t,ca=1;
        scanf("%d", &t);
        while(t--){
                mp.clear(); m = 0;
                scanf("%d", &n); getchar();
                for(int i = 0; i < n; i++) {
                        get(A[i]);
                }
                for(auto it: A[0]) {
                        ++belong0[it];
                }
                for(auto it: A[1]) {
                        ++belong1[it];
                }
                ret = INF;
                dfs();
                printf("Case #%d: %d\n", ca++, ret);
                for(auto it: A[0]) {
                        --belong0[it];
                }
                for(auto it: A[1]) {
                        --belong1[it];
                }

        }

        return 0;
}
