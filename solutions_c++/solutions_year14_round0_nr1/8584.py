#include <iostream>
#include <cstdio>
#include <cstdio>
#include <vector>
#include <map>
#include <set>

#define PII pair<int, int>
#define s(n) scanf("%d", &n)

using namespace std;

int main(){
    
    int t, a1[5][5], a2[5][5], r1, r2;    
    s(t);
    for(int z = 1; z <= t; z++){
        s(r1);
        for(int i = 1; i <= 4; i++){
            for(int j = 1; j <= 4; j++)
                s(a1[i][j]);
        }
        
        s(r2);
        for(int i = 1; i <= 4; i++){
            for(int j = 1; j <= 4; j++)
                s(a2[i][j]);
        }
        int cnt = 0, ans;
        for(int i = 1; i <= 4; i++){
            for(int j = 1; j <= 4; j++){
                if(a1[r1][i] == a2[r2][j]){
                    ans = a1[r1][i];
                    cnt++;
                }
            }
        }
        if(cnt == 0)
            printf("Case #%d: Volunteer cheated!\n", z);
        else if(cnt > 1)
            printf("Case #%d: Bad magician!\n", z);
        else
            printf("Case #%d: %d\n", z, ans);
    }
    return 0;
}
