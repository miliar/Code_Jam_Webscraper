#include <cstdlib>
#include <iostream>

using namespace std;

int main(int argc, char *argv[])
{
    int num_case;
    int X[100][100];
    
    scanf("%d", &num_case);
    for(int i=0;i<num_case;i++){
        int n,m;
        scanf("%d %d", &n, &m);
        
        for(int y=0;y<n;y++){
           for(int x=0;x<m;x++){                                   
               scanf("%d", &(X[y][x]));
           }
        }
        
        bool ok = true;
        for(int y=0;y<n && ok;y++){

           for(int x=0;x<m && ok;x++){                                   

               bool h_ok = true;
               for(int x1=0;x1<m && h_ok;x1++){                                   
                   if(X[y][x1] > X[y][x] && x != x1)
                       h_ok = false;
               }
                                      
               bool v_ok = true;
               for(int y1=0;y1<n && v_ok;y1++){                                   
                   if(X[y1][x] > X[y][x] && y != y1)
                       v_ok = false;
               }
               
               ok = h_ok || v_ok;
               //printf("%d %d %d\n", h_ok, v_ok, ok);
                   
           }
           
        }
        
        printf("Case #%d: %s\n", i+1, !ok?"NO":"YES");
                       
    }
}


