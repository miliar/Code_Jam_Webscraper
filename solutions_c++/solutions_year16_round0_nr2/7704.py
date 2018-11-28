#include<iostream>
#include<string>
using namespace std;

bool check(const string& str) {
    for(int i = 0; i < str.size(); ++i) {
        if(str[i] == '-') return true;
    }
    return false;
}

void run() {
    string in;
    cin >> in;
    int n = in.size();
    int cnt = 0;
    while(check(in)) {
        char c = in[0];
        char f = (c == '+') ? '-' : '+';
        int i = 0;
        while(c == in[i]) {
            in[i] = f;
            ++i;
        }
        ++cnt;
    }
    cout << cnt; 
}

int main(int argc, char *argv[]) {
    int T;
    cin >> T;
    for(int i = 1; i <= T; ++i) {
        cout << "Case #" << i << ": ";
        run();
        cout << endl;
    }
    return 0;
}
