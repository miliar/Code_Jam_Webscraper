#include <fstream>

using namespace std;

int main()
{
    int i,j,k,x,y,t;
    int c = 0;
    int a[5][5];
    int b[5][5];

    ifstream fin("magic.in");
    ofstream fout("magic.out");

    fin>>t;
    while (c<t){
        c++;
        fin>>x;
        for (i=1;i<=4;i++)
            for (j=1;j<=4;j++) fin>>a[i][j];

        fin>>y;
        for (i=1;i<=4;i++)
            for (j=1;j<=4;j++) fin>>b[i][j];
        int ans = 0;;
        k = 0;
        for (i=1;i<=4;i++)
            for (j=1;j<=4;j++){
                if (a[x][i]==b[y][j]){
                    ans = a[x][i];
                    k++;
                }
            }
        if (k > 1)  fout<<"Case #"<<c<<": Bad magician!"<<endl;
        if (k == 1) fout<<"Case #"<<c<<": "<<ans<<endl;
        if (k == 0) fout<<"Case #"<<c<<": Volunteer cheated!"<<endl;
    }
    return 0;
}
