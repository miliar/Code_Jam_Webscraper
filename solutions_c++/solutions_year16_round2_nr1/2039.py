#include <cstdio>
#include <cstring>

int t;
char s[2003];
int l[26], n[10];
char ini[] = {'Z', 'W', 'G', 'X', 'S', 'V', 'I', 'H', 'N', 'F'};
char let[][6] = {"ZERO", "TWO", "EIGHT", "SIX", "SEVEN", "FIVE", "NINE", "THREE", "ONE", "FOUR"};
int num[] = {0, 2, 8, 6, 7, 5, 9, 3, 1, 4};

int main(){
    scanf("%d", &t);
    for(int i=1; i<=t; i++){
        scanf("%s", s);
        
        memset(l, 0, sizeof(l));
        memset(n, 0, sizeof(n));
        for(int j=0; s[j]; j++) l[s[j]-'A']++;
        
        for(int j=0; j<10; j++){
            if(l[ini[j]-'A']){
                n[num[j]] = l[ini[j]-'A'];
                for(int k=0; let[j][k]; k++) l[let[j][k]-'A'] -= n[num[j]];
            }
        }
        
        printf("Case #%d: ", i);
        for(int j=0; j<10; j++){
            for(int k=0; k<n[j]; k++)
                printf("%d", j);
        }
        printf("\n");
    }
    
    return 0;
}