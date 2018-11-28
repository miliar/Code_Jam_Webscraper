#include<cstdio>
#include <cstdlib>
#include <iostream>
#include <fstream>
using namespace std;

FILE * fin = fopen ("B-large.in", "r");
FILE * fout = fopen ("B.out", "w");

void work (int r){
     fprintf (fout, "Case #%d: ", r);
     char S[100];
     fscanf (fin, "%s", &S);
     int s[100];
     int count = 0;
     int len = 0;
     while (S[len] != 0){
           printf ("%c", S[len]);
           s[len] = (S[len] == '-' ? 0 : 1);
           len ++;
     }
     while (true){
           int tag = 0;
           for (int i = 0; i < len; i ++) tag += s[i];
           if (tag == 0){
                   count ++;
                   break;
           }
           if (tag == len) break;
           if (s[0] == 0){
                for (int tmp = len - 1; tmp > 0; tmp --){
                    if (s[tmp] == 1 && s[tmp - 1] == 0){
                       int sta[100];
                       for (int i = 0; i < tmp; i ++){
                           sta[i] = 1 - s[tmp - i - 1];
                       }
                       for (int i = 0; i < tmp; i ++)
                           s[i] = sta[i];
                       count ++;
                       break;
                    }
                }
           }
           else{
                for (int tmp = len - 1; tmp > 0; tmp --){
                    if (s[tmp] == 0 && s[tmp - 1] == 1){
                       int sta[100];
                       for (int i = 0; i < tmp; i ++){
                           sta[i] = 1 - s[tmp - i - 1];
                       }
                       for (int i = 0; i < tmp; i ++)
                           s[i] = sta[i];
                       count ++;
                       break;
                    }
                }
           }
     }
     fprintf (fout, "%d\n", count);
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