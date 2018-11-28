#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cassert>
#include <climits>
#include <ctime>
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <algorithm>
#include <vector>
#include <deque>
#include <list>
#include <queue>
#include <set>
#include <map>
#include <limits>
#include <cstring>

using namespace std;

int main() {
    int nCases;
    scanf("%d", &nCases);

    int tab[10][10];
    int v[10][10];
    int tabM[10];

    for (int iCase = 1; iCase <= nCases; iCase++) {
        int M, N;
        int res=0;
        int minBord=2;
        scanf("%d%d", &N, &M);
        for (int n = 0; n < N; n++) {
          for (int m = 0; m < M; m++) {
              scanf("%d",&(tab[n][m]));
              //printf("%d ",(tab[n][m]));
          }
         // printf("\n");
        }
        

        for (int m = 0; m < M; m++) {
          for (int n = 0; n < N; n++) {
                 v[n][m]=0;
          }
        }
        

        for (int n = 0; n < N; n++) {
          for (int hauteur = 1; hauteur <=2; hauteur++) {
            int tmp=0;
            for (int m = 0; m < M; m++) {
              if (hauteur == 2) {
                 if (tab[n][m] == hauteur) {
                   v[n][m] = 3;
                 }
              } else {
                 if (tab[n][m] == 2) {
                   tmp = 1;
                 }
              }
            }
            if (hauteur == 1 && tmp == 0) {
               for (int m = 0; m < M; m++) {
                 v[n][m]=3;
               }
            }
          }
        }


        for (int m = 0; m < M; m++) {
          for (int hauteur = 1; hauteur <=2; hauteur++) {
            int tmp =0;
            for (int n = 0; n < N; n++) {
               if (hauteur == 2) {
                 if (tab[n][m] == hauteur) {
                   v[n][m] = 3;
                 }
               } else {
                 if (tab[n][m] == 2) {
                   tmp = 1;
                 }
               }
            }
            if (hauteur == 1 && tmp == 0) {
               for (int n = 0; n < N; n++) {
                 v[n][m]=3;
               }
            }
          }
        }
        
        for (int n = N-1; n >= 0; n--) {
          for (int hauteur = 1; hauteur <=2; hauteur++) {         

            int tmp=0;
            for (int m = M-1; m >=0; m--) {
              if (hauteur == 2) {
                 if (tab[n][m] == hauteur) {
                   v[n][m] = 3;
                 }
              } else {
                 if (tab[n][m] == 2) {
                   tmp = 1;
                 }
              }
            }
            if (hauteur == 1 && tmp == 0) {
               for (int m = 0; m < M; m++) {
                 v[n][m]=3;
               }
            }
          }
        } 


        for (int m = M-1; m >=0; m--) {
          for (int hauteur = 1; hauteur <=2; hauteur++) {
            int tmp =0;
            for (int n = N-1; n >=0; n--) {
               if (hauteur == 2) {
                 if (tab[n][m] == hauteur) {
                   v[n][m] = 3;
                 }
               } else {
                 if (tab[n][m] == 2) {
                   tmp = 1;
                 }
               }
            }
            if (hauteur == 1 && tmp == 0) {
               for (int n = 0; n < N; n++) {
                 v[n][m]=3;
               }
            }
          }
        }



//printf("\n");

        for (int m = 0; m < M; m++) {
          for (int n = 0; n < N; n++) {
             if (v[n][m] != 3) {
                //printf("%d ",v[n][m]);
                res=1;
             } else {
                //printf("%d ",v[n][m]);
             }
          }
          //printf("\n");
        }

//printf("\n");
        for (int m = 0; m < M; m++) {
          for (int n = 0; n < N; n++) {
                //printf("%d ",tab[n][m]);
          }
          //printf("\n");
        }
        

       if (res == 1) {
         printf("Case #%d: NO\n",iCase);
       } else {
         printf("Case #%d: YES\n",iCase);
       }
    }

    return 0;
}

