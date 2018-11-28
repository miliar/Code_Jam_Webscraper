#include <iostream>
#include <stdio.h>

using namespace std;

int pos(char c){
    switch(c){
        case '1': return 0;
        case 'i': return 1;
        case 'j': return 2;
        case 'k': return 3;
    }
}

void operation(char a[2], char b[2], char result[2]){
    char m[4][4][2] = {  {{'1', '+'}, {'i', '+'}, {'j','+'}, {'k','+'}},  {{'i', '+'}, {'1', '-'}, {'k','+'}, {'j','-'}},   {{'j', '+'}, {'k', '-'}, {'1','-'}, {'i','+'}},   {{'k', '+'}, {'j', '+'}, {'i','-'}, {'1','-'}}  };
    int A = pos(a[0]), B = pos(b[0]);

    result[0] = m[A][B][0];

    if (a[1] == '-' && m[A][B][1] == '+' || a[1] == '+' && m[A][B][1] == '-')
        result[1] = '-';
    else
        result[1] = '+';

}

int main(){
    int cases, i, j, k, L, X;
    char word[10005][2], result[2];

    scanf("%d ", &cases);

    for (i = 1 ; i <= cases ; i++){

        scanf("%d ", &L);
        scanf("%d ", &X);

        for (j = 0 ; j < L ; j++){
            word[j][0] = getchar();
            word[j][1] = '+';
        }
        getchar();

        for (j = 1 ; j < X ; j++)
            for (k = 0 ; k < L ; k++){
                word[L * j + k][0] = word[k][0];
                word[L * j + k][1] = '+';
            }


        /////////
//        for (j = 0 ; j < X * L ; j++)
//            cout << "j = " << j << " " << word[j][0] <<"/"<< word[j][1] << endl;
        ////////

        result[0] = '1';
        result[1] = '+';

        j = 0;
        while((result[0] != 'i' || result[1] != '+') && j < X * L){
            operation(result, word[j], result);
            j++;
        }
        if (j == X * L)
            printf("Case #%d: NO\n", i);
        else{
            result[0] = '1';
            result[1] = '+';
            while((result[0] != 'j' || result[1] != '+') && j < X * L){
                operation(result, word[j], result);
                j++;
            }

            if (j == X * L)
                printf("Case #%d: NO\n", i);
            else{
                result[0] = '1';
                result[1] = '+';
                while(j < X * L){
                    operation(result, word[j], result);
                    j++;
                }

                if (result[0] != 'k' || result[1] != '+')
                    printf("Case #%d: NO\n", i);
                else
                    printf("Case #%d: YES\n", i);
            }
        }
    }


return 0;
}
