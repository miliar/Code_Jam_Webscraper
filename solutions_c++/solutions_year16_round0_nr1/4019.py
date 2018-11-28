#include <cstdio>
#include <cstdlib>

FILE * fin = fopen ("A-large.in", "r");
FILE * fout = fopen ("A.out", "w");

void work (int r){
     fprintf (fout, "Case #%d: ", r);
     int N;
     fscanf (fin, "%d", &N);
     if (N == 0){
           fprintf (fout, "INSOMNIA\n");
           return;
     }
     int count[10];
     for (int i = 0; i < 10; i ++)
         count[i] = 0;
     int tmp = N;
     while(true){
         int q = tmp;
         while (q > 0){
               int r = q % 10;
               count[r] ++;
               q = q / 10;
         }       
         int tag = 1;
         for (int i = 0; i < 10; i ++) tag *= count[i];
         if (tag != 0){
                 fprintf (fout, "%d\n", tmp);
                 break;
         }
         tmp += N;
     }
     return;
}

int main (){
    int T;
    fscanf (fin, "%d", &T);
    for (int i = 0; i < T; i ++){
        work (i + 1);
    }
    return 0;
}