#include<fstream>
#include<string>
#include<iomanip>
using namespace std;

ifstream fin("A-small-attempt0.in");
ofstream fout("A-small-attempt0.out");

int main() {
    int T,c;
    fin>>T;

    for (c=1; c<=T; ++c) {
        int row_num;
        int first_row[4];

        int i, j, k, tmp, ans = -1;

        fin>>row_num;
        for (i=0;i<4;++i)
            for (j=0;j<4;++j) {
                fin>>tmp;
                if (i == row_num-1) first_row[j] = tmp;
            }

        fin>>row_num;
        for (i=0;i<4;++i)
            for (j=0;j<4;++j) {
                fin>>tmp;
                if (i == row_num-1) {
                    for (k = 0; k<4; ++k)
                        if (first_row[k] == tmp) {
                            if (ans == -1) {
                                ans = tmp;
                            } else {
                                ans = -2;
                            }
                        }
                }
            }

        // output
        fout<<"Case #"<<c<<": ";

        if (ans == -2) fout<<"Bad magician!";
        else
        if (ans == -1) fout<<"Volunteer cheated!";
        else
        fout<<ans;

        
        fout<<endl;
    }
    return 0;
}
