#include <cstdio>
#include <algorithm>
using namespace std;
FILE *in = fopen("D-large.in","r");
FILE *out = fopen("saida.txt","w");

const int MAXN = 1010;
double A[MAXN], B[MAXN];

int main() {
    int T, N;
    fscanf(in,"%d",&T);
    for (int t=1; t<=T; t++) {
        fprintf(out,"Case #%d: ",t);
        fscanf(in,"%d",&N);
        for (int i=1; i<=N; i++) fscanf(in,"%lf",&A[i]);
        for (int i=1; i<=N; i++) fscanf(in,"%lf",&B[i]);
        sort(A+1,A+N+1);
        sort(B+1,B+N+1);
        int posB, ini=1, fim=N, x=0, y=N, pos=1;
        for (int i=1; i<=N; i++) {
            if (A[i] < B[ini]) fim--;
            else {
                ini++;
                x++;
            }
        }
        ini=1;
        for (; pos<=N; pos++) {
            while (ini <=N && A[pos] > B[ini]) ini++;
            if (ini > N) break;
            ini++;
            y--;
        }
        fprintf(out,"%d %d\n",x,y);
    }
    return 0;
}
