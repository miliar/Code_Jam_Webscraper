#include <iostream>
#include <stdio.h>
#include <string.h>
#include <cmath>

#define STR_CNT 105
#define STR_LEN 105
using namespace std;

char A[STR_CNT][STR_LEN];
int C[STR_CNT][STR_LEN];
char L[STR_LEN];
int N;

int main()
{
    int t;
    scanf("%d", &t);
    for(int k=1; k<=t; k++){
        scanf("%d", &N);
        for(int i=0; i<N; i++){
            scanf("%s", A[i]);
        }

        for(int i=0; i<STR_CNT; i++) {
            L[i] = 0;
            for(int j=0; j<STR_LEN; j++) {
                C[i][j] = 0;
            }
        }
        
        int diffLetters = 0;
        int l = strlen(A[0]), d = 1;
        char currL = A[0][0];

        for(int i=1; i<l; i++) {
            if( currL != A[0][i] ) {
                C[0][diffLetters] = d;
                d = 0;
                L[diffLetters++] = currL;
                currL = A[0][i];
            }
            d++;
        }
        C[0][diffLetters] = d;
        L[diffLetters++] = currL;
        
        /*for(int i=0; i<diffLetters; i++) {
            printf("%c", L[i]);
        }
        printf("\n");*/
        
        bool sameLetters = true;
        for(int i=1; i<N; i++){
            l = strlen(A[i]);
            int c = 0, d = 1; 
            
            char currL = A[i][0];
            for(int j=1; j<l; j++) {
                if( currL != A[i][j] ){
                    if( L[c] != currL ) {
                        sameLetters = false;
                        break;
                    }
                    
                    C[i][c] = d;
                    d = 0;
                    c++;

                    currL = A[i][j];
                }
                d++;
            }
            if( L[c] != currL )
                sameLetters = false;

            C[i][c] = d;
            c++;
            
            if( c != diffLetters )
                sameLetters = false;

            if( !sameLetters )
                break;
        }

        /*
        for(int i=0; i<N; i++) {
            for(int j=0; j<diffLetters; j++)
                printf("%d ", C[i][j]);
            printf("\n");
        }
        */

        if( !sameLetters ) {
            printf("Case #%d: Fegla Won\n", k);
            continue;
        }

        int cnt = 0;
        for(int i=0; i<diffLetters; i++) {
            int sum = 0;
            for(int j=0; j<N; j++) {
                sum += C[j][i];
            }

            int av = round( ((double)sum) / ((double)N) );
            for(int j=0; j<N; j++) {
                cnt += abs(av - C[j][i]);
            }
        }

        printf("Case #%d: %d\n", k, cnt);
    }

    return 0;
}
