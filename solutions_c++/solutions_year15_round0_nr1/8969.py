#include <iostream>

using namespace std;

void test(int tt) {
    int len;
    cin >> len;
    int stay = 0;int add = 0;
    for(int i = 0; i <= len; i++) {
        char ch;
        cin >> ch;
        if(stay < i) {add += i-stay; stay = i;}
        stay+= ch - '0';
    }
    cout << "Case #" << tt << ": " << add << endl;
}


int main() {
   int tt;
    cin >> tt;
    for(int i = 0; i < tt; ++i) test(i+1);
    return 0;
}