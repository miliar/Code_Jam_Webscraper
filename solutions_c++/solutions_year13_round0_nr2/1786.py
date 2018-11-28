
#include <cstdlib>
#include <cstdio>
#include <cstring>
using namespace std;

int lawn[101][101], garden[101][101], rowMax[101], colMax[101];

int main(){
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int t, n, m, i, j, k, kase = 0, max;

    scanf("%d", &t);
    while(t--){
        scanf("%d%d", &n, &m);
        for(i = 0; i < n; i++){
            for(j = 0; j < m; j++){
                scanf("%d", &lawn[i][j]);
                garden[i][j] = 100;
            }
        }
        for(i = 0; i < n; i++){
            rowMax[i] = 0;
            for(j = 0; j < m; j++){
                if(lawn[i][j] > rowMax[i])
                    rowMax[i] = lawn[i][j];
            }
        }
        for(i = 0; i < m; i++){
            colMax[i] = 0;
            for(j = 0; j < n; j++){
                if(lawn[j][i] > colMax[i])
                    colMax[i] = lawn[j][i];
            }
        }
        for(k = 0; k < n + m; k++){
            max = 0;
            bool row = true;
            int ind = 0;
            for(i = 0; i < n; i++){
                if(rowMax[i] > max){
                    max = rowMax[i];
                    ind = i;
                }
            }
            for(i = 0; i < m; i++){
                if(colMax[i] > max){
                    max = colMax[i];
                    ind = i;
                    row = false;
                }
            }
            if(row == true){
                rowMax[ind] = 0;
                for(j = 0; j < m; j++){
                    if(garden[ind][j] > max)
                        garden[ind][j] = max;
                }
            }
            else{
                colMax[ind] = 0;
                for(i = 0; i < n; i++){
                    if(garden[i][ind] > max)
                        garden[i][ind] = max;
                }
            }
        }
        bool posssible = true;
        for(i = 0; i < n; i++){
            for(j = 0; j < m; j++){
                if(lawn[i][j] != garden[i][j]){
                    posssible = false;
                    break;
                }
            }
        }
        printf("Case #%d: ", ++kase);
        if(posssible == true) printf("YES\n");
        else printf("NO\n");
    }
    return 0;
}
