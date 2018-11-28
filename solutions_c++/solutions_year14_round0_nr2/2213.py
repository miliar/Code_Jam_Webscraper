#include<iostream>
#include<fstream>
using namespace std;
int t, i, j, k, first_answer, second_answer, right_number, count;
double c, f, x, result, farm_time, farm_rate;
int main() {
    ifstream fin;
    ofstream fout;
    fin.open("B-small-attempt0.in");
    fout.open("B-small-practice.out");
    fin >> t;
    for (k = 0; k < t; ++k) {
        fin >> c;
        fin >> f;
        fin >> x;
        result = x/2;
        farm_time = 0;
        farm_rate = 2;
        for (;;) {
            //cout << result << endl;
            farm_time += c/farm_rate;
            farm_rate +=f;
            if (result > (farm_time + x/farm_rate))
                result = farm_time + x/farm_rate;
            else break;
        }
        fout << fixed;
        fout.precision(7);
        fout << "Case #" << k + 1 << ": " << result << endl;
        //printf("Case # %d: %.7f", k + 1, result);
    }
    fin.close();
    fout.close();
    return 0;
}
