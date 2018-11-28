//
//  main.cpp
//  GoogleCodeJam
//
//

#include <iostream>
#include <iostream>
#include <fstream>
#include <math.h>
#include <deque>
using namespace std;

void solveB(string s, string& output) {
    // Normalize first
    string cur_side = "";
    deque<int> side_array;
    cout << "Start solving S : " << s << endl;
    for(int c = 0 ; c < s.size() ; c++) {
        if (cur_side != s.substr(c,1)) {
            cur_side = s.substr(c,1);
            if ("+" == s.substr(c,1)) {
                side_array.push_back(1);
            } else {
                side_array.push_back(0);
            }
            cout << cur_side << endl;
            cout << side_array.back() << endl;
        }
    }
    // Only one type
    if (1 == side_array.size()) {
        if (1 == side_array.front()) {
            output = "0";
        } else {
            output = "1";
        }
        cout << "Necessary flip count : " << output << endl;
        return;
    }

    int count = 0;
    // More than 2 type
    if (1 == side_array.back()) {
        side_array.pop_back();
    }
    if (1 == side_array.front()) {
        side_array.pop_front();
        count++;
    }
    count += side_array.size();
    output = to_string(count);
    cout << "Necessary flip count : " << output << endl;
}

void solveA(string t, string& output) {
    bool flags[10];
    memset(flags, false, 10);
    int org_val = stoi(t);
    if (0 == org_val) {
        output = "INSOMNIA";
        return;
    }
    int val = org_val;
    cout << "Try to solve string : " << t << endl;
    while(true) {
        //update flag
        string val_str = to_string(val);
        for(int c = 0 ; c < val_str.size(); c++) {
            cout << "Var : " << val_str << " , Substring : " << stoi(val_str.substr(c,1)) << endl;
            flags[stoi(val_str.substr(c,1))] = true;
        }
        bool is_all_true = true;
      
        for(int fc = 0 ; fc < 10 ; fc++) {
            if (!flags[fc]){
                is_all_true = false;
            }
        }
        
        if (is_all_true) {
            cout << "Succeed to complete all digit : " << val << endl;
            output = to_string(val);
            return;
        }
        val += org_val;
    }
}

int main(int argc, const char * argv[]) {
    
    string file_name = "/Users/jun/Desktop/B-large.in";
    string file_name_out = "/Users/jun/Desktop/B-large.out";
    ifstream ifs(file_name);
    ofstream ofs(file_name_out);
    int case_num;
    ifs >> case_num;
    
    string t;
    string output;
    for(int i = 0 ; i < case_num ; i++) {
        ifs >> t;
        solveB(t, output);
        ofs << "Case #" << i + 1 << ": " << output << endl;
    }
    
    return 0;
}
