//
//  fractiles.cpp
//
//  Created by Lucca Siaudzionis on 09/04/16.
//
//  Google Code Jam

#include <cstdio>

int main(){
    
    int casos;
    scanf("%d", &casos);
    
    for(int tt = 1;tt <= casos;tt++){
        
        int k, c, s;
        scanf("%d %d %d", &k, &c, &s);
        
        printf("Case #%d:", tt);
        
        if(s == k){
            for(int i = 1;i <= k;i++) printf(" %d", i);
            printf("\n");
            continue;
        }
        
        if(c == 1 || s < k-1){
            printf(" IMPOSSIBLE\n");
            continue;
        }
        
        for(int i = 2;i <= k;i++) printf(" %d", i);
        printf("\n");
        
    }
    
}