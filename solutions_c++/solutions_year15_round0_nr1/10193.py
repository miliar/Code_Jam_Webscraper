#include <iostream>
#include <stdio.h>
#include <stdlib.h>
using namespace std;

int resolve(char str[], char max){
    printf("\nStart resolve(%c %s)\n", max, str);
    int count = 0,n[255];
    int sMax = max - '0';
    for(count = 0;str[count] != '\0';count++)
        n[count] = str[count] - '0';
    //Inizio
    printf("Start resolving...");
    int sI = 0, people = 0;
    int toAdd = 0;
    for(int i = 0;i < count;i++){
        if(people < i){
            toAdd += i - people;
            people += (i - people);
        }
        people += n[i];
    }
    printf("solved!\nUpPeople:%d toAdd:%d", people, toAdd);
    //Fine
    return toAdd;
}

int main()
{
    FILE *input = fopen("input.txt", "r");
    FILE *output = fopen("output.txt", "w");
    int nCase;
    fscanf(input, "%d\n", &nCase);
    for(int i = 0;i < nCase;i++){
        char str[255], max, space;
        fscanf(input, "%c%c%s\n", &max, &space, &str);
        fprintf(output, "Case #%d: %d\n", i + 1, resolve(str, max));
    }
    fclose(input);
    fclose(output);
    return 0;
}
