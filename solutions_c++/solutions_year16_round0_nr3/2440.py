#include <iostream>
#include "GenValidSerial.h"
using namespace std;

int main()
{
    int T, N, J;
    cin >> T;
    for(int i=1; i<=T; i++){

        cin >> N >> J;
        cout << "Case #" << i << ":" << endl;
        GenValidSerial(J).genSerial(N);
    }

    return 0;
}
