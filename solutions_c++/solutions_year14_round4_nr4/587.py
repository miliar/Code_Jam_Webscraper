#include <iostream>
#include <cmath>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <queue>
#include <set>

using namespace std;
int num[100], id[100];
int n,m;
string word[100];
int chd[100][26];
int sz;
int cnt2;
void Insert(string s) {
    int len = s.size();
    int p = 0;
    for(int k = 0; k < len; k++) {
        int ch = s[k] - 'A';
        if(chd[p][ch] != -1) {
            p = chd[p][ch];
        } else {
            sz++;
            chd[p][ch] = sz;
            p = sz;
        }
    }
}

int GetDone(int who) {
    sz = 1;
    memset(chd, -1, sizeof(chd));
    for(int i = 1; i <= n; i++) {
        if(id[i] == who) {
            Insert(word[i]);
        }
    }
    return sz;
}
int ans;
void dfs(int cur) {
    if(cur == n + 1) {
        memset(num, 0 ,sizeof(num));
        for(int j = 1; j <= n; j++) {
            num[id[j]]++;
        }
        for(int i =  1; i <= m; i++) {
            if(!num[i]) {
                return ;
            }
        }
        // for(int i =  1; i <= n; i++) {
        //     cout<<id[i]<<" ";
        // }
        //cout<<endl;
        int sum1 = 0;
        for(int i =1 ; i <= m; i++) {
            sum1 += GetDone(i);
            //cout<<sum1<<endl;
        }
        //cout<<sum1<<endl;
        if(sum1 > ans) {
            ans = sum1;
            cnt2 = 0;
        }
        if(sum1 == ans) {
            cnt2++;
        }
        return ;
    }
    bool flag = false;
    for(int i = 1; i <= m; i++) {
        id[cur] = i;
        dfs(cur + 1);
    }
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    
    int T = 0, CAS = 0;
    scanf("%d", &T);
    while(T--) {
        cnt2 = 0;
        memset(id, 0, sizeof(id));
        scanf("%d%d", &n, &m);
        for(int i = 1; i <= n; i++) {
            cin>>word[i];
        }
        ans = 0;
        dfs(1);
        printf("Case #%d: %d %d\n", ++CAS,ans, cnt2);
        // sz = 1;
        // memset(chd, -1, sizeof(chd));
        // Insert(1, "AAA");
        // Insert(1, "AAB");
        // cout<<sz<<endl;
    }
}