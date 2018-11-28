#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;

const int MAXN = 1010;
int a[MAXN];
int p[MAXN];
int N,_;

bool check(){
    for (int i=1;i<=N;i++){
        bool flag = true;
        for (int j=1;j<i && flag;j++){
            if (a[p[j]]<a[p[j+1]]) continue;
            flag = false;
        }
        for (int j=i+1;j<N && flag;j++){
            if (a[p[j]]>a[p[j+1]]) continue;
            flag = false;
        }
        if(flag) return true;
    }
    return false;
}

int work(){
    int cnt = 0;
    for (int i=1;i<=N;i++)
        for (int j=i+1;j<=N;j++)
            if(p[i]>p[j]) cnt++;
    return cnt;
}

int main(){
    //freopen("in.txt","r",stdin);
    freopen("B-small-attempt1.in","r",stdin);
    freopen("B-small-attempt1.out","w",stdout);
    scanf("%d",&_);
    int cas = 0;
    while(_--){
        scanf("%d",&N);
        for (int i=1;i<=N;i++) scanf("%d",&a[i]);
        for (int i=1;i<=N;i++) p[i]=i;
        int ans = 1<<30;
        do{
            //cout << "!!" << endl;
            if (check()) ans = min(ans,work());
        } while (next_permutation(p+1,p+N+1));
        printf("Case #%d: %d\n",++cas,ans);
    }
}
