#include <iostream>
#include <stdio.h>
#include <list>

using namespace std;

int main()
{
    FILE *f, *g;
    /*f = fopen("input", "r");
    g = fopen("output", "w");*/
    f = stdin;
    g = stdout;

    int T, i, j;
    char c, d, first;
    list<char> word;

    fscanf(f, "%d ", &T);

    for(i = 1; i <= T; i++){
        word.clear();
        fscanf(f, " %c", &c);
        first = 'A';
        while((64 < c) && (c < 91)){
            if(c < first){
                word.push_back(c);
            }
            else{
                word.push_front(c);
                first = c;
            }
            fscanf(f, "%c", &c);
        }


        fprintf(g, "Case #%d: ", i);
        while(!word.empty()){
            c = word.front();
            fprintf(g, "%c", c);
            word.pop_front();

        }
        fprintf(g, "\n");
    }

    fclose(f);
    fclose(g);
    return 0;
}
