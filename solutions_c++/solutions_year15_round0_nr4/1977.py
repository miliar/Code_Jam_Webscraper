#include <fstream>
#include <vector>
#include <algorithm>
#include <cstring>
using namespace std;

int T;

int main()
{
    ifstream fin("D-small-attempt1.in");
    //ifstream fin("file.in");
    ofstream fout("file.out");

    fin >> T;

    int X,N,M;
    string R = "RICHARD";
    string G = "GABRIEL";
    string ans;

    for(int t = 1; t <= T; t++){
        fin >> X >> N >> M;
        if(N > M) swap(N,M);
        if(X >= 7) ans = R;

        else if(X == 1) ans = G;
        else if(X == 2){
            if(N*M%2 == 0) ans = G;
            else ans = R;
        }
        else if(X == 3){
            if(N*M%3 != 0 || N == 1) ans = R;
            else ans = G;
        }
        else if(X == 4){
            if(N*M%4 != 0) ans = R;
            else{
                if(N >= 3 && M >= 4) ans = G;
                else ans = R;
            }
        }

        fout << "Case #" << t << ": " << ans << "\n";


    }

}
