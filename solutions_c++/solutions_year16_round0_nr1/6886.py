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

	long long Seed;
	long long N;
	long long Old;
	long long Test;
	int X[10];
	
    for (int T_i=0; T_i<T;T_i++){
        cin >> Seed;
        
        for (int ii=0;ii<10; ii++){
            X[ii]=0;
        }
        N=Seed;
        Old = 0;
        while (((X[0]==0) || (X[1] ==0) || (X[2] ==0) || (X[3]==0)  || (X[4]==0) || (X[5] ==0) || (X[6] ==0) || (X[7]==0) || (X[8] ==0) || (X[9] ==0)) && (Old != N)) {
              Test = N;
              while (Test > 0) {
                    X[Test % 10]  = 1;
                    Test = int(Test / 10);
                    }
              Old = N;
              N = N + Seed;
        }
        
        if ((X[0]==1) && (X[1] ==1) && (X[2] ==1) && (X[3] ==1) && (X[4]==1) && (X[5] ==1) && (X[6] ==1) && (X[7]==1) && (X[8] ==1) && (X[9] ==1) ) {
        cout << "Case #" << T_i+1 << ": " << Old << endl;
        } else {
        cout << "Case #" << T_i+1 << ": INSOMNIA" << endl;
    
               }        
        
    }
    return EXIT_SUCCESS;
}
