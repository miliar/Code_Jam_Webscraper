#include <stdio.h>
#include <string.h>
#include <iostream>

int main(int argc, char const *argv[])
{
    int t, n, i, j;
    scanf("%d", &t);
    long long int count, no_of_people;
    char s[1002];
    for (j=1; j<=t; j++){
        count = no_of_people = 0;
        scanf("%d", &n);
        std::cin >> s;
        for (i=0; i<=n ; i++){
            if (s[i] == '0'){
                if (!count){
                    no_of_people ++;
                }else{
                    count--;
                }
            }else{
                count += s[i] - '0' - 1;
            }
        }
        printf("Case #%d: %llu\n", j, no_of_people);
    }
    return 0;
}