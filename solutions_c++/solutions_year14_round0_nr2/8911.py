#include <iostream>
#include <fstream>
using namespace std;

template<typename IN>
void skip_line(IN &fin)
{
    string line;
    getline(fin, line);
}

template<typename IN>
int read_number(IN &fin)
{
    int number;
    fin >> number;
    skip_line(fin);
    return number;
}

template<typename IN, typename OUT>
void solve_cookie(IN &fin, OUT &fout, int t)
{
    // Read data
    double c, f, x;
    fin >> c >> f >> x;
    skip_line(fin);
    //cout << "data=" << c << ", " << f << ", " << x <<endl;

    // Solve
    // without a factory ... tend = x/current_rate
    // with a factory....... tend = c/current_rate + x/(current_rate+f)

    double time = 0.0;
    double current_rate = 2;
    while(x/current_rate > c/current_rate + x/(current_rate+f)) {
        //cout << "Buy << " << time << endl;
        time += c/current_rate;
        current_rate += f;
    }

    fout.setf(ios::fixed);
    fout.precision(8);
    fout << "Case #" << t+1 << ": " << (time + x/current_rate) << endl;
}

int main()
{
    const int t = read_number(cin);
    for(int i=0;i<t;++i) {
        solve_cookie(cin, cout, i);
    }
    return 0;
}
