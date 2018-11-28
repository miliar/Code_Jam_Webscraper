#include <cstdio>
#include <cstring>

int t;
char s[101];

int main(){
    scanf("%d", &t);
    
    for(int tc=1; tc<=t; tc++){
        scanf("%s", s);
        
        int c=1;
        char a=s[0];
        for(int i=1; s[i]; i++)
        if(s[i]!=a){
            a=s[i];
            c++;
        }
        if(a=='+') c--;
        
        printf("Case #%d: %d\n", tc, c);
    }
    
    return 0;
}