#include <cstdio>
#include <algorithm>
using namespace std;
FILE *in = fopen("A-small-attempt0.in","r");
FILE *out = fopen("saida.txt","w");

int m[2][5][5];

int main() {
    int T, a, b;
    fscanf(in,"%d",&T);
    for (int t=1; t<=T; t++) {
        fprintf(out,"Case #%d: ",t);
        fscanf(in,"%d",&a);
        for (int i=1; i<=4; i++) {
            for (int k=1; k<=4; k++) {
                fscanf(in,"%d",&m[0][i][k]);
            }
        }
        fscanf(in,"%d",&b);
        for (int i=1; i<=4; i++) {
            for (int k=1; k<=4; k++) {
                fscanf(in,"%d",&m[1][i][k]);
            }
        }
        int cont = 0, resp;
        for (int i=1; i<=4; i++) {
            for (int k=1; k<=4; k++) {
                if (m[0][a][i] == m[1][b][k]) {
                    cont++;
                    resp = m[0][a][i];
                }
            }
        }
        if (cont == 1) fprintf(out,"%d\n",resp);
        else if (cont > 1) fprintf(out,"Bad magician!\n");
        else fprintf(out,"Volunteer cheated!\n");
    }
    return 0;
}
