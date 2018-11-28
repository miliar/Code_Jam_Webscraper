#include <bits/stdc++.h>
using namespace std;

int T, len;
char izq, der;
string s;

int main()
{
    ifstream cin("B-large.in");
    ofstream cout("out_B1_large.txt");
    cin >> T;
    for(int t=1; t<=T; t++){
        cin >> s;
        len = s.length();
        int cont = 0;
        for(int i=0; i<s.length()-1; i++){
            if(s[i] != s[i+1]) cont++;
        }
        if(s[len-1] == '-') cont++;

        cout << "Case #" << t << ": " << cont << "\n";

    }
    return 0;
}
