#include <cstdio>
#include <cstdlib>
#include <vector>
#include <iostream>
using namespace std;

#define debug(v) cerr << #v << ": " << (v) << endl

int main(){
    int T;
    scanf("%d", &T);
    for(int t = 0; t < T; ++t){
        int r1, r2;
        int A1[4][4], A2[4][4];
        scanf("%d", &r1);
        for(int i = 0; i < 4; ++i)
            for(int j = 0; j < 4; ++j)
                scanf("%d", &A1[i][j]);

        scanf("%d", &r2);
        for(int i = 0; i < 4; ++i)
            for(int j = 0; j < 4; ++j)
                scanf("%d", &A2[i][j]);

        vector<int> ans;
        
        for(int i = 0; i < 4; ++i){
            for(int j = 0; j < 4; ++j){
                if(A1[r1 - 1][i] == A2[r2 - 1][j]){
                    ans.push_back(A1[r1 - 1][i]);
                }
            }
        }
        if(ans.size() > 1){
            printf("Case #%d: Bad magician!\n", t + 1);
        }
        else if(ans.size() == 1){
            printf("Case #%d: %d\n", t + 1, ans[0]);
        }
        else if(ans.size() == 0){
            printf("Case #%d: Volunteer cheated!\n", t + 1);
        }
    }
    return 0;
}
