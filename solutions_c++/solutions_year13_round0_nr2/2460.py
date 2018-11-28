#include <stdio.h>
using namespace std;
 
int main (){
    int T, N, M, adjacency[105][105], rowmax[105], colmax[105], tcase = 1;
    
     freopen("B.txt", "r", stdin);
    freopen("Bans.txt", "w", stdout);
    scanf ("%d",&T);
    while (T--){
        scanf ("%d%d",&N,&M);
        for (int i=0;i<N;i++)    for (int j=0;j<M;j++)  scanf ("%d",&adjacency[i][j]);
        
        
        for (int i=0;i<N;i++){
            int mx = adjacency[i][0];
            for (int j=0;j<M;j++)   if (adjacency[i][j]>mx)   mx = adjacency[i][j];
            rowmax [i] = mx;
        }
        
       
        for (int j=0;j<M;j++){
            int mx = adjacency[0][j];
            for (int i=0;i<N;i++)   if (adjacency[i][j]>mx)   mx = adjacency[i][j];
            colmax [j] = mx;
        }
        
        
        bool p = true;
        for (int i=0;i<N;i++){
            for (int j=0;j<M;j++){
                if (adjacency[i][j]<rowmax[i] && adjacency[i][j]<colmax[j]){
                    p = false;
                    break;
                }
            }
            if (!p) break;
        }
        if (p){
            printf ("Case #%d: YES\n", tcase++);
        }
        else {
            printf ("Case #%d: NO\n", tcase++);
        }
    }
}
