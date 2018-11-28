# include <bits/stdc++.h>
# define NR 100005
using namespace std;
ifstream f("date.in");
ofstream g("date.out");
int i,j,n,m,T,R,P,S,test,ok;
char s[NR], aux[NR];
bool verifica () {
    strcpy(aux+1, s+1);
    int I,J;
    for (int nivel=n; nivel>=1; --nivel) {
        int POZ=0;
        for (int i=1; i<=(1<<nivel); i+=2) {
            I=i; J=i+1;

            if (aux[I]==aux[J]) return 0;
            else {
                if (aux[I]=='R' && aux[J]=='P') aux[++POZ]='P';
                if (aux[I]=='P' && aux[J]=='R') aux[++POZ]='P';
                if (aux[I]=='R' && aux[J]=='S') aux[++POZ]='R';
                if (aux[I]=='S' && aux[J]=='R') aux[++POZ]='R';
                if (aux[I]=='S' && aux[J]=='P') aux[++POZ]='S';
                if (aux[I]=='P' && aux[J]=='S') aux[++POZ]='S';
            }
        }
    }

    return 1;
}

void BACK (int k) {
    if (ok) return;
    if (k==(1<<n)+1) {
        if (verifica()) {
            ok=1;
            for (int i=1; i<=(1<<n); ++i)
                g<<s[i];
            g<<"\n";
        }
    } else {
        if (P) {
            --P; s[k]='P';
            BACK (k+1);
            ++P;
        }

        if (R) {
            --R; s[k]='R';
            BACK (k+1);
            ++R;
        }


        if (S) {
            --S; s[k]='S';
            BACK (k+1);
            ++S;
        }
    }
}
int main ()
{
    f>>T; int test=0;
    while (T--) {
        f>>n>>R>>P>>S;
        ++test; g<<"Case #"<<test<<": ";

        ok=0;
        BACK (1);

        if (ok==0) g<<"IMPOSSIBLE\n";
    }



    return 0;
}
