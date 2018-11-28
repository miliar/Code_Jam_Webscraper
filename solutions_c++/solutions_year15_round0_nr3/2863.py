#include <stdio.h>

#define MAX 10001

char S[MAX];
int pf[MAX];
int pb[MAX];
int Mul[5][5];
int Si[MAX];
int Sk[MAX];
int si, sk;

int change(char c);

int main() {
    freopen("C-small-attempt1.in", "r", stdin);
    freopen("outC.txt", "w+", stdout);
    Mul[1][1]=1;Mul[1][2]=2;Mul[1][3]=3;Mul[1][4]=4;
    Mul[2][1]=2;Mul[2][2]=-1;Mul[2][3]=4;Mul[2][4]=-3;
    Mul[3][1]=3;Mul[3][2]=-4;Mul[3][3]=-1;Mul[3][4]=2;
    Mul[4][1]=4;Mul[4][2]=3;Mul[4][3]=-2;Mul[4][4]=-1;
    int T;
    scanf("%d", &T);
    for(int t=1;t<=T;t++) {
        bool Yes = false;
        int L;si=sk=0;
        long long int X;
        scanf("%d%d", &L, &X);
        scanf("%s", S);

        pf[0]=change(S[0]);
        if(pf[0]==2) Si[si++] = 0;
        for(int i=1;i<L*X;i++) {
            if(pf[i-1]<0) pf[i]=(-1)*Mul[(-1)*pf[i-1]][change(S[i%L])];
            else    pf[i]=Mul[pf[i-1]][change(S[i%L])];
            if(pf[i]==2)    Si[si++] = i;
        }
        pb[X*L-1]=change(S[L-1]);
        if(pb[X*L-1]==4)    Sk[sk++] = X*L-1;
        for(int i=L*X-2;i>=0;i--) {
            if(pb[i+1]<0) pb[i]=(-1)*Mul[change(S[i%L])][(-1)*pb[i+1]];
            else    pb[i]=Mul[change(S[i%L])][pb[i+1]];
            if(pb[i]==4)    Sk[sk++] = i;
        }
        for(int i=0;i<si && !Yes;i++) {
            for(int j=0;j<sk;j++) {
                if((Sk[j]-1)>Si[i]) {
                    if(pf[Sk[j]-1]==4) {
                        Yes = true;
                        break;
                    }
                }
            }
        }

        printf("Case #%d: ", t);
        if(Yes) printf("YES\n");
        else    printf("NO\n");
    }

    return 0;
}

int change(char c) {
    if(c == '1') return 1;
    if(c == 'i') return 2;
    if(c == 'j') return 3;
    return 4;
}
