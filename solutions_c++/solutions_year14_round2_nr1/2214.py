#include<stdio.h>
#include<string>
#include<math.h>
#include<stdlib.h>
#include<set>
#include<bitset>
#include<map>
#include<vector>
#include<string.h>
#include<algorithm>
#include<iostream>
#include<list>
#define RI(X) scanf("%d", &(X))
#define RII(X, Y) scanf("%d%d", &(X), &(Y))
#define RIII(X, Y, Z) scanf("%d%d%d", &(X), &(Y), &(Z))
#define DRI(X) int (X); scanf("%d", &X)
#define DRII(X, Y) int X, Y; scanf("%d%d", &X, &Y)
#define DRIII(X, Y, Z) int X, Y, Z; scanf("%d%d%d", &X, &Y, &Z)
#define RS(X) scanf("%s", (X))
#define CASET int ___T, case_n = 1; scanf("%d ", &___T); while (___T-- > 0)
using namespace std;

#define SIZE 105

char str[SIZE];
char cnt[SIZE][SIZE];
int N;

int run()
{
    int M = strlen(str);
    /*printf("%s\n", str);
    for(int i=0; i<N; i++){
        printf("[%d] ", i);
        for(int j=0; j<M; j++)printf("%d ", cnt[i][j]);
        printf("\n");
    }*/
    
    int c = 0;
    for(int i=0; i<M; i++){
        int cc = 0;
        for(int j=0; j<N; j++){
            cc += cnt[j][i];
        }
        if( (cc % N)*2 > N ) cc = cc / N + 1;
        else cc = cc / N;
        //printf("> %d %d\n", i, cc);
        for(int j=0; j<N; j++){
            c += abs(cc - cnt[j][i]);
        }
    }
    return c;
}

int main()
{
    CASET {
        RI(N);
        char s[SIZE];
        char ns[SIZE];
        gets(s);
        
        memset(str, 0, sizeof(str));
        memset(cnt, 0, sizeof(cnt));
        bool ok = true;
        for(int i = 0; i<N; i++){
            char o = 0;
            gets(s);
            
            int j = 0;
            int k = -1;
            while(s[j]){
                if(s[j] == o)
                    cnt[i][k]++;
                else {
                    k++;
                    o = s[j];
                    ns[k] = o;
                }
                j++;
            }
            ns[++k]=0;
            if(i == 0)
                strcpy(str, ns);
            else if(strcmp(ns, str) != 0){
                //printf("%s %s\n", str, ns);
                ok = false;
            }
        }
        printf("Case #%d: ", case_n++);
        if(!ok)
            printf("Fegla Won\n");
        else
            printf("%d\n", run());
    }
    return 0;
}

