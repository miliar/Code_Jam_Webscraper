#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>

using namespace std;

int main(){
    int cases = 0;
    int c = 0;

    scanf("%d", &cases);

    bool solution[ 16 ];
    
    while(cases --){
        int row;
        int resp = 0;
        int count = 0;

        memset(solution, 0, sizeof(solution));
        bool flag = false;

       for(int p = 0; p < 2; p++){
            if(p == 1) flag = true;

            scanf("%d", &row);
    
            for(int i = 0; i < 4; i++){
                for(int j = 0; j < 4; j++){
                    int aux;
                    scanf("%d", &aux);
        
                    if(!flag && (i == (row - 1)) ){
                         solution[ aux - 1 ] = true;
                    }
                    if(flag && (i == (row - 1))){
                        if(solution[ aux - 1 ]){
                            resp = aux;
                            count++;
                        }
                    }
                }
            }
        }

        if(!count){
            printf("Case #%d: Volunteer cheated!\n", c + 1);
        }
        else{
             if(count > 1){
                  printf("Case #%d: Bad magician!\n", c + 1);
             }
             else{
                  printf("Case #%d: %d\n", c + 1, resp);
             }
        }
        c++;
    }
    return 0;
}
