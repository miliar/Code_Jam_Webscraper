#include <iostream>
#include <fstream>

using namespace std;

int main() {
    ifstream fi("in");
    ofstream fw("out");

    int T, np;

    fi >> T;
    for(int i=0; i<T ; ++i) {
        string s;
        fi >> s;
        np = s.length();
        int res = 0;
        cout << "start " << s << endl ;
        fw << "Case #" << (i+1) << ": ";
        while(true) {
            int tm = -1;
            int fm = -1;

            for(int i=np-1; i>=0; --i) {
                if(s[i] == '-') {
                    tm = i;
                    break;
                }
            }

            if(tm != -1) {
                res++;
                for(int i=tm; i>=0; i--) {
                    if(s[i] == '-') {
                        s[i] = '+';
                    } else {
                        s[i] = '-';
                    }
                }
                cout << s << endl;
            }

            bool correct = true;
            for(int i=0; i<s.length(); ++i) {
                if(s[i] == '-') {
                    correct = false;
                    break;
                }
            }
            if(correct) break;
        }
        fw << res << endl;

    }


    fw.close();
    fi.close();
    return 0;
}