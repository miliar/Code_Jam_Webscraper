#include <iostream>
#include <fstream>
#include <string.h>
#include <map>
#include <vector>
#include <cmath>
#include <list>
#include <string>
#include <sstream>
#include <algorithm>

using namespace std;


const char *numbers[] = {
    "ZERO",
    "ONE",
    "TWO",
    "THREE",
    "FOUR",
    "FIVE",
    "SIX",
    "SEVEN",
    "EIGHT",
    "NINE"
};


char mapc(string s){
        if("ZERO" == s) return '0';
        if("ONE" == s) return '1';
        if("TWO" == s) return '2';
        if("THREE" == s) return '3';
        if("FOUR" == s) return '4';
        if("FIVE" == s) return '5';
        if("SIX" == s) return '6';
        if("SEVEN" == s) return '7';
        if("EIGHT" == s) return '8';
        if("NINE" == s) return '9';
    return 'E';
}

bool find(string digit, string &number){
    string tmp = number;

//    cout << number << " " << digit << endl;

    for(int i=0; i<digit.size(); i++){
        int found = -1;
        for(int j=0; j < tmp.size(); j++){
            if(digit[i] == tmp[j]){
                found = j;
//                cout << found << endl;
                break;
            }
        }
        if(found < 0){
//            cout << "Not found " << digit[i] << endl;
            return false;
        }
        tmp.erase(found,1);
    }
    number = tmp;
    return true;
}


int main(int argc, char **argv){
    istream &in  = (argc>1)?*(new ifstream(argv[1])):cin;
    ostream &out = (argc>2)?*(new ofstream(argv[2])):cout;

    int T;
    in >> T;

    for(int i=1; i<=T; i++){
        vector<string> phonenumber;
        string s;
        in >> s;

//        cout << s << endl;

        // go over each number
        string res;
        int b = 0;
        string tmp = s;
        do{
            tmp = s;
            phonenumber.clear();
//            for(int j=b; j<10 && tmp.size(); j++){
            int k = b;
            bool working = true;
            int lastfound = -1;
            while(tmp.size() && working){
                int j = k++%10;
                if(find(numbers[j], tmp)){
                    phonenumber.push_back(numbers[j]);
                    lastfound = k;
                }
                if(k-lastfound>10)
                    working = false;

            }
//            for(auto n: phonenumber){
//                cout << (mapc(n));
//            }
//            cout << endl;
            b++;
        }while(tmp.size());

//        if(tmp.size()) cout << "EROROROROROROROOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO";


        for(auto n: phonenumber){
            res.push_back(mapc(n));
        }

        sort(res.begin(), res.end());

        out << "Case #" << i  << ": " << res << endl;

    }

    return 0;
}
