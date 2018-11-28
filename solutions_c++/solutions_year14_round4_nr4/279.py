#include<cstdio>
#include<cstring>
#include<vector>
using namespace std;
char str[123][123];
int w[123];

struct node {
    int to[26];
} nt[123];
int tcnt = 0;
int init_node() {
    memset(nt[tcnt].to,0,sizeof(nt[tcnt].to));
    return tcnt++;
}
void add(char *s) {
    int now=0;
    for(int i=0; s[i]; i++) {
        if(nt[now].to[s[i]-'A'] == 0)
            nt[now].to[s[i]-'A'] = init_node();
        now = nt[now].to[s[i]-'A'];
    }
}

void cls() {
    tcnt=0;
    init_node();
}

int main() {
    int ti;
    scanf("%d",&ti);
    for(int ca=1; ca<=ti; ca++) {
        int n,m;
        scanf("%d%d",&m,&n);
        for(int i=0; i<m; i++) {
            scanf("%s",str[i]);
        }
        for(int i=0; i<m; i++)w[i]=0;

        int ans = 0, num = 0;

        while(1) {
            vector<int>cnt[8];
            for(int i=0; i<m; i++) {
                cnt[w[i]].push_back(i);
            }
            int flag = 1;
            for(int i=0; i<n; i++) {
                if(cnt[i].size() == 0) {
                    flag = 0;
                    break;
                }
            }

            if(flag) {
                int has = 0;
                for(int i=0; i<n; i++) {
                    cls();
                    for(int j=0; j<cnt[i].size(); j++) {
                        add(str[cnt[i][j]]);
                    }
                    has += tcnt;
                }
                if(has > ans) {
                    ans = has;
                    num = 1;
                } else if(has == ans) {
                    num++;
                }
            }




            int cc = 0;
            w[cc]++;
            while(w[cc]==n&&cc<m) {
                w[cc] = 0;
                cc++;
                w[cc] ++;
            }
            if(cc==m)break;
        }
        printf("Case #%d: %d %d\n",ca,ans,num);
    }
}
