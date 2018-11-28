#include <iostream>
#include <fstream>
#include <iterator>
#include <vector>
#include <algorithm>
#include <cstring>
#include <utility>

using namespace std;

struct Quaternion {
public:
    char c;
    //true = +, false -
    bool sign;

    Quaternion(char c,bool sign = true)
        : c(c), sign(sign)
    {}

    Quaternion() {}

    Quaternion operator*(const Quaternion& q) const {
        char c_res;
        bool sign_res(true);
        Quaternion q_res;
        switch (c) {
        case '1':
            switch (q.c) {
            case '1':
                c_res = '1';
                break;
            case 'i':
                c_res = 'i';
                break;
            case 'j':
                c_res = 'j';
                break;
            case 'k':
                c_res = 'k';
                break;
            }
            break;

        case 'i':
            switch (q.c) {
            case '1':
                c_res = 'i';
                break;
            case 'i':
                c_res = '1';
                sign_res = false;
                break;
            case 'j':
                c_res = 'k';
                break;
            case 'k':
                c_res = 'j';
                sign_res = false;
                break;
            }
            break;

        case 'j':
            switch (q.c) {
            case '1':
                c_res = 'j';
                break;
            case 'i':
                c_res = 'k';
                sign_res = false;
                break;
            case 'j':
                c_res = '1';
                sign_res = false;
                break;
            case 'k':
                c_res = 'i';
                break;
            }
            break;

        case 'k':
            switch (q.c) {
            case '1':
                c_res = 'k';
                break;
            case 'i':
                c_res = 'j';
                break;
            case 'j':
                c_res = 'i';
                sign_res = false;
                break;
            case 'k':
                c_res = '1';
                sign_res = false;
                break;
            }
            break;
        }
        q_res.c = c_res;
        q_res.sign = (sign == q.sign) == sign_res;
        return q_res;
    }

    friend ostream& operator<< (ostream& out,const Quaternion& q) {
        return out << (q.sign ? "" : "-" )<< q.c << endl;
    }

    bool operator== (const Quaternion& that) const {
        return c == that.c && sign == that.sign;
    }

    bool operator!= (const Quaternion& that) const {
        return !(*this == that);
    }
};

vector<Quaternion> mk_quaternions(string s) {
    vector<Quaternion> quaternions;
    for (auto c: s) quaternions.push_back(Quaternion(c));
    return quaternions;
}

Quaternion multiply(const vector<Quaternion>& v, int begin, int end, int L) {
    Quaternion res('1');
    for(auto i = begin; i <=end; ++i) res = res * v[i % L];
    return res;
}

string get_solution(pair<pair<int, int>, string> data) {
    vector<Quaternion> quaternions;
    int L, X, begin, end, LX;
    Quaternion l('1'), r('1');
    Quaternion i('i'), j('j'), k('k');
    L = data.first.first;
    X = data.first.second;
    LX = L*X;

    begin = 0;
    end = LX - 1;

    if (L * X < 3) return "NO";

    quaternions = mk_quaternions(data.second);
    l = l * quaternions[begin % L];
    r = quaternions[end % L] * r;

    //for (auto q: quaternions) cout << q;
    int temp;
    Quaternion q_temp;
    while (begin < end) {
        /*cout << "b=" << begin << " e=" << end << endl;
        cout << "l_i=" << begin % L << " r_i=" << end % L << endl;
        cout << "l=" << l << "r=" << r << endl;*/

        if ( l != i && r != k) {
            begin++;
            end--;
            l = l * quaternions[begin % L];
            r = quaternions[end % L] * r;
        }
        else if ( l == i && r != k) {
            end--;
            r = quaternions[end % L] * r;
            /*temp = end;
            Quaternion q_temp('1');
            while(begin < temp) {
                q_temp = quaternions[temp % L] * q_temp;
                if(q_temp == k)
                    if (multiply(quaternions, begin, temp, L) == j) return "YES";
                temp--;
            }*/
        }
        else if ( l != i && r == k) {
            begin++;
            l = l * quaternions[begin % L];
            /*temp = begin;
            Quaternion q_temp('1');
            while(temp < end) {
                q_temp = q_temp * quaternions[temp % L];
                if(q_temp == i)
                    if (multiply(quaternions, temp, end, L) == j) return "YES";
                temp++;
            }*/
        }
        else {
            begin++;
            end--;
            l = l * quaternions[begin % L];
            r = quaternions[end % L] * r;
            if (multiply(quaternions, begin, end, L) == j) return "YES";
        }
        //cout << "-----------------" << endl;
    }

    return "NO";
}

int main()
{
    //INPUT
    typedef string data_type;
    string file_name("../data/Input");
    ifstream input_file(file_name);

    int i(0);
    int T;
    input_file >> T;

    istream_iterator<data_type> start(input_file), end;
    vector<data_type> data(start, end);
    int data_size(0);

    data_size = data.size();
    if (data_size == 0) {
        cerr << "Data from file <" << file_name.c_str() << "> isn't loaded : " << strerror(errno) << endl;
        return 1;
    }
    cout << "T=" << T << endl;
    cout << "File is open" << endl;
    cout << "Read " << data_size << " elements" << std::endl;
    cout << "Data read in:\n";

    /*ostream_iterator<data_type> out_stream_iterator(cout, " ");
    copy(data.begin(), data.end(), out_stream_iterator);
    input_file.close();
    cout << endl;*/

    //////////////////////////DO YOUR CODE HERE//////////////////////////
    vector<pair<pair<int, int>, string>> format_data;
    pair<pair<int, int>, string> one_case;
    for (i = 0; i < data_size; i += 3) {
        one_case = pair<pair<int, int>, string>(pair<int, int>(stoi(data[i]), stoi(data[i+1])), data[i+2]);
        format_data.push_back(one_case);
    }

    i = 0;
    for(auto fd : format_data) {
        //cout << "Case #" << i << ": " << << endl;
        cout << "Case #" << i << ": " << endl;
        cout << "size = " << fd.second.size() << endl;
        //cout << fd.first.first << " " << fd.first.second << " " << fd.second << endl;
        i++;
    }

    /*i = 0;
    for(auto fd : format_data) {
        cout << "Case #" << i+1 << ": " << get_solution(fd) << endl;
        i++;
    }*/

    /*Quaternion q1('i');
    Quaternion q2('j');
    Quaternion q3('i');
    cout << "Quaternions=" << endl;
    cout << q1 * q2;
    cout << q1 * q2 * q3;

    Quaternion q4('j');
    Quaternion q5('i');
    Quaternion q6('j');
    Quaternion q7('i');
    Quaternion q8('j');
    Quaternion q9('i', false);

    cout << q4 * q5 * q6 * q7 * q8 * q9;

    Quaternion q10('k');
    Quaternion q11('k');

    cout << q10 * q11;*/

    /////////////////////////////////////////////////////////////////////

    //OUTPUT
    cout << "Start to write " << T << " elements" << std::endl;
    ofstream outfile("../data/Output");
    i = 0;
        for(auto fd : format_data) {
            outfile << "Case #" << i+1 << ": " << get_solution(fd) << endl;
            i++;
        }
    cout << "Finish to write " << T << " elements" << std::endl;
    outfile.close();

    return 0;
}
