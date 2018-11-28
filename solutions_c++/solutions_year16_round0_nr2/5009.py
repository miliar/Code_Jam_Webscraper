#include <stdio.h>

int main(){
    int t, bl, len;
    char in[5000];

    scanf ("%d", &t);

    for (int k=1; k<=t; k++){
        printf ("Case #%d: ", k);

        scanf ("%s", in);

        bl = 1;
        for (len=1; in[len]!=0; len++)
            if (in[len] != in[len-1]) bl++;

        if (in[len-1] == '+') bl--;

        printf ("%d\n", bl);
    }

    return 0;
}
