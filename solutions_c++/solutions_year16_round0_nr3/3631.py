#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <cmath>
#include <bitset>

using namespace std;

long long div[11];

long long convertBase(string str, int base) {
    long long sum = 0;
    for (long i=0; i<str.length(); i++) {
        sum = sum*base +  (str[i]-'0');
    }
    return sum;
}

bool isPrime(long long num, int base) {
    long long upper = sqrt(num)+0.5;
    for (long i=2; i<=upper; i++) {
        if (num%i==0 && i!=1 && num!=i) {
            div[base] = i;
            return false;
        }
    }
    return true;
}

bool isJam(string str) {
    if (str[0] != '1' || str[str.length()-1] != '1') return false;
    for (int i=2; i<=10; i++) {
        if (isPrime(convertBase(str, i), i )) {
            return false;;
        }
    }
    return true;
}

string gen(string ch, int k) {
    string str = "";
    while (k--) str+=ch;
    return str;
}

string next(string str, int len) {
    string nstr = "";
    int add = 1;
    for (int i=str.length()-1; i>=0; i--) {
        nstr = (char)(((str[i]-'0'+add)%2)+'0') + nstr;
        add = (str[i]-'0'+add)/2;
    }
    return nstr;
}

void solve(int N, int J, ofstream & out) {
    string str = "1" + gen("0", N-2) +"1";
    while (J) {
        if (isJam(str)) {
            J--;
            out << str << " ";
            cout <<str<<endl;
            for (int i=2; i<=10; i++) {
                //if (convertBase(str,i)%div[i])
                    //out<<convertBase(str,i)<<", "<<div[i]<<", "<<(convertBase(str,i)%div[i])<<endl;
                out << div[i] << " ";
            }
            out << endl;
        }
        str = next(str,0);
        //cout<<str<<endl;
    }
    return;
}

int main(int argc, char *argv[]) {

    ifstream in;
    ofstream out;
    in.open("C:\\Users\\Administrator\\Desktop\\MAD\\C-small-attempt2.in");
    out.open("C:\\Users\\Administrator\\Desktop\\MAD\\out.txt");

    int cases;
    in>>cases;
    for (int i=1; i<=cases; i++) {
        int N, J;
        in >> N >> J;
        out<<"Case #"<<i<<":"<<endl;
        solve(N, J, out);
        //out<<endl;
    }
    in.close();
    out.close();

    return 0;
}
