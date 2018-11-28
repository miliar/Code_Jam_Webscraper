#include <fstream>
using namespace std;

int v[5][5];
int inrow[17];
int main() {

    int i,j,l,t,r,ans;

    ifstream in("A-small.in");
    ofstream out("output.out");

    in>>t;

    for (l=1; l<=t; l++) {
        for (i=1; i<=16; i++)
            inrow[i]=0;
        ans=0;
        in>>r;
        for (i=1; i<=4; i++)
            for (j=1; j<=4; j++) {
                in>>v[i][j];
                if (i==r)
                    inrow[v[i][j]]=1;
            }

        in>>r;
        for (i=1; i<=4; i++)
            for (j=1; j<=4; j++) {
                in>>v[i][j];
                if (i==r) {
                    if (inrow[v[i][j]]&&ans==0)
                        ans=v[i][j];
                    else if (inrow[v[i][j]]&&ans!=0) {
                        ans=-1;
                    }
                }

            }

        out<<"Case #"<<l<<": ";
        if (ans==-1)
            out<<"Bad magician!"<<'\n';
        else if (ans==0)
            out<<"Volunteer cheated!"<<'\n';
        else
            out<<ans<<'\n';
    }

    in.close();
    out.close();
    return 0;

}
