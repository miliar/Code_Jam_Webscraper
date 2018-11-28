#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <cstdlib>
#include <queue>

using namespace std; 

#define MAXN 510

#define BOMBA 3
#define NUM   2
#define VAZIO 0

typedef pair<int,int> ii;

int vis[MAXN][MAXN];
int aux[MAXN][MAXN];
int mapa[MAXN][MAXN];
int dl[] = {-1,-1,-1,0,0,1,1,1};
int dc[] = {-1,0,1,-1,1,-1,0,1};

int n,m,nbomb;
ii start;

void imprime(){
    for(int i = 0 ; i < n ; i++){
        for(int j = 0 ; j < m ; j++){
            if(i == start.first && j == start.second) printf("c");
            else if(mapa[i][j] == BOMBA) printf("*"); 
            else printf(".");
        }
        printf("\n");
    }    
}

bool teste(){   
    
    for(int i = 0 ; i < n ; i++)
        for(int j = 0 ; j < m ; j++){
            vis[i][j] = 0;
            if(mapa[i][j] == BOMBA){
                for(int k = 0 ; k < 8 ; k++){           
                    int pl = i + dl[k];
                    int pc = j + dc[k];
                    if(pl < 0 || pl >= n) continue;
                    if(pc < 0 || pc >= m) continue;
                    if(mapa[pl][pc] == BOMBA) continue;
                    mapa[pl][pc] = NUM;
                }
            }
        }
    //~ imprime();
    for(int i = 0 ; i < n ; i++)
        for(int j = 0 ; j < m ; j++){
            if(mapa[i][j] == VAZIO){
                start = ii(i,j);
                queue<ii> q;
                q.push(start);
                vis[i][j] = true;
                while(!q.empty()){
                    ii v = q.front();
                    q.pop();
                    for(int k = 0 ; k < 8 ; k++){
                        int pl = v.first + dl[k];
                        int pc = v.second + dc[k];
                        if(pl < 0 || pl >= n) continue;
                        if(pc < 0 || pc >= m) continue;
                        if(vis[pl][pc]) continue;
                        vis[pl][pc] = true;
                        if(mapa[pl][pc] == VAZIO){              
                            q.push(ii(pl,pc));                            
                        }                        
                    }                    
                }
                for(int a = 0; a < n ; a++)
                    for(int b = 0 ; b < m ; b++){
                        if(mapa[a][b] == VAZIO && !vis[a][b]) return false;
                        if(mapa[a][b] == NUM && !vis[a][b]) return false;
                    }
                return true;
            }               
        }
    
    return false;
}

bool solve(){
    int faltam = n*m - nbomb;
    if(nbomb == 0){
        printf("c");
        for(int j = 1 ; j < m ; j++) printf(".");
        printf("\n");
        for(int i = 1 ; i < n ; i++){
            for(int j = 0 ; j < m ; j++) printf(".");
            printf("\n");
        }            
        return true;
    }
    if(faltam == 1){
        printf("c");
        for(int j = 1 ; j < m ; j++) printf("*");
        printf("\n");
        for(int i = 1 ; i < n ; i++){
            for(int j = 0 ; j < m ; j++) printf("*");
            printf("\n");
        }            
        return true;
    }
    if((n > 1) && (m > 1) && faltam < 4) return false;
    for(int mask = 0 ; mask < (1 << n*m) ; mask++){
        if(__builtin_popcount(mask) == nbomb){
            //~ printf("<< %d >>\n",mask);
            for(int i = 0 ; i < n ; i++)
                for(int j = 0 ; j < m ; j++){
                    if(mask & 1 << (i*m + j)){
                        mapa[i][j] = BOMBA;
                    }                    
                    else mapa[i][j] = VAZIO;
                }
            if(teste()){
                imprime();
                return true;
            }
        }       
    }    
    return false;
}

int main(){
    int nt;
    scanf(" %d",&nt);
    for(int t = 1 ; t <= nt ; t++){
        scanf(" %d %d %d",&n,&m,&nbomb);        
        printf("Case #%d:\n",t); 
        if(!solve()) printf("Impossible\n");        
    }
    return 0;
}
