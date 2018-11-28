#include <iostream>
using namespace std;
int main()
{
    int T;
    cin >> T;
    for(int i = 1 ; i <= T ; i++) {
        string in;
        cin >> in;
        if(in.size() == 1) {
            if(in == "+") {
                cout << "Case #" << i << ": 0" << endl;
            }else if(in == "-") {
                cout << "Case #" << i << ": 1" << endl;
            }else {
                cerr << "ERROR" << endl;
            }
            continue;
        }
        const char * cstr = in.c_str();
        const char start = *cstr;
        int count = 0;
        ++cstr;
        while(*cstr != '\0') {
            char prev = *(cstr-1);
            if(prev != *cstr) {
                count++;
            }
            cstr++;
        }
        const char last = *(cstr-1);
        if(last == '-') {
            count++;
        }

        cout << "Case #" << i << ": " << count << endl;
    }
}
