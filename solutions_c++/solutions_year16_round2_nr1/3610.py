#include <vector>
#include <string>
#include <iostream>
#include <fstream>
#include <cstdio>
#include <cstdlib>

using namespace std;

char uniq[10] = {0};
string representation[10] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};

bool do_remove(int x, string s, string& new_s) {
    new_s = s;
    for (int i(0); i<representation[x].size(); i++) {
        bool flag = false;
        for (int j(0); j<new_s.size(); j++) {
            if (new_s[j] == representation[x][i]) {
                new_s.erase(j, 1);
                flag = true;
                break;
            }
        }
        if (!flag) {
            return false;
        }
    }
    return true;
}


int do_try(int j, string s, string& result) {
    if (s.size() == 0) {
        return 1;
    }
    
    string new_s;
    if (uniq[j]) {
        if (s.find(uniq[j]) != string::npos) {
            if (!do_remove(j, s, new_s)) {
                return 0;
            }
        }
        else {
            return 0;
        }
    }
    else {
        if (!do_remove(j, s, new_s)) {
            return 0;
        }
    }
    
    int flag = 0;
    
    for (int i = j; i < 10; i++) {
        result += to_string(i);
        flag = do_try(i, new_s, result);
        if (flag) {
            break;
        }
        result.pop_back();
    }
    return flag;
}

int main() {
    ifstream fi("a.in");
    ofstream fo("a.out");
    
    int t;
    fi >> t;
    
    
    uniq[0] = 'Z';
    uniq[2] = 'W';
    uniq[6] = 'X';
    uniq[8] = 'G';
    

    for (int i(0); i<t; i++) {
        string s;
        fi >> s;
        
        string result = "";

        for (int j(0); j<10; j++) {
            result += to_string(j);
            if (do_try(j, s, result)) {
                break;
            }
            result.pop_back();
        }
        result.pop_back();
        fo << "Case #" << i+1 << ": " << result << endl;
    }
    
    
    fi.close();
    fo.close();
    
    return 0;
}