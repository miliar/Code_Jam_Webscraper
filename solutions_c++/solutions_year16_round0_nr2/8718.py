#include<iostream>
#include<cstdlib>
#include<cstdio>
#include<map>

using namespace std;

int flip(char *s) {
    int f=0;
    int lp=s[0];

    if(s[0]=='-' && s[1]=='\0')
        return 1;

    int i=0;
    for(i=1;s[i]!='\0';i++) {
        if(s[i]!=lp) {
            f++;
            lp=s[i];
        }
    }
    if(s[i-1]=='-')
        f++;

    return f;
}

int main() {
    int t;
    char s[101];
    scanf("%d",&t);
    for(int i=1;i<=t;i++) {
        scanf("%s",&s);
        printf("Case #%d: ",i);
        printf("%d\n",flip(s));
    }
}
