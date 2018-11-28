#include <stdio.h>
#include <string.h>
#include <stdlib.h>

using namespace std;

bool check[9] = { false };

bool isSleep()
{
    for (int i = 0; i <= 9; i++) {
        if (check[i] == false) { return false; }
    }
    
    return true;
}

bool insert(int index)
{
    bool temp = check[index];
    check[index] = true;
    
    // when false -> true
    return temp == false ? true : false;
}

void init(){
    for(int i = 0 ;i<=9;i++) check[i] = false;
}

int main()
{
    int t = 0;
    // t = 5;
    scanf("%d",&t);
    for (int i = 0; i < t; i++) {
        
        //init
        init();
        long int n;
        n = 1;
        
        scanf("%ld",&n);
//        printf("%ld\n",n);
        if (n == 0) {
            printf("Case #%d: INSOMNIA\n", i+1);
            continue;
        } else {
            for (int j = 1;; j++) {
                char     baf[500];
                long int nj = n * j;
                sprintf(baf, "%ld", nj);
                for (long int k = 0; k < strlen(baf); k++) {
                    char c = baf[k];
                    if (insert(atoi(&c))) {
                        if (isSleep()) {
                            printf("Case #%d: %ld\n", i+1, nj);
                            goto END;
                        }
                    }
                }
            }
        END:continue;
        }
    }
    
    return 0;
}
