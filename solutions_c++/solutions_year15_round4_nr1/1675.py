//In the name of Allah

#include <iostream>
#include <vector>
#include <string>
#include <stack>
#include <algorithm>
#include <bitset>
#include <math.h>
#include <queue>
#include <map>
#include <set>
#include <limits.h>
#include <limits>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <sstream>
#include <assert.h>
using namespace std;

int T, R, C, caseN;
char s[105][105];

int Li[105], Ri[105], Ui[105], Di[105];

int main(){
    scanf("%d", &T);
    while(T--){
        scanf("%d %d", &R, &C);
        
        for(int i = 0; i < R; i++)
            Li[i] = C, Ri[i] = -1;
        for(int j = 0; j < C; j++)
            Ui[j] = R, Di[j] = -1;
        
        for(int i = 0; i < R; i++){
            scanf("%s", s[i]);
            for(int j = 0; j < C; j++)if(s[i][j] != '.'){
                Li[i] = min(Li[i], j);
                Ri[i] = max(Ri[i], j);
                Ui[j] = min(Ui[j], i);
                Di[j] = max(Di[j], i);
            }
        }
        
        int res = 0;
        bool ok = true;
        
        for(int i = 0; i < R; i++)
        for(int j = 0; j < C; j++){
            if(s[i][j] != '.'){
                bool found1, found2, found3, found4;
                
                if(Ri[i] > j)found1 = true;
                else found1 = false;

                if(Li[i] < j)found2 = true;
                else found2 = false;

                if(Di[i] > i)found3 = true;
                else found3 = false;

                if(Ui[i] < i)found4 = true;
                else found4 = false;
                
                if(!(found1 || found2 || found3 || found4))ok = false;
                else{
                    if((s[i][j] == '>') && !found1)res++;
                    if((s[i][j] == '<') && !found2)res++;
                    if((s[i][j] == 'v') && !found3)res++;
                    if((s[i][j] == '^') && !found4)res++;
                }
            }
        }
        
        if(!ok)printf("Case #%d: IMPOSSIBLE\n", ++caseN);
        else printf("Case #%d: %d\n", ++caseN, res);
    }
    return 0;
}