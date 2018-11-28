#include <iostream>
#include <cstdio>

using namespace std;

int N, M;
int lawn[120][120];

int check();

int main(void)
{
    int T;
    scanf("%d", &T);
    for(int round=1;round<=T;round++) {
        for(int i=0;i<sizeof(lawn);i++)
            ((char *)lawn)[i] = 0;
        scanf("%d %d", &N, &M);
        for(int i=1;i<=N;i++)
            for(int j=1;j<=M;j++)
                scanf("%d", &lawn[i][j]);
       
        printf("Case #%d: %s\n", round,
               check() ? "YES" : "NO");
    }
    return 0;
}

int check()
{
    for(int i=1;i<=N;i++) {
        for(int j=1;j<=M;j++) {
            if(lawn[i][j] > lawn[i][0])
                lawn[i][0] = lawn[i][j];
            if(lawn[i][j] > lawn[0][j])
                lawn[0][j] = lawn[i][j];
        }
    }
    for(int i=1;i<=N;i++) {
        for(int j=1;j<=M;j++) {
            if(lawn[i][j] < lawn[i][0] &&
               lawn[i][j] < lawn[0][j]) 
                return 0;
        }
    }
    return 1;
}
