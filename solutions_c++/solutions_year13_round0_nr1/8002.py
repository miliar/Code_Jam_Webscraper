#include <fstream>
using namespace std;

char v[5][5];
int horz[5][5],vert[5][5],pdiag[5][5],sdiag[6][6];
int t;
int main() {
    int i,j,l,fin,nrpct;
    char localwinner,c;
    ifstream in("a-small.in");
    ofstream out("output.out");
    in>>t;

    for (l=1; l<=t; l++) {
        fin=0;
        nrpct=0;
        localwinner = '.';
        for (i=1; i<=4; i++)
            for (j=1; j<=4; j++) {
                in>>v[i][j];
                if (!fin){
                if (v[i][j]=='.')
                    nrpct++;

                if ((v[i][j]==v[i][j-1]||v[i][j]=='T')&&v[i][j-1]!='.')
                    horz[i][j]=horz[i][j-1] +1;
                else if (v[i][j]!='.')
                    horz[i][j]=1;

                if ((v[i][j]==v[i-1][j]||v[i][j]=='T')&&v[i-1][j]!='.')
                    vert[i][j]=vert[i-1][j] +1;
                else if (v[i][j]!='.')
                    vert[i][j]=1;

                if ((v[i][j]==v[i-1][j-1]||v[i][j]=='T')&&v[i-1][j-1]!='.')
                    pdiag[i][j]=pdiag[i-1][j-1] +1;
                else if (v[i][j]!='.')
                    pdiag[i][j]=1;

                if ((v[i][j]==v[i-1][j+1]||v[i][j]=='T')&&v[i-1][j+1]!='.')
                    sdiag[i][j]=sdiag[i-1][j+1] +1;
                else if (v[i][j]!='.')
                    sdiag[i][j]=1;


                if (horz[i][j]==4) {
                    fin=1;
                    if (v[i][j]!='T')
                        localwinner=v[i][j];
                    else
                        localwinner=v[i][j-1];
                }

                else if (vert[i][j]==4) {
                    fin=1;
                    if (v[i][j]!='T')
                        localwinner=v[i][j];
                    else
                        localwinner=v[i-1][j];
                }

                else if (pdiag[i][j]==4) {
                    fin=1;
                    if (v[i][j]!='T')
                        localwinner=v[i][j];
                    else
                        localwinner=v[i-1][j-1];
                }

                else if (sdiag[i][j]==4) {
                    fin=1;
                    if (v[i][j]!='T')
                        localwinner=v[i][j];
                    else
                        localwinner=v[i-1][j+1];
                }
                }

            }
        out<<"Case #"<<l<<": ";
        if (fin)
            out<<localwinner<<" won"<<'\n';
        else if (!fin) {
            if (nrpct==0)
                out<<"Draw"<<'\n';
            else
                out<<"Game has not completed"<<'\n';
        }

        for (i=1; i<=4; i++)
            for (j=1; j<=4; j++)
                pdiag[i][j]=sdiag[i][j]=horz[i][j]=vert[i][j]=0;

    }

    out.close();
    return 0;


    }
