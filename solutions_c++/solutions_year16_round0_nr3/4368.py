#include <stdio.h>
#include <math.h>

typedef unsigned long long ull;

FILE *fout = fopen("output.txt", "w");

int t, n, jj;
int coin[16];
ull ntDivs[10];
ull convN; // number converted to specific base

ull myPower(ull base, ull degree)
{
    ull result = 1;
    ull term = base;
    while (degree)
    {
        if (degree & 1)
            result *= term;
        term *= term;
        degree = degree >> 1;
    }
    return result;
}

void cnCoin(int ind)
{
    if(jj == 0) return; //found all J jamcoins

    //control: check if this number is jamcoin
    if(ind == n-1) {
        int i, j;
        int nb; //number base
        int jcFlag = 1; //true if this number is jamcoin
        int tFlag;
        ull tmpSqrt;

        for(nb=2; nb<11; nb++) {

            convN = 0;
            for(i=0; i<n; i++) {
                if(coin[i] == 1)
                    convN += coin[i]*myPower(nb, i);
            }

            tFlag = 0;

            if(convN%2 == 1) {
                tmpSqrt = (ull)sqrt(convN);
                for(j=3; j<=tmpSqrt; j+=2) {
                    if(convN % j == 0) {
                        ntDivs[nb-2] = j;
                        tFlag = 1;
                        break;
                    }
                }
            } else {
                ntDivs[nb-2] = 2;
                tFlag = 1;
            }
            // stop even if one base is not ok
            if(tFlag == 0) {
                jcFlag = 0;
                break;
            }
        }

        if(jcFlag == 1) {
            //print goes here...
            for(i=n-1; i>-1; i--) { //print binary JC num
                fprintf(fout, "%d",coin[i]);
            }

            for(i=0; i<9; i++) { //print non-triv divs
                fprintf(fout, " %lld",ntDivs[i]);
            } fprintf(fout, "\n");

            jj--; //one less jamcoin to be found
        }

        return;
    }

    coin[ind] = 1;
    cnCoin(ind+1);
    coin[ind] = 0;
    cnCoin(ind+1);
}

int main()
{
    FILE *fin = fopen("input.txt", "r");

    fscanf(fin, "%d%d%d", &t, &n, &jj);
    fprintf(fout, "Case #1:\n");

    coin[0] = 1;
    coin[n-1] = 1;
    cnCoin(1);


    fclose(fin);
    fclose(fout);
    return 0;
}
