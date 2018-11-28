#include <iostream>
#include <string>
#include <cstring>

using namespace std;

bool is_nval_subtring(string &name, int start, int len, int n) {
    int max_n =0;
    for(int i=start; i<(start+len); i++) {
        switch(name[i]) {
            case 'a':
            case 'e':
            case 'i':
            case 'o':
            case 'u':
                max_n=0;
                break;

            default:
                max_n++;
                if(max_n>=n) {
                    return true;
                }
                break;
        }
    }

    return false;
}

int main() {

    int T;

    cin >> T;

    for(int z=1; z<=T; z++) {
        string name;
        int n, len;
        int nval = 0;

        cin >> name >> n;
        //cout << "Input: " << name << " " << n << endl;
        len = name.length();

        for(int i=0; i<len; i++) {
            for(int j=1; j<=len-i; j++) {
                //cout << i << " " << j << " ";
                if(is_nval_subtring(name, i, j, n)) {
                    nval++;
                    //cout << "true" << endl;
                } else {
                    //cout << "false" << endl;
                }
            }
        }

        cout << "Case #" << z << ": ";
        cout << nval << endl;
    }

    return 1;
}
