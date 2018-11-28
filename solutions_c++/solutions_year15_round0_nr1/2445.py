#include <cstdlib>
#include <iostream>
#include "set"

using namespace std;

int main(int argc, char *argv[])
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    int T;
    cin >> T;

    int K;
    string S;
    int Vs;
	int y;
	int V;
    for (int T_i=0; T_i<T;T_i++){
        cin >> K;
        V = 0;
        y = 0;
        cin >> S;
        for (int K_i=0; K_i<=K; K_i++){
            Vs = (int)S[K_i] - 48;   
            if (V < K_i) {
                  y += K_i - V;
                  V = K_i;
               }
            V += Vs;
        }
        cout << "Case #" << T_i+1 << ": " << y << endl;
    }
    return EXIT_SUCCESS;
}
