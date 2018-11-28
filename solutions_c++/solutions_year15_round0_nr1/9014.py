#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <stdlib.h>

using namespace std;

int invite(string s, int Smax) {
    int n_persons = 0, ans = 0;
    for(int i = 0; i <= Smax; i++) {
        char buffer[2] = {s[i], '\0'};
        int p = atoi(buffer);
        //cout << p << " ";
        if(p > 0) {
            if(i > n_persons) {
                int inv = i-n_persons;
                ans += inv;
                n_persons += inv;
            }
            n_persons += p;
        }
    }
    //cout << endl;

    return ans;
}

int main(int argc, char **argv) {
    if(argc <= 1) {
        cout << "Input filename not specified" << endl;
        return -1;
    }

    ifstream ifs(argv[1]);
    if(!ifs.is_open()) {
        cout << "Error opening file" << endl;
        return -1;
    }
    
    ofstream ofs("out.txt");

    int T;
    ifs >> T;

    for(int t = 0; t < T; t++) {
        int Smax;
        ifs >> Smax;
        
        string s;
        ifs >> s;
        //cout << "String " << s << endl;

        int ans = invite(s, Smax);
        //cout << "Ans = " << ans << endl << endl;

        ofs << "Case #" << t+1 << ": " << ans << endl;
    }

    ifs.close();
    ofs.close();

    return 0;
}
