#include<stdio.h>
#include<vector>

using namespace std;

vector<int> ans;

int r1[4][4], r2[4][4];

int main(){
    int n;
    scanf("%d", &n);
    int cas = 1;
    int i, j;

    for(cas = 1; cas <= n; cas++){
        ans.clear();
        printf("Case #%d: ", cas);
        int n1, n2;
        scanf("%d", &n1);
        for(i = 0 ; i < 4; i++){
            for(j = 0; j < 4; j++){
                scanf("%d", &r1[i][j]);
            }
        }
        scanf("%d", &n2);
        for(i = 0 ; i < 4; i++){
            for(j = 0; j < 4; j++){
                scanf("%d", &r2[i][j]);
            }
        }

        for(i = 0; i < 4; i++){
            int tmp = r1[n1 - 1][i];
            int count = 0;
            for(j = 0; j < 4; j++){
                if(tmp == r2[n2 - 1][j]){
                    ans.push_back(tmp);
                }
            }
        }

        if(ans.size() == 1){
            printf("%d\n", ans[0]);
        }
        else if(ans.size() > 1){
            printf("Bad magician!\n");
        }
        else{
            printf("Volunteer cheated!\n");
        }
        
    }

}
