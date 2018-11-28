#include <cstdio>
#include <cstdlib>

FILE * fin = fopen ("D-small-attempt0.in", "r");
FILE * fout = fopen ("d.out", "w");

void work(int r){
     fprintf (fout, "Case #%d: ", r);
     int K, C, S;
     fscanf (fin, "%d%d%d", &K, &C, &S);
     for (int i = 0; i < K; i ++)
         fprintf (fout, "%d ", i + 1);
     fprintf (fout, "\n");
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