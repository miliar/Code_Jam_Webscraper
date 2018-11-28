#include<iostream>
#include<fstream>
using namespace std;
int main() {
    ifstream in;
    ofstream out;
    in.open("A-large.in.txt");
    out.open("salidaAgrande.txt");
    int t,n;
    int kase = 1;
    string s;
    in >> t;
    while(t--) {
        in >> n;
        in >> s;
        int acum = 0, r = 0;
        for(int i=0;i<s.length();i++) {
            if(s[i] != '0') {
                if(acum < i) {
                    r += (i-acum);
                    acum += (i-acum);
                }
                acum += (s[i]-'0');
            }
        }
        out << "Case #" << kase << ": " <<  r << endl;
        kase++;
        
    }
    
    in.close();
    out.close();
}