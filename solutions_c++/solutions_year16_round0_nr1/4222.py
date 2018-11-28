#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>
#include <set>

using namespace std;

int solve(int n) {
    //cout << n << endl;
    set <int> digits;
    int k = 0;
    while (digits.size()!=10) {
        int tmp = n * ++k;
        while (tmp) {
            digits.insert(tmp%10);
            tmp /= 10;
        }
    }
    return k;
}

int main(int argc, char *argv[]) {

    ifstream in;
    ofstream out;
    in.open("C:\\Users\\Administrator\\Desktop\\MAD\\A-small-attempt0.in");
    out.open("C:\\Users\\Administrator\\Desktop\\MAD\\out.txt");

    int cases;
    in>>cases;
    for (int i=1; i<=cases; i++) {
        int n=0;
        in >> n;
        out<<"Case #"<<i<<": ";
        if (n==0)
            out << "INSOMNIA";
        else
            out << n*solve(n);
        out<<endl;
    }
    in.close();
    out.close();

    return 0;
}
