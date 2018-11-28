#include<iostream>
#include <cstdio>
#include <cstring>
using namespace std;

int main(){
    int test, i;
    char s[500];

    cin >>test;
    for(int j=1;j<=test;j++){
        int c=0;
        cin >> s;

        for(i=0;i<strlen(s);i++){
            if( (s[i] == '-' && s[i+1] == '+') || (s[i] == '+' && s[i+1] == '-'))
                c++;
        }
        if(s[i-1] == '-')
            c++;

        printf("Case #%d: %d\n", j, c);
    }
}
