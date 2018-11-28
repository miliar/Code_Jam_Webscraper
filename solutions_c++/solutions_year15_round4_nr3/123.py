#include <set>
#include <map>
#include <ctime>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <algorithm>

#define MaxN 1000010
#define MaxC 22220

using namespace std;

int T, N;
map<string, int> num;
int s, t;
string nows;
string mats[MaxN];
int tot;
bool exist[220][MaxC];
bool Is[MaxC][2];
int to[MaxN][2], c_tot;
int Ans = 0, INF = 10000000;
int u[MaxN * 50], v[MaxN * 50], w[MaxN * 50], prep[MaxN * 50], head[MaxN], nowhead[MaxN], Dis[MaxN];
int stack[MaxN], path[MaxN], cnt[MaxN], m0, Total;

void AddEdge(int a, int b, int c) {
    ++m0; v[m0] = b; u[m0] = a; w[m0] = c; prep[m0] = head[a]; head[a] = m0;
    ++m0; v[m0] = a; u[m0] = b; w[m0] = 0; prep[m0] = head[b]; head[b] = m0;
}

void Get_L(int i, int cas) {
    char c;
    scanf("%c", &c);
    nows = "";
    while(c != '\n') {
        if(c == ' ') {
            if(!num[nows]) {
                num[nows] = ++tot;
            }
            exist[i][num[nows]] = 1;
            if(cas < 2)
                Is[num[nows]][cas] = 1;
            nows = "";
        }
        else {
            nows += c;
        }
        scanf("%c", &c);
    }
    if(!num[nows])
        num[nows] = ++tot;
    exist[i][num[nows]] = 1;
    if(cas < 2)
        Is[num[nows]][cas] = 1;
    nows = "";
}

void Sap(){
    for(int i=0;i<=t;++i)
        nowhead[i]=head[i];
    memset(Dis, 0, sizeof(Dis));
    memset(path, 0, sizeof(path));
    memset(cnt, 0, sizeof(cnt));
    memset(stack, 0, sizeof(stack));
    int p=s,f=INF,flag;
    cnt[0]=Total;
    while(Dis[s]<Total){
        flag=0;
        stack[p]=f;
        for(int i=nowhead[p];i;i=prep[i])
            if(w[i]&&Dis[v[i]]+1==Dis[p]){
                nowhead[p]=i;
                path[v[i]]=i;
                flag=1;
                if(f>w[i])
                    f=w[i];
                p=v[i];
                if(p==t){
                    Ans+=f;
                    for(;p!=s;p=u[path[p]]){
                        w[path[p]]-=f;
                        w[path[p]^1]+=f;
                    }
                    f=INF;
                }
                break;
            }
        if(flag)
            continue;
        int minx=Total+1,tmp;
        for(int i=head[p];i;i=prep[i])
            if(w[i]&&Dis[v[i]]<minx){
                minx=Dis[v[i]];
                tmp=i;
            }
        nowhead[p]=tmp;
        --cnt[Dis[p]];
        tmp=Dis[p];
        Dis[p]=minx+1;
        ++cnt[Dis[p]];
        if(!cnt[tmp])
            break;
        if(p!=s)
            f=stack[p=u[path[p]]];
    }
}

int main() {
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);
    int i, j, T0 = 0;
    scanf("%d", &T);
    for( ; T; --T) {
        tot = 0;
        scanf("%d", &N);
        num.clear();
        memset(exist, 0, sizeof(exist));
        memset(Is, 0, sizeof(Is));
        Ans = 0; m0 = 1;
        memset(head, 0, sizeof(head));
        char c;
        getchar();
        Get_L(1, 0);
        Get_L(2, 1);
        for(i = 3; i <= N; ++i)
           Get_L(i, 2);
        for(i = 1; i <= tot; ++i) {
            if(Is[i][0] && Is[i][1]) {
                ++Ans;
                continue;
            }
            if(Is[i][0]) {
                to[i][0] = ++c_tot;
            }
            if(Is[i][1]) {
                to[i][1] = ++c_tot;
            }
            if((!Is[i][0]) && (!Is[i][1])) {
                to[i][0] = ++c_tot;
                to[i][1] = ++c_tot;
                --Ans;
            }
        }
        t = c_tot + N - 1;
        for(i = 1; i <= tot; ++i) {
            if(Is[i][0] && Is[i][1])
                continue;
            if(Is[i][0]) {
                AddEdge(s, to[i][0], 1);
                for(j = 3; j <= N; ++j) {
                    if(exist[j][i])
                        AddEdge(to[i][0], c_tot + j - 2, INF);
                }
                continue;
            }
            if(Is[i][1]) {
                AddEdge(to[i][1], t, 1);
                for(j = 3; j <= N; ++j) {
                    if(exist[j][i])
                        AddEdge(c_tot + j - 2, to[i][1], INF);
                }
                continue;
            }
            AddEdge(s, to[i][0], 1);
            AddEdge(to[i][1], t, 1);
            for(j = 3; j <= N; ++j) {
                if(exist[j][i])
                    AddEdge(to[i][0], c_tot + j - 2, INF);
            }
            for(j = 3; j <= N; ++j) {
                if(exist[j][i])
                    AddEdge(c_tot + j - 2, to[i][1], INF);
            }
        }
        Total = t + 1;
        Sap();
        printf("Case #%d: %d\n", ++T0, Ans);
    }
    return 0;
}

