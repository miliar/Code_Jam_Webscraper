//
//  counting_sheep.cpp
//
//  Created by Lucca Siaudzionis on 09/04/16.
//
//  Google Code Jam

#include <cstdio>
typedef long long lli;

//-----------------
lli n;
int left;
bool mark[10];
//-----------------

void update(lli x){
    
    while(x){
        
        int r = (x % (10LL));
        x /= (10LL);
        
        if(!mark[r]) left--, mark[r] = true;
    }
    
}

int main(){
    
    int casos;
    scanf("%d", &casos);
    
    for(int tt = 1;tt <= casos;tt++){
        
        left = 10;
        for(int i = 0;i < 10;i++) mark[i] = 0;
        
        scanf("%lld", &n);
        
        printf("Case #%d: ", tt);
        
        if(!n){
            printf("INSOMNIA\n");
            continue;
        }
        
        lli num = 0LL;
        
        int ans = 0;
        while(left){
            
            ans++;
            num += n;
            update(num);
        }
        
        printf("%lld\n", num);
        
    }
    
    return 0;
}