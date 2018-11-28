# include <iostream>
# include <cstdio>
# include <cstring>
# include <map>

using namespace std;

map<string,int> e;
int v[20000];
int n, cnt;
int getid(const string&s) {
    int &t = e[s];
    if(t == 0) {
        ++cnt;
        v[cnt] = 0;
        t = cnt;
    }
    return t;
}

int calc(int mask) {
    int ret = 0;
    for(int i = 1; i <= cnt; ++i) 
        if((v[i] & mask) != v[i] && (v[i] & mask) != 0) ++ret;
    return ret;
}

char buff[200000+20];

int main() {
    freopen("c.in","r",stdin);
    int T, cas = 0; scanf("%d", &T);
    while(T--) {
        printf("Case #%d: ", ++cas);
        scanf("%d", &n);
        gets(buff); 
        e.clear();
        cnt = 0;
        int ans = 0x3f3f3f3f;
        for(int i = 0; i < n; ++i) {
            gets(buff); 
            int len = strlen(buff); 
            string s;
            for(int k = 0; k < len; ++k) 
                if(isalpha(buff[k])) s.push_back(buff[k]);
                else if(s.size()) {
                    v[getid(s)] |= (1<<i);
                    s.clear();
                }
            if(s.size()) {
                v[getid(s)] |= (1<<i);
                s.clear();
            }
        }
        for(int mask = 0; mask < (1<<(n-2)); ++mask) 
            ans = min(ans, calc(mask << 2 | 1));
        printf("%d\n", ans);
    }
    return 0;
}

