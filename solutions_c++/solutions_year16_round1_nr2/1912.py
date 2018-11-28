#include <iostream>
#include <fstream>

using namespace std;

int main() {
    ifstream fin("B-large.in");
    ofstream fout("output-large.txt");
    int T, n, h[2501], m[51], ip, j, temp;
    fin >> T;
    for(int l = 0; l < T; l++) {
        fin >> n;
        for(int i = 1; i <= 2500; i++){
            h[i] = 0;
        }

        for(int i = 0; i < 2*n-1; i++){
            for(int j = 0; j < n; j++){
                fin >> ip;
                h[ip]++;
            }
        }

        j = 0;
        for(int i = 1; i <= 2500; i++){
            if(h[i]%2){
                m[j] = i;
                j++;
            }
        }

        for(int i = 1; i < n; i++){
            for(j = 0; j < (n - i); j++)
                if(m[j] > m[j+1]){
                    temp = m[j];
                    m[j] = m[j+1];
                    m[j+1] = temp;
                }
        }


        fout << "Case #" << l + 1 << ": ";

        for(int k = 0; k < n; k++){
            fout << m[k] << " ";
        }

        fout << '\n';

    }
    return 0;
}
