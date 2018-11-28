#include <stdio.h>

int main(){
    int TC, Smax;
    scanf("%d", &TC);
    for(int c = 1; c <= TC; c++){
        printf("Case #%d: ", c);
        scanf("%d", &Smax);
        char arr[Smax + 1];
        scanf("%s", &arr[0]);

        // Datos leidos, procesamos
        int friends = 0, people = 0;
        for(int i = 0; i <= Smax; i++){
            if(people + friends < i) friends += i - (people + friends);
            people += (int)arr[i] - '0';
        }
        printf("%d\n", friends);
    }
}
