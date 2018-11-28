#include <bits/stdc++.h>
using namespace std;
bool found[11];
int main(){
    int T, cases=1;
    long long l;
    freopen("A-large-attempt0.in", "r", stdin);
    freopen("A-large-Counting Sheep.out", "w", stdout);
    scanf("%d", &T);
    while(T--){
        int n=10, i;
        memset(found, false, sizeof(found));
        cin>>l;
        if(l==0){
            printf("Case #%d: INSOMNIA\n", cases++);
            continue;
        }
        for(i=1;n>0;i++){
            long long m = i*l;
            while(m>0){
                if(!found[m%10])n--, found[m%10]=true;
                m/=10;
            }
        }
        printf("Case #%d: %I64d\n", cases++, (i-1LL)*l);
    }
    return 0;
}
