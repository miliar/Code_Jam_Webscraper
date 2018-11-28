#include <cstdio>
#include <cstdlib>
#include <vector>
#include <algorithm>

using namespace std;


int tab[100][100];
int tabW[100];
int tabK[100];


int main() {
    int T;
    scanf("%d", &T);
    for (int t=1; t<=T; t++) {
	int N, M;
        scanf("%d %d", &N, &M);
        for (int n=0; n<N; n++) for (int m=0; m<M; m++) {
	    scanf("%d", &tab[n][m]);
        }
        for (int n=0; n<100; n++) tabW[n]=tabK[n]=0;
        for (int n=0; n<N; n++) for (int m=0; m<M; m++) {
	    tabW[n]=max(tabW[n], tab[n][m]);
	    tabK[m]=max(tabK[m], tab[n][m]);
        }
        bool OK=true;
        for (int n=0; n<N; n++) for (int m=0; m<M; m++)
	    OK=OK&&(tab[n][m]==min(tabW[n],tabK[m]));
	printf("Case #%d: %s\n", t, OK?"YES":"NO");
    }
    return 0;
}
