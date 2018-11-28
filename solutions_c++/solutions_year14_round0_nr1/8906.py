#include <iostream>
#include <fstream>
#include <array>
#include <algorithm>
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

template<typename IN>
void read_line(IN &fin, array<int, 4> &line)
{
    for(int i=0;i<4;++i) {
        fin >> line[i];
    }
    skip_line(fin);
}

template<typename IN>
void read_square(IN &fin, array<int, 4> &line)
{
    const int num_row = read_number(fin);
    for(int i=0;i<4;++i) {
        if(i==num_row-1) {
            read_line(fin, line);
        }
        else {
            skip_line(fin);
        }
    }
    sort(begin(line), end(line));
}


template<typename IN, typename OUT>
void solve_case(IN &fin, OUT &fout, int t)
{
    array<int, 4> line[2];
    read_square(fin, line[0]);
    read_square(fin, line[1]);
    vector<int> result;
    set_intersection(begin(line[0]), end(line[0]),
                     begin(line[1]), end(line[1]),
                     back_inserter(result));
    fout << "Case #" << t+1 << ": ";
    if(result.empty())          fout << "Volunteer cheated!";
    else if(result.size() == 1) fout << result[0];
    else                        fout << "Bad magician!";
    fout << endl;
}


int main(int argc, char *argv[])
{
    const int t = read_number(cin);
    for(int i=0;i<t;++i) {
        solve_case(cin, cout, i);
    }

    return 0;
}
