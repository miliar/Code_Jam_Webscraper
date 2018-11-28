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
    int N;
	long long y;
	long long z;
	int NN[1000];
	int NMax;
    for (int T_i=0; T_i<T;T_i++){
        cin >> N;
        y= 0;
        z=0;
        NMax = 0;
        for (int Ni =0; Ni < N;Ni++){
            cin >> NN[Ni];
            if (Ni>0) {
               if (NN[Ni] < NN[Ni-1]) y += NN[Ni-1]-NN[Ni];
               if ((NN[Ni-1]-NN[Ni]) > NMax) NMax = NN[Ni-1]-NN[Ni];
            }
        }
        for (int Ni =1; Ni < N;Ni++){
            if ((NN[Ni-1]-NN[Ni]) == NMax ){
                 z += NMax;
            } else {
                 if ((NN[Ni-1] - NMax) <0)
                 {z += NN[Ni-1]; } else 
                 {z += NMax;}
            }
            
        }
        
        cout << "Case #" << T_i+1 << ": " << y << " " << z << endl;
    }
    return EXIT_SUCCESS;
}
