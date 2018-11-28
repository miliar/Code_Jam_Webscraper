#include <iostream>
#include <fstream>
#include <iomanip>
using namespace std;

int main()
{
    ofstream output("solved.out");
    ifstream input("test.in");
    int test_cases;
    input >> test_cases;
    for (int i = 0; i < test_cases; i++) {


    double c; //30
    double f;//1
    double x;//2
    double cookiesec = 2;

    input >> c;
    input >> f;
    input >> x;

    double y = 0;
    for (cookiesec = 2; x/cookiesec > ((x/(cookiesec+f)) +(c/cookiesec)); cookiesec= cookiesec+f) {
        y = y + c/cookiesec;
    }
   output << "Case #" << i+1 << ": " << fixed << setprecision(7) << (x/cookiesec) + y << endl;

}
    return 0;
}
