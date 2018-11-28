#include <iostream>
#include <vector>
#include <string>
#include <fstream>

using namespace std;

ifstream in("A-large.in");
ofstream out("out.out");

int main(){
    int t;
    in >> t;
    string s;
    int k, n;
    for (int i = 0; i < t; i++){
        in >> s >> k;
        n = s.size();
        int res = 0;
        for (int j = 0; j < n - k + 1; j++){
            if (s[j] == '-'){
                for (int ii = j; ii < j + k; ii++){
                    if (s[ii] == '-'){
                        s[ii] = '+';
                    }
                    else {
                        s[ii] = '-';
                    }
                }
                res++;
            }
        }
        bool can = true;
        for (int j = n - k + 1; j < n && can; j++){
            if (s[j] == '-'){
                can = false;
            }
        }
        if (can){
            out << "Case #" << i + 1 << ": " << res << endl;
        }
        else {
            out << "Case #" << i + 1 << ": IMPOSSIBLE" << endl;
        }
    }
}
