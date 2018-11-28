#include <stdio.h>
#include <string.h>
int main(){
    int cx[4],cO[4];

    cx[0] = cx[1] =cx[2] = cx[3] = 0;
    cO[0] = cO[1] =cO[2] = cO[3] = 0;
    char ch = '0' ;
    int d = 0, rx = 0,rO = 0, di1x=0,di1O = 0, di2x = 0, di2O = 0; 
    freopen("A-large.in", "r",stdin);
    freopen("drull.out", "w", stdout);
    int T = 0, row=0, col = 0;    
    scanf("%d", &T);
    for(int i = 0;i<T;i++){
        row = col = 0;
        cx[0] = cx[1] =cx[2] = cx[3] = 0;
        cO[0] = cO[1] =cO[2] = cO[3] = 0;
        di1x  = di1O  = di2x =  di2O = 0;
        d = 0;
        while(row<4){
            col = 0;
            rx = rO = 0;
            while (col<4){
                ch = getchar();
                if(d == -1 ){                    
                    if((ch == 'X')||(ch == 'O') || (ch == '.') || (ch == 'T'))col++;
                    continue;
                 }
                 if(ch == 'X'){
                    if(col == row) di1x++;
                    if(col+row == 3) di2x++;
                    cx[col++]++; rx++;    
                 }
                 else if (ch == 'O'){
                    if(col == row) di1O++;
                    if(col+row == 3) di2O++;
                    cO[col++]++; rO++;
                 }
                 else if (ch == 'T'){
                    cO[col]++;cx[col]++;
                    if(col == row) di1x++;
                    if(col+row == 3) di2x++;
                    if(col == row) di1O++;
                    if(col+row == 3) di2O++;
                    rx++;rO++;col++;
                 }
                 else if (ch == '.'){
                    d++; col++;
                 }
            }
            row++;
            if(d == -1) continue;
            if(rx == 4){                
                printf("Case #%d: X won\n", (i+1));
                d = -1;
                //break;
            }
            if(rO == 4){
                printf("Case #%d: O won\n", (i+1));
                d = -1;
                //break;
            }
        }
        if(d == -1) continue;
        if(cx[0] == 4 || cx[1] == 4 ||cx[2] == 4 ||cx[3] == 4 || di1x == 4 || di2x == 4){
            printf("Case #%d: X won\n", (i+1));    
            continue;
        }
        if(cO[0] == 4 || cO[1] == 4 ||cO[2] == 4 ||cO[3] == 4 || di1O == 4 || di2O == 4) {
            printf("Case #%d: O won\n", (i+1));
            continue;
        }
        if(d>0)
            printf("Case #%d: Game has not completed\n", (i+1));
        else
            printf("Case #%d: Draw\n", (i+1));
    }           
    return 0;
}
