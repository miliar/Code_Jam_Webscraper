#include <fstream>

using namespace std;

int main(){
    ifstream fin;
    fin.open("A-small-input.ln", fstream::in);
    ofstream fout;
    fout.open("A-small-output.ln", fstream::out);

    int T;
    fin >> T;
    for(int i = 1; i <= T; i ++){
        int a[4][4], b[4][4];
        int m, n;
        int ans = 0;

        fin >> m;
        for(int j = 0; j < 4; j ++)
            for(int k = 0; k < 4; k++)
                fin >> a[j][k];
        fin >> n;
        for(int j = 0; j < 4; j ++)
            for(int k = 0; k < 4; k++)
                fin >> b[j][k];
        

        for(int j = 0; j < 4; j ++)
            for(int k = 0; k < 4; k++)
                if(a[m - 1][j] == b[n - 1][k]){
                    if(ans ==0)
                        ans = a[m - 1][j];
                    else
                        ans = -1;
                }

        fout << "Case #" << i << ": ";
        if(ans > 0)
            fout << ans << endl;
        else if(ans == -1)
            fout << "Bad magician!" << endl;
        else if(ans == 0)
            fout << "Volunteer cheated!" << endl;
    }

    fin.close();
    fout.close();

    return 0;
}
