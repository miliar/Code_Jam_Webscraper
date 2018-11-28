#include<cstdio>
#include<iostream>
#include<algorithm>

using namespace std;

int main(){
    freopen("D-large.in", "r", stdin);
    freopen("out", "w", stdout);
    int T;
    int cnt = 0;
    int N;
    double naomi[1010], ken[1010];
    scanf("%d", &T);
    while(T--){
        scanf("%d", &N);
        for(int i = 0; i < N; i++)
            cin >> naomi[i];
        for(int i = 0; i < N; i++)
            cin >> ken[i];
        sort(naomi, naomi+N);
        sort(ken, ken+N);
        int ans1 = N, ans2 = 0;
        int h = 0, t = N-1;
        for(int i = N-1; i >= 0; i--){
            if(ken[i] > naomi[t]){
                h++;
                ans1--;
            }
            else t--;
        }
        h = 0, t = N-1;
        for(int i = N-1; i >= 0; i--){
            if(naomi[i] > ken[t]){
                h++;
                ans2++;
//                cout << "use " << naomi[i] << "  > " << ken[t] << ", naomi win\n";
            }
            else t--;
        }
        printf("Case #%d: %d %d\n", ++cnt, ans1, ans2);
    }
    return 0;
}
