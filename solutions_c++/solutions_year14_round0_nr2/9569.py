#include <iostream>
#include <fstream>
#include<iomanip>
using namespace std;

int main()
{
    ifstream input;
    ofstream output;
    output.open("out.txt");
    input.open("B-small-attempt0.in");
    int t;
    input >> t;
    int i = 0;
    while(i < t){
        double c, f, x;
        input >> c >> f >> x;
        double sec1 = 50001.0, sec2 = x / 2.0;
        int count = 1;
        while(sec2 < sec1){
            sec1 = sec2;
            sec2 = 0.0;
            for(int j = 0; j < count; j++){
                sec2 += c / (2.0 + f * j);
            }
            sec2 += x / (2.0 + f * count);
            count++;
        }
        output << setiosflags(ios::fixed) << setprecision(7) << "Case #" << i + 1 << ": " << sec1 << endl;
        i++;
    }
    input.close();
    output.close();
    return 0;
}
