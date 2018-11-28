// g++ -O2 -o tst standingOvation.cpp
// cat input | ./tst > output


#include <iostream>     // std::cin, std::cout, std::hex
#include <fstream>      // std::fstream
#include <algorithm>    // std::reverse
#include <vector>       // std::vector

using namespace std;

typedef struct {
    int a;
    int b;
} tWire;

bool inf(tWire i, tWire j)
{
    return (i.a < j.a);
}

int main ()
{
    int numTests;
    int testNum = 0;

    cin >> numTests;

    while( ++testNum <= numTests) {

        int numS;
        cin >> numS;
        string S;
        getline(cin, S);
//        cout << "Line: \"" << S << "\""<< endl;
        int count = 0;
        int people = 0;
        for(int i =0; i < (numS+1); i++) {
            if(i > people) {
                count += (i - people);
                people+= (i - people);
            }
            people += S[i+1] - '0';
//            cout << people << " ";
        }
//        cout << endl;
        cout << "Case #" << testNum <<": " << count << endl;


    }

    cout << endl;

    return 0;
}


