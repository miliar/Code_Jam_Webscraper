# include <bits/stdc++.h>
using namespace std;

int main(){
    freopen("B-large.in", "r", stdin);
    freopen("Blargeout.txt", "w", stdout);
    int cases, caseno=0, sum, i;
    char st[105];
    scanf("%d", &cases);
    while(cases--){
        sum = 0;
        scanf("%s", st);
        for (i=1; st[i]; i++){
            if (st[i]!=st[i-1]) sum++;
        }
        if (st[i-1]=='-') sum++;
        printf("Case #%d: %d\n", ++caseno, sum);
    }
    return 0;
}
