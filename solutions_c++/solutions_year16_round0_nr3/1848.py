#include<bits/stdc++.h>
using namespace std;
#define N 32
#define J 500
char s[40];
int cnt=0;
void dfs(int u,int add){
    if(u==N){
        if(add==0){
            cnt++;
            //printf("(%)")
            printf("%s 3 2 5 2 7 2 9 2 11\n",s);
        }
        if(cnt==J) exit(0);
        return;
    }
    s[u]='0';
    if(u!=0 && u!=N-1)dfs(u+1,add);
    s[u]='1';
    if(u%2) dfs(u+1,add+1);
    else dfs(u+1,add-1);
}
int main(){
    freopen("C.out","w",stdout);
    puts("Case #1:");
    dfs(0,0);
}
