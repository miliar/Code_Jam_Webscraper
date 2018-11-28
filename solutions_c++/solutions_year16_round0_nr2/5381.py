/** CyCraig33 - Google Code Jam 2016 Qualification Problem B **/
#include <cstdio>
#include <cstring>


char s[100];
bool pancakes[100];

void printPancakes() {
    int len = strlen(s);
    for(int i = 0; i < len; i++) {
        printf("%c",pancakes[i]?'+':'-');
    }
    printf("\n");
}

bool pancakesUp(int len) {
    int up = 0;
    for(int i = 0; i < len; i++) {
        up += pancakes[i];
    }
    return (up==len);
}

int main(void) {
    freopen("B-large.in", "r", stdin);
    freopen("outlarge", "w", stdout);
    
    int n,c = 0;
    scanf("%d",&n);
    while(n-- > 0) {
        memset(pancakes,0,sizeof(pancakes));
        scanf("%s",&s);
        int len = strlen(s);
        for(int i = 0; i < len; i++) {
            pancakes[i] = (s[i] == '+');
        }

        int numFlips = 0;
        bool allUp = false;
        
        if( len == 1 ) {
            numFlips = !pancakes[0];
        }
        else {
            while( !allUp ) {
                //printPancakes();
                int numUp = 0;
                int pos = 0;
                while( pancakes[pos] == pancakes[pos+1] && pos < len ) {
                    pos++;
                }
                if( pancakesUp(len)) {
                    allUp = true;
                }
                else {
                    numFlips++;
                    
                    // flip until pos
                    for(int i = 0; i <= pos; i++) pancakes[i] = !pancakes[i];
                }
            }
        }
        printf("Case #%d: %d\n",++c,numFlips);
    }
    fflush(stdout);
    
    
    return 0;
}