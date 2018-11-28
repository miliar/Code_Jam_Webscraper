#include <iostream>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int comp (const void * elem1, const void * elem2)
{
    int f = *((int*)elem1);
    int s = *((int*)elem2);
    if (f > s) return  1;
    if (f < s) return -1;
    return 0;
}

int lookFor(char * string, char car){

    char * copie = string;
    while(*copie != '\0'){
        if(*copie == car){
            return 1;
        }
        ++copie;
    }
    return -1;
}

int replace(char* string, char toRep, char with){

    char * copie = string;
    int count = 0;
    while(*copie != '\0'){
        if(*copie == toRep){
            string[count] = with;
            return 1;
        }
        ++count;
        ++copie;
    }
    return -1;
}

int main(void)
{

    int nbTest;

    std::cin >> nbTest;

    char C[20];
    char J[20];

    for(int i = 0; i < nbTest; ++ i){
        char * input = new char[2001];

        std::cin >> input;

        input[2000]='\0';

        int nb[667];
        int count = 0;


        while(lookFor(input,'Z') == 1){
            nb[count] = 0;
            ++count;
            replace(input, 'Z','K');
            replace(input, 'E','K');
            replace(input, 'R','K');
            replace(input, 'O','K');
        }
        while(lookFor(input,'W') == 1){
            nb[count] = 2;
            ++count;
            replace(input, 'T','K');
            replace(input, 'W','K');
            replace(input, 'O','K');
        }
        while(lookFor(input,'X')==1){
            nb[count] = 6;
            ++count;
            replace(input, 'S','K');
            replace(input, 'I', 'K');
            replace(input, 'X', 'K');
        }
        while(lookFor(input,'G')==1){
            nb[count] = 8;
            ++count;
            replace(input, 'E','K');
            replace(input, 'I', 'K');
            replace(input, 'G', 'K');
            replace(input, 'H', 'K');
            replace(input, 'T', 'K');
        }

        while(lookFor(input,'T')==1){
            nb[count] = 3;
            ++count;
            replace(input, 'T','K');
            replace(input, 'H', 'K');
            replace(input, 'R', 'K');
            replace(input, 'E', 'K');
            replace(input, 'E', 'K');
        }

        while(lookFor(input,'S')==1){
            nb[count] = 7;
            ++count;
            replace(input, 'S','K');
            replace(input, 'E', 'K');
            replace(input, 'V', 'K');
            replace(input, 'E', 'K');
            replace(input, 'N', 'K');
        }
        while(lookFor(input,'V')==1){
            nb[count] = 5;
            ++count;
            replace(input, 'F','K');
            replace(input, 'I', 'K');
            replace(input, 'V', 'K');
            replace(input, 'E', 'K');
        }
        while(lookFor(input,'F')==1){
            nb[count] = 4;
            ++count;
            replace(input, 'F','K');
            replace(input, 'O', 'K');
            replace(input, 'U', 'K');
            replace(input, 'R', 'K');
        }
        while(lookFor(input,'O')==1){
            nb[count] = 1;
            ++count;
            replace(input, 'O','K');
            replace(input, 'N', 'K');
            replace(input, 'E', 'K');
        }

        while(lookFor(input,'N')==1){
            nb[count] = 9;
            ++count;
            replace(input, 'N','K');
            replace(input, 'I', 'K');
            replace(input, 'N', 'K');
            replace(input, 'E', 'K');
        }

        qsort(nb, count,sizeof(int), comp);

        std::cout << "Case #" << 1+i << ": ";

        for(int i = 0; i< count; ++i){
            printf("%d",nb[i]);
        }


        std::cout <<std::endl;

    }


    return 0;
}

