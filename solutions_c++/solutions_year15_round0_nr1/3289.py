#include<iostream>
#include<cstdio>
#include<cstdlib>

using namespace std;

const int MAXN = 1005;
char s[MAXN];

int main(){

    int T;
    scanf("%d",&T);
    for(int i=1;i<=T;i++){
        int N;
        scanf("%d",&N);
        int mx = 0;
        int cnt = 0;
        scanf("%s",s);
        
        cnt = s[0] - '0';
        for(int j=1;j<=N;j++){
            if(cnt < j){
                mx = max(mx,j-cnt);
            }
            cnt += s[j] - '0';
        }

        printf("Case #%d: %d\n",i,mx);
    }
}
