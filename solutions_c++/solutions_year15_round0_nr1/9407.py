#include <bits/stdc++.h>
using namespace std;
int T, s; char ch;
int main(){
    freopen("A-large.in", "r", stdin);
    freopen("test_out.txt", "w", stdout);
    scanf("%d", &T);
    for(int k=1; k<=T; k++){
        int cnt=-1, ans=0;
        scanf("%d", &s);
        for(int i=0; i<=s; i++){
            scanf(" %c", &ch);
            cnt += ch-'0';
            while(cnt<i){ans++; cnt++;}
        }
        printf("Case #%d: %d\n", k, ans);
    }
}
