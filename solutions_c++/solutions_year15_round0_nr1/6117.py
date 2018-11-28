#include <fstream>
#include <iostream>

using namespace std;

int main()
{
    ifstream testcase("example.txt");
    ofstream result("result.out");

    int ncases;
    testcase >> ncases;

    for(int c = 0; c < ncases; ++c) {
        int standing = 0;
        int needed = 0;
        int smax;
        testcase >> smax;
        for(int i=0; i<=smax; ++i) {
            char c;
            testcase >> c;
            int nb = c-'0';
            if(i>standing) {
                needed += i-standing;
                standing += i-standing;
            }
            standing += nb;
        }
        result << "Case #" << c+1 << ": " << needed << endl;

    }
}
