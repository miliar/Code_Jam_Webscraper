#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>
#include <set>

using namespace std;

string gen(string ch, int k) {
    string str = "";
    while (k--) str += ch;
    return str;
}

int solve(string str) {
    int k = 0;
    while (str.find("-")!=-1) {
        k++;
        int fb = str.find_first_of("-");
        int ft = str.find_first_of("+");
        if (ft==-1) ft = str.length();
        if (fb < ft) {
            str = gen("+",ft-fb) + str.substr(ft,str.length());
        } else {
            str = gen("-", fb-ft) + str.substr(fb,str.length());
        }
    }
    return k;
}

int main(int argc, char *argv[]) {

    ifstream in;
    ofstream out;
    in.open("C:\\Users\\Administrator\\Desktop\\MAD\\B-small-attempt0.in");
    out.open("C:\\Users\\Administrator\\Desktop\\MAD\\out.txt");

    int cases;
    in>>cases;
    for (int i=1; i<=cases; i++) {
        string str;
        in >> str;

        out<<"Case #"<<i<<": "<<solve(str);
        out<<endl;
    }
    in.close();
    out.close();

    return 0;
}
