
#include <cstdlib>
#include <iostream>

using namespace std;



int main() {
    int T;
    cin >> T;
    
    for (int t=0; t<T; t++) {
        int A, B, K;
        cin >> A >> B >> K;
        
        int counter = 0;
        for (int a=0; a<A; a++) {
            for (int b=0; b<B; b++) {
                if ((a&b) < K)
                    counter++;
            }
        }
        
        cout << "Case #" << (t+1) << ": " << counter << endl;
    }

    return 0;
}


