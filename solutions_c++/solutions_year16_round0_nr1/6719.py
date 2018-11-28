#include <iostream>
#include <string>
#include <fstream>
using namespace std;

class P1{
private:
    bool flag[10];
public:
    P1() {
        for (int i=0; i<10; i++)
            flag[i] = 0;
    }
    long long test(string v) {
        int len;
        long long num;
        long long base = stoll(v,0,0);
        bool good;
        while (1) {
            good = 1;
            len = v.length();
            for (int i= 0; i<len; i++) {
                if (flag[v[i] - '0'] == 0) {
                    flag[v[i] - '0'] = 1;
                }
            }
            for (int i=0; i<=9; i++) {
                if (flag[i] == 0) {
                    good = 0;
                    break;
                }
            }
            if (good == 0) {
                num = stoll(v,0,0);
                num = num+base;
                v = to_string(num);
            } else {
                num = stoll(v,0,0);
                return num;
            }
        }
    }
};

int main() {
    ifstream fin("A-large.in.txt");
    ofstream fout("out2.txt");
    string number;
    fin >> number;
    
    int n = stoi(number, 0, 0);
    for (int i=1; i<=n; i++) {
        fin >> number;
        P1 p;
        if(number == "0")
            fout << "Case #" << i << ": INSOMNIA" << endl;
        else
            fout << "Case #" << i << ": " << p.test(number) << endl;
    }
    
}