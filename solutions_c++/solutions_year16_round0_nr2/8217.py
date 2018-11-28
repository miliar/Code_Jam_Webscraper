#include<iostream>
#include<string>
using namespace std;

int main()
{
    int ilosc;
    cin >> ilosc;
    for(int n=0;n<ilosc;++n) {
        string s;
        cin >> s;
        bool bylo = false;
        int flips = 0;
        for(int k=s.length()-1;k>0;--k) {
            if(s[k]=='-') {
                   if(s[k-1] =='+') flips += 2;
            }
        }
        if(s[0]=='-') ++ flips;
        cout << "Case #" << n+1 << ": " << flips << endl;
    }
}