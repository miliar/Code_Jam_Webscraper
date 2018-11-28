#include <iostream>
#include <string>

using namespace std;

bool parse(unsigned int n, bool (&digits)[10]) {
    while (n>0) {
        digits[n%10] = true;
        n = n/10;
    }
    for (int i=0; i<10; ++i)
        if (digits[i] == false) return false;
    return true;
}



string count(unsigned int n) {
    if (n == 0) return "INSOMNIA";
    int curr = n;
    bool digits[10] = { false } ;

    while (true) {
        if( parse(curr,digits) ) return to_string(curr);
        curr += n;
    }
}

int main(int argc, char * argv[]) {
    unsigned int t;
    cin >> t;

    for (int i=1; i<=t; ++i) {
        unsigned int n;
        cin >> n;
        cout << "Case #" << i << ": " << count(n) << endl;
    }

    return 0;
}
