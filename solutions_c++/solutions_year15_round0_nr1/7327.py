#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
using namespace std;
void get_audience(ifstream &ifile);
void write_output(int cnt, int smax, string aud);

int main() {
    ifstream f;
    f.open("input.txt");
    remove("out.txt");
    if (!f.is_open()) {
        return 0;
    } else {
        get_audience(f);
    }
    return 0;
}

void get_audience(ifstream &ifile) {
    string line;
    int num, smax, cnt = 1;
    getline(ifile,line);
    stringstream(line) >> num;
    while (ifile >> smax >> line) {
        write_output(cnt, smax, line);
        cnt++;
    }
    return;
}

void write_output(int cnt, int smax, string aud) {
    int i = 0, diff = 0, invite = 0, total = 0;
    string out;
    stringstream c;
    c << cnt;
    ofstream o;
    o.open("out.txt", fstream::app);
    for (string::iterator it = aud.begin(); i <= smax; ++it, i++) {
        int count = *it - '0';
        diff = total - i;
        if (count > 0) {
            if (diff < 0) {
                invite -= diff;
                total += count - diff;
            } else {
                total += count;
            }
        }
    }
    cout << "Case #" << cnt << ": " << invite << endl;
    out = "Case #" + c.str() + ": ";
    stringstream c1;
    c1 << invite;
    out += c1.str();
    o << out << "\n";
    o.close();
    return;
}
