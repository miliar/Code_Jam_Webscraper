#include <iostream>
#include <fstream>


using namespace std;
int main()
{
    ofstream out("out.txt");
    ifstream in("in.txt");
    int count;
    long long nValue;
    unsigned int targetValue = 1023;
    in >> count;
    for (int i = 0; i < count; i++) {
        unsigned int numbersSeen = 0;
        long long multipliedNValue = 0;
        in >> nValue;
        if (nValue == 0) {
            out << "Case #" << i + 1 << ": INSOMNIA\n";
        } else {
            do {
                multipliedNValue += nValue;
                long long temp = multipliedNValue;
                while(temp > 0) {
                    numbersSeen = (numbersSeen | (1 << (temp % 10)));
                    temp /= 10;
                }
            } while (numbersSeen != targetValue);
            out << "Case #" << i + 1 << ": " <<  multipliedNValue << "\n";
        }
    }
    out.close();
    in.close();
}
