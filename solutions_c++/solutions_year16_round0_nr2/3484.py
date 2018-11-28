//
//  revenge2.cpp
//
//  Created by Lucca Siaudzionis on 09/04/16.
//
//  Google Code Jam

#include <cstdio>
#include <vector>
#include <cstring>
#include <algorithm>
using namespace std;

//---------------------
int n;
int seq[105];

char s[105];
//---------------------

void inverte(int k){
    
    int aux[105];
    for(int i = 0;i < n;i++) aux[i] = seq[i];
    
    for(int i = 0;i <= k;i++) aux[i] = (seq[k-i] xor 1);
    for(int i = 0;i < n;i++) seq[i] = aux[i];
}

int main(){
    
    int casos;
    scanf("%d", &casos);
    
    for(int tt = 1;tt <= casos;tt++){
        
        scanf("%s", s);
        
        n = strlen(s);
        for(int i = 0;i < n;i++) seq[i] = (s[i]=='+')?0:1;
        
        int op = 0;
        while(n){
            
            while(n && !seq[n-1]) n--;
            if(!n) break;
            
            seq[n] = 1;
            
            op++;
            if(seq[0]) inverte(n-1);
            else{
                int k = 0;
                while(!seq[k]) k++;
                inverte(k-1);
            }
            
        }
        
        printf("Case #%d: %d\n", tt, op);
    }
    
    return 0;
}