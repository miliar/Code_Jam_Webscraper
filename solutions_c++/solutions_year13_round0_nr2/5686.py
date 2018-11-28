#include <stdio.h>
using namespace std;
 
int main (){
    int T, N, M, arr[105][105], max_row[105], max_col[105], tcase = 1;
    scanf ("%d",&T);
    while (T--){
        scanf ("%d%d",&N,&M);
        for (int i=0;i<N;i++)    for (int j=0;j<M;j++)  scanf ("%d",&arr[i][j]);
        
        //Get max row 
        for (int i=0;i<N;i++){
            int mx = arr[i][0];
            for (int j=0;j<M;j++)   if (arr[i][j]>mx)   mx = arr[i][j];
            max_row [i] = mx;
        }
        
        //Get max col
        for (int j=0;j<M;j++){
            int mx = arr[0][j];
            for (int i=0;i<N;i++)   if (arr[i][j]>mx)   mx = arr[i][j];
            max_col [j] = mx;
        }
        
        //Process
        bool flag = true;
        for (int i=0;i<N;i++){
            for (int j=0;j<M;j++){
                if (arr[i][j]<max_row[i] && arr[i][j]<max_col[j]){
                    flag = false;
                    break;
                }
            }
            if (!flag) break;
        }
        if (flag){
            printf ("Case #%d: YES\n", tcase++);
        }
        else {
            printf ("Case #%d: NO\n", tcase++);
        }
    }
}