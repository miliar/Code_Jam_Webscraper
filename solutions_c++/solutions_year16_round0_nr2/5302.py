#include<iostream>
#include<string>
#include<cmath>

using namespace std;

void flip (string& str, int n) {
    char c;
    for (int i=0; i<ceil(n/2.); ++i) {
        c = str[i];
        str[i] = (str[n-i-1] == '+') ? '-' : '+';
        str[n-i-1] = (c == '+') ? '-' : '+';
    }
}

bool good (string& str) {
    return str.find('-') == -1;
}

int main(){
    int tmax, cnt;
    int first0, last0;
    string str;
    cin >> tmax;
    for (int t=1; t<=tmax; ++t) {
        cin >> str;
        cnt = 0;
        while (!good(str)) {
            first0 = str.find_first_of('-');
            last0 = str.find_last_of('-') + 1;
            if (first0 > 0) {
                flip(str, first0);
                ++cnt;
            }
            if (last0 > 0) {
                flip(str, last0);
                ++cnt;
            }
        }
        cout << "Case #" << t << ": " << cnt << endl;
    }
    return 0;
}
