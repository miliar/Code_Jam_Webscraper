#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t,r,n,i,pl[110],ng[110],ans;
    char s[110];
    scanf("%d", &t);
    for(r = 1; r <=t; r++){
        scanf("%s", s);
        if(s[0] == '+'){
            pl[0] = 0;
            ng[0] = 1;
        }
        else{
            pl[0] = 1;
            ng[0] = 0;
        }
        for(i = 1; s[i] != '\0'; i++){
            if(s[i] == '+'){
                pl[i] = min(pl[i-1], ng[i-1] + 1);
                ng[i] = min(pl[i-1] + 1, ng[i-1] + 2);
            }
            else{
                pl[i] = min(pl[i-1] + 2, ng[i-1] + 1);
                ng[i] = min(pl[i-1] + 1, ng[i-1]);
            }
        }
        ans = min(pl[i-1], ng[i-1] + 1);
        printf("Case #%d: %d\n", r, ans);
    }
    return 0;
}

