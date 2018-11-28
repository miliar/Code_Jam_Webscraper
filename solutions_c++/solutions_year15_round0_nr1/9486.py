#include <iostream>
#include <vector>
#include <iterator>
#include <sstream>
#include <string>
#include <cstdlib>
using namespace std;

template<typename T, typename IN> vector<T> read_numbers(IN &fin)
{
    string line;
    getline(fin, line);
    istringstream linestr(line);

    vector<T> ret;
    back_insert_iterator< vector<T> > insert_it(ret);
    copy(istream_iterator<T>(linestr),
         istream_iterator<T>(),
         insert_it);
    return ret;
}

template<typename IN, typename OUT>
void solve(IN &fin, OUT &fout, int index)
{
    const auto line = read_numbers<string>(fin);
    const int num_elem = atoi(line[0].c_str());
    int num_inserted = 0, num_standing = 0;
    for(int i=0;i<=num_elem;++i) {
        int num_people = line[1][i] - '0';
        auto dif = i - num_standing;
        auto num_inserted_now =(num_people>0 && dif>0)?dif:0;
        num_standing += num_people + num_inserted_now;
        num_inserted += num_inserted_now;
    }
    fout << "Case #" << index << ": " << num_inserted << endl;
}

int main()
{
    const int t = read_numbers<int>(cin).back();  // I know...
    for(int i=0;i<t;++i) {
        solve(cin, cout, i+1);
    }
    return 0;
}
