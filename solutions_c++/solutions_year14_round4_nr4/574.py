#include<cstdio>
#include<vector>
#include<iostream>
using namespace std;
typedef long long ll;
int TC, p[10], ans, ansc, n, m;
vector<string> g[5];
char str[100];
string s[100];
int inspect(int sid){
    int ret = 1;
    sort(g[sid].begin(), g[sid].end());
    for(int i = 0; i < g[sid].size(); ++i){
        ret += g[sid][i].length();
        if(i > 0){
            for(int j = 0; j < g[sid][i-1].length() && j < g[sid][i].length() && g[sid][i][j] == g[sid][i-1][j]; ++j) --ret;
        }
    }
    return ret;
}
void brute(int id){
    if(id < m){
        for(int i = 0; i < n; ++i){
            p[id] = i;
            brute(id + 1);
        }
    }
    else{
        for(int i = 0; i < n; ++i){
            g[i].clear();
        }
        //printf("start brute\n");
        for(int i = 0; i < m; ++i){
            //printf("brute %d\n", p[i]);
            g[p[i]].push_back(s[i]);
        }
        int ret = 0;
        for(int i = 0; i < n; ++i){
            if(g[i].empty()) return;
            ret += inspect(i);
        }
        if(ret > ans){
            ans = ret;
            ansc = 1;
        }
        else if(ret == ans){
            ansc ++;
        }
        //printf("end brute %d %d\n", ans, ansc);
    }
}
int main(){
    scanf("%d", &TC);
    for(int tc = 1; tc <= TC; ++tc){
        scanf("%d %d", &m, &n);
        for(int i = 0; i < m; ++i){
            scanf("%s", str);
            s[i] = string(str);
        }
        ans = 0; ansc = 0;
        brute(0);
        printf("Case #%d: %d %d\n", tc, ans, ansc);
    }
    //system("pause");
}
