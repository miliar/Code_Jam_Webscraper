//
//  coin_jam.cpp
//
//  Created by Lucca Siaudzionis on 09/04/16.
//
//  Google Code Jam

#include <map>
#include <cstdio>
using namespace std;
typedef long long lli;

//--------------------
int n, j;

int quantos; // quantos ja consegui

bool num[35];

lli pot[15][35];

map<lli, int> div;
//--------------------

int is_prime(lli x){
    
    if(div.count(x)) return div[x];
    
    lli i = 2;
    if(!(x % i)) return div[x] = int(i);
    
    for(i = 3;i*i <= x;i+=2)
        if(!(x % i))
            return div[x] = int(i);
    
    return div[x] = int(0);
}

void check(){
    
    if(quantos == j) return;
    
    int ans[11];
    
    for(int i = 2;i <= 10;i++){
        
        lli cur = 0LL;
        for(int j = 0;j < n;j++) if(num[j]) cur += pot[i][j];
        
        ans[i] = is_prime(cur);
        
        if(!ans[i]) return;
    }
    
    quantos++;
    for(int i = n-1;i >= 0;i--) printf("%d", num[i]);
    for(int i = 2;i <= 10;i++) printf(" %d", ans[i]);
    printf("\n");
}

void Try(int x){
    
    if(quantos == j) return;
    
    if(x == -1){
        check();
        return;
    }
    
    // boto
    num[x] = 1;
    Try(x-1);
    num[x] = 0;
    
    // nao boto
    if(x < n-1 && x > 0) Try(x-1);
    
}

int main(){
    
    int casos;
    scanf("%d", &casos);

    for(int i = 2;i <= 10;i++){
        pot[i][0] = 1LL;
        for(int j = 1;j < 35;j++) pot[i][j] = pot[i][j-1]*lli(i);
    }
    
    for(int tt = 1;tt <= casos;tt++){
        
        scanf("%d %d", &n, &j);
        
        quantos = 0;
        
        printf("Case #%d:\n", tt);
        Try(n-1);
    }
    
    return 0;
}