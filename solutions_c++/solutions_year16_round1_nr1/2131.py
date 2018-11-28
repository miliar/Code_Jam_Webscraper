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
#include <bitset>
#include <vector>
#include <map>
#include <string>

using namespace std;

void solveD(int k , int c, int s, vector<string> &output) {
    if (k > s) {
        output.push_back("IMPOSSIBLE");
        return;
    }
    if (1 == c) {
        for(int i = 1 ; i <= k ; i++) {
            output.push_back(to_string(i));
        }
        return;
    }
    output.push_back("1");
    for(long long i = 1 ; i < k ; i++) {
        long long unit = pow(k, c-1);
        long long p = i * unit + 1;
        output.push_back(to_string(p));
    }
}

void solveC(map<string, vector<long long>> &anwsers) {
    bitset<16> bs16("1000000000000001");
    bitset<16> bs16_tmp(bs16);
    long long total_pos = pow(2, 14);
    int count = 0;
    for(long long pos = 0 ; pos < total_pos ; pos++) {
        if (count >= 50) {
            return;
        }
        bitset<16> add_bs16(pos);
        bs16_tmp = bs16 | (add_bs16 << 1);
        
        // Check each base for not having prime
        vector<long long> divisors;
        cout << "BitSet : " << bs16_tmp.to_string() << endl;
        for(int base = 2; base <= 10 ; base++) {
            long long val = 0;
            for(int p = 0 ; p < bs16_tmp.size() ; p++) {
                if (bs16_tmp[p]) {
                    long long inc_val = pow(base, p);
                    cout << "Val : " << val << " Inc Val : " << inc_val << endl;
                    val += inc_val;
                }
            }
            cout << "Value : " << val << " Base : " << base << endl;

            bool is_divisor = false;
            for(long long divisor = 2 ; divisor < 1000 ; divisor++) {
                if (divisor > 2 && divisor % 2 == 0) {
                    continue;
                }
                long long rest = val % divisor;
                if (0 == rest) {
                    is_divisor = true;
                    cout << "Divisor : " << divisor << " Rest : " << rest << endl;
                    divisors.push_back(divisor);
                    break;
                }
            }
            if (!is_divisor) {
                break;
            }
        }
        
        // Can find divisor for all base number
        if (9 == divisors.size()) {
            cout << "Coin Jam : " << bs16_tmp.to_string() << endl;
            anwsers.insert(pair<string, vector<long long>> (string(bs16_tmp.to_string()), divisors));
            count++;
        }
    }
}

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
    long long org_val = stoll(t);
    if (0 == org_val) {
        output = "INSOMNIA";
        return;
    }
    long long val = org_val;
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

void solve_roundA_A(string input, string& output) {
    unsigned long s_length = input.size();
    vector<string> last_words(s_length);
    for(long i = 0 ; i < s_length ; i++) {
        string sub_str = input.substr(i,1);
        if (0 == i) {
            last_words[i] = sub_str;
        } else {
            if (last_words[i - 1] < sub_str) {
                last_words[i] = sub_str;
            } else {
                last_words[i] = last_words[i - 1];
            }
        }
        cout << "Last Words i : " << i << " string : " + last_words[i] << endl;
    }
    string last;
    string first;
    for(long i = s_length - 1 ; i >= 0 ; i--) {
        string sub_str = input.substr(i,1);
        if (last_words[i] > sub_str) {
            last = sub_str + last;
            cout << "Put as Last Words i : " << i << " string : " + sub_str << endl;
        } else {
            first = first + sub_str;
            cout << "Put as First Words i : " << i << " string : " + sub_str << endl;
        }
    }
    output = first + last;
}

int main(int argc, const char * argv[]) {
    string file_name = "/Users/jun/Desktop/A-large.in";
    string file_name_out = "/Users/jun/Desktop/A-large.out";
    ifstream ifs(file_name);
    ofstream ofs(file_name_out);
    int case_num;
    ifs >> case_num;
    string str;
    string output;
    for(int i = 0 ; i < case_num ; i++) {
        ifs >> str;
        solve_roundA_A(str, output);
        cout << "Output " << output << endl;
        ofs << "Case #" << i + 1 << ": " << output << endl;
    }
   return 0;
}
