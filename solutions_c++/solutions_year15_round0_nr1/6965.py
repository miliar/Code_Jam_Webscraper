#include <bits/stdc++.h>
using namespace std;
int main(){
    int T;
    scanf("%d",&T);
    for(int t = 1; t <= T; t++){
        int s;
        char str[1280];
        scanf("%d",&s);
        scanf("%s",str);
        int cnt = 0;
        int peo = 0;
        peo = str[0]-'0';
        for(int i = 1; i < s+1; i++){
            int num = str[i]-'0';
            if(peo < i){
                int res = i-peo;
                cnt += res;
                peo += res;
            }
            peo += num;
        }
        printf("Case #%d: %d\n",t,cnt);
    }
}