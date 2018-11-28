#include <bits/stdc++.h>
#define optimizar_ ios_base::sync_with_stdio(0);cin.tie(0);

using namespace std;

int bm;

int main(){
    //optimizar_
    ifstream cin2;
    ofstream cout2;
    cin2.open("a.in", ios::in);
    cout2.open("result.txt", ios::out);
    int T;
    cin2 >> T;
    int N, cont, copy;
    int lim = (1 << 10) - 1;

    for(int i = 1; i <= T; i++){
        cout2 << "Case #" << i << ": ";
        cin2 >> N;

        if(N == 0){
            cout2 << "INSOMNIA\n";
            continue;
        }

        cont = 1;
        bm = 0;
        while(bm != lim){
            int copy = cont * N;

            while(copy){
                bm = bm | (1 << (copy % 10));
                copy /= 10;
            }
            cont ++;
        }

        if(bm == lim){
            cout2 << N * (cont - 1) << "\n";
        }
    }

    cout2 << flush;
    cout2.flush();
    cout2 << endl;

    cin2.close();
    cout2.close();

    return 0;
}