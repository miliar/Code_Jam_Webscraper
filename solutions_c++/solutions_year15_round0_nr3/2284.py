#include <cstdio>
#include <cstdlib>

long long int T, L, X;
int A[200000];
char c;
int map[5][5]={{0, 0, 0, 0, 0}, {0, 1, 2, 3, 4}, {0, 2, -1, 4, -3}, {0, 3, -4, -1, 2}, {0, 4, 3, -2, -1}};

int Multiply(int a, int b){
    int Neg;
    if(a*b < 0)
        Neg = -1;
    else
        Neg = 1;
    return Neg * map[abs(a)][abs(b)];
}

int main(){
    freopen("/Users/Apple/Desktop/Programming/Codes/Dijkstra/Dijkstra/C-large.in", "r", stdin);
    freopen("/Users/Apple/Desktop/Programming/Codes/Dijkstra/Dijkstra/out.txt", "w", stdout);
    scanf("%lld", &T);
    for(long long int i=0; i<T; i++){
        long long int finding = 2, Start = 1, can = 1;
        scanf("%lld %lld", &L, &X);
        if(X > 12)
            X = X % 4 + 12;
        A[0] = 1;
        for(long long int j=1; j<=L; j++){
            scanf(" %c", &c);
            for(long long int k=0; k<X; k++)
                A[j+L*k] = c - 'a' - 6;
        }
        for(long long int j=1; j<=L*X; j++){
            if(j==Start-1+4*L){
                can = 0;
                break;
            }
            A[j] = Multiply(A[j-1], A[j]);
            if(A[j]==finding){
                A[j] = 1;
                finding++;
                Start = j+1;
            }
            if(finding==5){
                Start = j+1;
                break;
            }
        }
        if(can && finding==5){
            for(long long int j=Start+1; j<=L*X; j++)
                A[j] = Multiply(A[j-1], A[j]);
            if(A[L*X]!=1) can = 0;
        }
        else can = 0;
        if(can)
            printf("Case #%lld: YES\n", i+1);
        else
            printf("Case #%lld: NO\n", i+1);
    }
    return 0;
}
