#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

int T;
int N;
vector<bool> f(10);

void get(int N){
    int k = N;
    while(N != 0){
        f[N%10] = true;
        N = N/10;
    }
}

bool allget(){
    for(int i = 0; i < 10; i++)
        if (!f[i])
            return false;
    return true;
}

int main() {
    ifstream in("A-large.in");
    ofstream out("output.out");

    in >> T;
    for(int cases = 1; cases <=T; cases++){
        in >> N;
        if (N == 0)
            out << "Case #" << cases << ": INSOMNIA" << endl;
        else{
          for(int i = 0; i < 10; i++)
              f[i] = false;
          get(N);
          int M = N;
          while(!allget()){
              N = N+M;
              get(N);
          }
          out << "Case #" << cases << ": " << N << endl;
        }
    }

    in.close();
    out.close();
}