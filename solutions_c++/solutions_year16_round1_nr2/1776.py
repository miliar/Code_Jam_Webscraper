#include <iostream>
#include <fstream>

using namespace std;

ifstream fin("rankLarge.in");
ofstream fout("rankLarge.out");

int numUse[2502];

void reset(){
    for(int i = 0; i < 2502; i++){
        numUse[i] = 0;
    }
}

int main(){
    int T, N, num;
    fin>>T;
    for(int t = 1; t <= T; t++){
        fout<<"Case #"<<t<<":";
        reset();
        fin>>N;
        for(int n = 0; n < 2*N-1; n++){
            for(int i = 0; i < N; i++){
                fin>>num;
                numUse[num]++;
            }
        }
        for(int i = 1; i <= 2500; i++){
            if(numUse[i] % 2 == 1){
                fout<<" "<<i;
            }
        }
        fout<<"\n";
    }
    fin.close();
    fout.close();
}
