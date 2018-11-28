#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <deque>

using namespace std;

#define MAXNUM 2000010
int n;
double a[1010], b[1010];
deque<double>qa;
deque<double>qb;
bool cmp(deque<double>a, deque<double>b){
    int len = a.size();
    for(int i = 0; i < len; i++){
        if(a[i] < b[i]) return false;
    }
    return true;
}
bool visit[1010];
int cal(){
    memset(visit, 0, sizeof(visit));
    int flag = 0;
    int ans = 0;
    for(int i = 0; i < n; i++){
        flag = 0;
        for(int j = 0; j < n; j++){
            if(b[j] > a[i] && visit[j] == 0){
                visit[j] = 1;
                ans++;
                flag = 1;
                break;
            }
        }
        if(flag == 0){
            for(int j = 0; j < n; j++){
                if(visit[j]==0){
                    visit[j] = 1;
                    break;
                }
            }
        }
    }
    return n - ans;
}
int main(){
    //freopen("in.txt", "r", stdin);
    //freopen("D-large.in","r", stdin);
    //freopen("D-large.out","w", stdout);
    int t;
    scanf("%d", &t);
    for(int cas = 1; cas <= t; cas++){
        scanf("%d", &n);
        qa.clear();
        qb.clear();
        for(int i = 0; i < n; i++) scanf("%lf", a+i);
        for(int j = 0; j < n; j++) scanf("%lf", b+j);
        sort(a, a+n); sort(b, b+n);
        for(int i = 0; i < n; i++) {
            qa.push_back(a[i]);
            qb.push_back(b[i]);
        }
        //for(int i = 0; i < n; i++) cout << qa[i] << "\n";
        //cout << qa.size()<<"d\n";
        while(1){
            if(qa.size() == 0) break;
            if(cmp(qa, qb) == 1) {break;}
            qa.pop_front();
            qb.pop_back();
        }
        int ans1 = qa.size();
        int ans2 = cal();
        printf("Case #%d: %d %d\n", cas, ans1, ans2);
    }
    return 0;
}

