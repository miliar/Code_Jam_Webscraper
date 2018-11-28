#include <iostream>
#include <cstring>
#include <cstdio>
#include <string>
#include <cmath>
#include <vector>

#define N 20

using namespace std;

int ac[N];

int main(){
    
    int nc;
    scanf("%d", &nc);
    for(int caso = 1; caso <= nc; caso++){
        
        memset(ac, 0, sizeof(ac));
        
        int f1, f2;
        scanf("%d", &f1);
        for(int i = 1; i <= 4; i++){
            for(int j = 1; j <= 4; j++){
                int x;
                scanf("%d", &x);
                if(i == f1) ac[x]++;
            }
        }
        
        scanf("%d", &f2);
        for(int i = 1; i <= 4; i++){
            for(int j = 1; j <= 4; j++){
                int x;
                scanf("%d", &x);
                if(i == f2) ac[x]++;
            }
        }
        
        int ct2 = 0, val;
        for(int i = 1; i <= 16; i++){
            if(ac[i] == 2) ct2++, val = i;
        }
        
        if(ct2 == 0) printf("Case #%d: Volunteer cheated!\n", caso);
        else{
            if(ct2 == 1) printf("Case #%d: %d\n", caso, val);
            else printf("Case #%d: Bad magician!\n", caso);
        }
        
    }
}
