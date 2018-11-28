#include<cstring>
#include<cstdio>
#include<iostream>
using namespace std;


int main()
{
    //freopen("A-large.in","r", stdin);
    //freopen("A-large.out", "w", stdout);
    int T,smax;
    int a[1100];
    while(scanf("%d", &T)!=EOF){
        for(int t=1; t<=T; t++){
            scanf("%d", &smax);
            char tmp[1100];
            scanf("%s", &tmp);
            for(int i=0; i<=smax; i++){
                a[i] = tmp[i]-'0';
            }
            int res = 0;
            int now_stand = a[0];
            for(int i=1; i<=smax; i++){
                if(now_stand<i){
                    res += i-now_stand;
                    now_stand = i;
                }
                now_stand += a[i];
            }
            printf("Case #%d: %d\n", t, res);
        }
    }
    return 0;
}
