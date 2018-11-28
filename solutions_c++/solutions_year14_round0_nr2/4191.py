#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <algorithm>
#include <iomanip>

using namespace std;

std::vector<double> split(const std::string &s, char delim)
{
    std::vector<double> elems;
    std::stringstream ss(s);
    std::string item;
    while (std::getline(ss, item, delim)) {
        elems.push_back(stod(item));
    }
    return elems;
}

double get_seconds(double F, double X)
{
    return X / double(2. + F);
}

int main()
{
    ifstream input;
    input.open("input.txt");

    ofstream output;
    output.open("output.txt");
    output.setf(ios::fixed);
    output.setf(ios::showpoint);

    string reader;
    getline(input, reader);

    const int T = atoi(reader.c_str());
    for (int i = 0; i < T; i++) {
        getline(input, reader);
        auto elems = split(reader, ' ');

        double C = elems[0];
        double F = elems[1];
        double X = elems[2];

        double extra = 0;
        double minsec = get_seconds(extra, X);
        double farmsec = 0.0;
        while (true) {
            farmsec += get_seconds(extra, C);
            extra += F;
            double res = farmsec + get_seconds(extra, X);
            if (minsec < res) {
                break;
            }
            else
                minsec = res;
        }

        output << "Case #" << i + 1 << ": " << setprecision(7)  << minsec << "\n";

    }

    input.close();
    output.close();

    return 0;
}
