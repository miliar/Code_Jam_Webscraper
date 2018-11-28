/*
g++ -O2 -o tst mushroom.cpp
cat in | ./tst > out
*/


#include <iostream>     // std::cin, std::cout, std::hex
#include <fstream>      // std::fstream
#include <algorithm>    // std::reverse
#include <vector>       // std::vector

using namespace std;



int main ()
{
    int i;
    int numTests;
    int testNum = 0;

    cin >> numTests;

    while( ++testNum <= numTests) {
        int N;

        cin >> N;
        int Ni[N];
        for(i=0; i<N; i++){
            cin >> Ni[i];
//            cout << Ni[i] << " ";
        }
//        cout << endl;

        // Method 1
        int count1 = 0;
        int total = 0;
        int maxDiff = 0;
        for(i=1; i<N; i++){
            int diff = Ni[i-1] - Ni[i];
//            cout << "Diff: " << diff << endl;
            if(diff > 0) {
                count1 += diff;
                if(diff > maxDiff) {
                    maxDiff = diff;
                }
            }
        }

        // Method 2
        int count2 = 0;
//        cout << "Max: " << maxDiff << endl;
        for(i=1; i<N; i++){
            if(Ni[i-1] <= maxDiff) {
                count2 += Ni[i-1];
            }
            else {
                count2+= maxDiff;
            }
//            cout << count2 << endl;
        }
        cout << "Case #" << testNum <<": " << count1 << " " << count2 << endl;
    }

    cout << endl;

    return 0;
}


