#include <iostream>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <math.h>

using namespace std;

int main()
{
    ifstream in("prob b.in");
    ofstream out("prob b.out");

    int T;
    in >> T;

    for(int t = 0; t < T; ++t) {
        int A, B, K;
        in >> A >> B >> K;
        
        int count = 0;
        
        for(int i = 0; i < A; ++i) {
          for(int j = 0; j < B; ++j) {
            if((i & j) < K)
              count++;
          }
        }
        
        out << "Case #" << t+1 << ": " << count << endl;
    }

    out.close();
}
