#include <cstdlib>
#include <iostream>
#include "set"
#include "math.h"

using namespace std;

int main(int argc, char *argv[])
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    int T;
    cin >> T;

	int y;
	int B;
	int Bi;
	long long N;
	long Mk[1000];
	long Bk[1000];
	int Rep;
	long long Ni;
	long MinB;
	long MinB2;
    for (int T_i=0; T_i<T;T_i++){
        cin >> B >> N;
        
        for (int B_i=0; B_i < B; B_i++){
            cin >> Mk[B_i];
            Bk[B_i] = 0;
        }
        
        Ni=0;
        Bi=0;
        MinB = 1000000;
        
        while (Ni < N){
                  while ((Bk[Bi] != 0) && (Bi < B)) Bi++;
                  if((Bk[Bi]==0) && (Bi < B)) {
                      Bk[Bi]= Mk[Bi];
                      y = Bi;
                      if (MinB > Mk[Bi]) MinB = Mk[Bi];
                      Bi++;
                      Ni++;
                  }
                  if (Bi== B) {
                     MinB2 = 1000000;
                     for (int B_i=0;B_i<B; B_i++){
                         Bk[B_i] -= MinB;
                         if ((Bk[B_i] > 0) && (Bk[B_i] < MinB2)) MinB2 = Bk[B_i];
                         if ((Bk[B_i] ==0) && (Bi > B_i)) Bi=B_i;
                     }
                     MinB = MinB2;
                     if ((MinB2==1000000) && (Ni < N)) {
                        Ni = (long long)(floor(N / Ni) * Ni);
                     }
                  }
              }
        cout << "Case #" << T_i+1 << ": " << (y+1) << endl;
    }
    return EXIT_SUCCESS;
}
