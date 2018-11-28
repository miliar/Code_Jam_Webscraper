#include <iostream>
#include <vector>
#include <string>
#include <stdio.h>
#include <cmath>
#include <algorithm>
#include <utility>
#include <cstring>
#include <queue>

using namespace std;

#define INF 1<<30

int lawn[110][110];

int main()
{
    int casenum = 1;
    int TC;
    int N,M;
    scanf("%d\n",&TC);
    while(TC--){
        
        scanf("%d %d\n",&N,&M);
        bool found = false;
        for(int i = 0; i < N; i++){
            for(int j = 0; j < M; j++){
                scanf("%d",&lawn[i][j]);
            }
        }
        for(int i = 0; i < N; i++){
            for(int j = 0; j < M; j++){
                
                bool f = true;
                for(int k = 0; k < N; k++){
                    if(lawn[k][j] > lawn[i][j]){
                        f = false;
                    }
                }
                bool f2 = true;
                for(int k = 0; k < M; k++){
                    if(lawn[i][k] > lawn[i][j]){
                        f2 = false;
                    }
                }
                if(!(f2 | f)){
                    found = true;   
                }
            }
        }
        if(found) printf("Case #%d: NO\n",casenum++);
        else{
            printf("Case #%d: YES\n",casenum++);   
        }
    }
    return 0;
}
