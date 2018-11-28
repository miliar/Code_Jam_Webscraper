#include "stdlib.h"
#include "stdio.h"

using namespace std;

int next(){
    int r=0;
    char* s = new char[200];


    scanf("%s\n", s);

    // printf("%s\n", s);

    int i=1;
    while(s[i] == '+' || s[i]=='-'){
        if(s[i] != s[i-1])
            r++;
        i++;
    }
    if(s[i-1] == '-')
        r++;

    return r;
}


int main(){
    int n;
    scanf("%d", &n);
    for(int i=1;i<=n;i++)
        printf("Case #%d: %d\n", i, next());

    return 0;
}
