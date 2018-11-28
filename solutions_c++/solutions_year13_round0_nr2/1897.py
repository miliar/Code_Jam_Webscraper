#include <iostream>
#include <cstdio>
using namespace std;

int t, n, m;
int tab[105][105];
int naj[105], poz[105];

int main(){
    scanf("%d", &t);
    
    for(int q=0; q<t; q++){
        scanf("%d %d", &n, &m);
        
        for(int i=0; i<n; i++)
            for(int j=0; j<m; j++){
                scanf("%d", &tab[i][j]);
                naj[j] = max(naj[j], tab[i][j]); 
                poz[i] = max(poz[i], tab[i][j]);  
            }
            
        bool git = true;
                
        for(int i=0; i<n; i++){
            int stan = poz[i];
            for(int j=0; j<m; j++){
                if(tab[i][j] < stan && naj[j] > tab[i][j]){
                    git = false;
                    break;
                }
            }
        }
        
        if(git) printf("Case #%d: YES\n", q+1);
        else printf("Case #%d: NO\n", q+1);
        
        for(int i=0; i<n; i++)  poz[i] = 0;
        for(int i=0; i<m; i++)  naj[i] = 0;  
    }
    
    return 0;    
}
