#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

bool check_str(string s);
int flipp(string s);

vector < string > data;

int main() {

    int i, cases, counter = 1;
    string str, strr;

    ifstream fin;
    ofstream fout;

    fin.open("Input.txt");

    fin >> cases;
    vector < int > flips;

    while (!fin.eof()) {
        if (counter == 1) {
            counter++;
            continue;
        } else {
            for (int i = 1; i <= cases; i++) {
                getline(fin, strr);
                data.push_back(strr);

            }
        }
        counter = 2;

    }

    for (int i = 1; i <= cases; i++) {

        str = data[i];

        flips.push_back(flipp(str));

    }

    fout.open("Output.txt");

    for (int i = 0; i < cases; i++)
        fout << "Case #" << i + 1 << ": " << flips[i] << endl;

    return 0;
}

bool check_str(string s) {
    bool flag = true;

    for (int i = 0; i <= s.length(); i++) {
        if (s[i] == '-')
            flag = false;

    }

    return flag;

}

int flipp(string s) {

    string str = s;
    int flip = 0;
    vector < int > vec;

    bool status = check_str(str);
    if (status == true) {
        flip = 0;
        return flip;

    }

    while (status == false) {

        for (int i = 0; i < str.length(); i++) {
            if (str[i] == '-')
                vec.push_back(i);
        }

        int pos = vec[vec.size() - 1];

        for (int k = 0; k <= pos; k++) {

            if (str[k] == '+') {
                str[k] = '-';

            } else
                str[k] = '+';
        }

        flip++;
        status = check_str(str);

    }

    return flip;
}
