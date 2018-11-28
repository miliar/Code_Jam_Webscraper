#include <iostream>
#include <fstream>
#include <iterator>
#include <vector>
#include <algorithm>
#include <cstring>

using namespace std;

int main()
{
    //INPUT
    typedef long data_type;
    string file_name("../data/Input");
    ifstream input_file(file_name);

    long T;
    input_file >> T;

    istream_iterator<data_type> start(input_file), end;
    vector<data_type> data(start, end);
    long data_size(0);



    data_size = data.size();
    if (data_size == 0) {
        cerr << "Data from file <" << file_name.c_str() << "> isn't loaded : " << strerror(errno) << endl;
        return 1;
    }
    cout << "File is open" << endl;
    cout << "Read " << data_size << " elements" << std::endl;
    cout << "Data read in:\n";
    ostream_iterator<data_type> out_stream_iterator(cout, " ");
    copy(data.begin(), data.end(), out_stream_iterator);
    input_file.close();
    cout << endl;

    //OUTPUT
    cout << "Start to write " << -1 << " elements" << std::endl;
    ofstream outfile("../data/Output");
    unsigned long i = 0;
    long number_of_longervals;
    long min_1(0), min_2(0);
    long c(1);
    while(i < data.size()) {
        number_of_longervals = data[i];
        if (number_of_longervals == 1) {
            cout << "Case #" << c << ": " << 0 << " " << 0 << endl;
            i++;
            i += 2;
            continue;
        }
        for(auto j = 1; j <= number_of_longervals-1; ++j) {
            long dif = data[i + j] - data[i + j + 1];
            min_1 += (dif > 0) ? dif : 0;
        }
        long rate(0);
        long stop_el(number_of_longervals);
        for(auto j = number_of_longervals - 1; j >= 0; --j) {
            long dif = data[i + j] - data[i + j + 1];
            rate = (dif > rate) ? dif : rate;
            //if (dif >= 0 && stop_el == number_of_longervals) stop_el = j + 1;
        }
        cout << rate << endl;
        if (rate > 0 )
        for(auto j = 1; j <= number_of_longervals - 1; ++j) {
            cout << data[i+j] << endl;
            min_2 += (data[i + j] > rate) ? rate : data[i + j];
        }
        outfile << "Case #" << c << ": " << min_1 << " " << min_2 << endl;
        min_1 = 0;
        min_2 = 0;
        c++;
        i += number_of_longervals + 1;
    }
    cout << "Finish to write " << -1 << " elements" << std::endl;
    outfile.close();

    return 0;
}
