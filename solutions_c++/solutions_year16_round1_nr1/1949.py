#include <iostream>
#include <fstream>

using namespace std;

int main() {
    ifstream fin("A-large.in");
    ofstream fout("output-large.txt");
    int T, n, i;
    char s, S[1001];
    fin >> T;
    fin.get();
    //cout << "T input : " << T;
    for(int l = 0; l < T; l++) {
        //cout << "\nin Loop : iteration = " << i+1 ;
        s = fin.get();
        S[0] = s;
        n = 1;
        s = fin.get();
        //getchar();
        while(s != '\n') {
            //cout << "\ninside inner loop";
            for(i = 0; i < n; i++){
                if(s > S[i]){
                    i = 0;
                    break;
                }else if(s < S[i]){
                    i = n;
                    break;
                }
            }
            if(i == 0){
                for(int j = n; j > 0; j--){
                    S[j] = S[j - 1];
                }
            }
            S[i] = s;
            n++;
            s = fin.get();
        }
        fout << "Case #" << l+1 << ": ";
        for(int k = 0; k < n; k++){
            fout << S[k];
        }
        fout << '\n';
    }
    return 0;
}
