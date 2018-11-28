/* 
 * File:   main.cpp
 * Author: watcharin
 *
 * Created on April 9, 2015, 3:21 PM
 */

#include <stdio.h>

#include <cstdlib>
#include <fstream>

#include <iomanip>
#include <iostream>

#include <sstream>
#include <string>
#include <vector>

using namespace std;

string **dp;

string mul(string a, string b) {
    string minus("-");
    
    if (a[0] == '-') {
        string x = mul(a.substr(1), b);
        
        if (x[0] == '-') {
            return x.substr(1);
        }
        else {
            return minus + x;
        }
    }
    
    if (b[0] == '-') {
        string x = mul(a, b.substr(1));
        
        if (x[0] == '-') {
            return x.substr(1);
        }
        else {
            return minus + x;
        }
    }
    
    if (a.compare("1") == 0) {
        return b;
    }
    else if (b.compare("1") == 0) {
        return a;
    }
    else if (a.compare(b) == 0) {
        return "-1";
    }
    else if (a.compare("i") == 0) {
        if (b.compare("j") == 0) {
            return "k";
        }
        else {
            return "-j";
        }
    }
    else if (a.compare("j") == 0) {
        if (b.compare("i") == 0) {
            return "-k";
        }
        else {
            return "i";
        }
    }
    else {
        if (b.compare("i") == 0) {
            return "j";
        }
        else {
            return "-i";
        }
    }
}

string mul(vector<string> v) {
    string x("1");
    
    for (int i = 0, n = v.size(); i < n; i++) {
        x = mul(x, v[i]);
    }
    
    return x;
}

bool has_sign(string s) {
    return s[0] == '-';
}

char fam(string s) {    
    if (has_sign(s)) {
        s = s.substr(1);
    }
    
    return s[0];
}

string neg(string s) {
    if (has_sign(s)) {
        return s.substr(1);
    }
    
    string y("-");
    y.push_back(s[0]);
    
    return y;
}

string pow(string s, int exp) {
    bool sign = has_sign(s);
    char family = fam(s);
    
    if (family == '1') {
        if (sign) {
            if (exp % 2 == 0) {
                return "1";
            }
            else {
                return "-1";
            }
        }
        else {
            return "1";
        }
    }
    else {
        string x;
        string y;
        
        x.push_back(family);
        y.push_back('-');
        y.push_back(family);
        
        string pattern[4] = { "1", x, "-1", y };
        string base = pattern[exp % 4];
        
        if (sign && exp % 2 == 1) {
            return neg(base);
        }
        else {
            return base;
        }
    }
}

string div(string y, string x) {
    char fy = fam(y);
    char fx = fam(x);
    char fr;
    bool sx = has_sign(x);
    bool sy = has_sign(y);
    bool sr;
    
    if (fy == '1') {       
        if (fx == '1') {
            if ((sx && sy) || (!sx && !sy)) {
                return "1";
            }
            else {
                return "-1";
            }
        }
        else if (fx == 'i') {
            if ((sx && sy) || (!sx && !sy)) {
                return "-i";
            }
            else {
                return "i";
            }
        }
        else if (fx == 'j') {
            if ((sx && sy) || (!sx && !sy)) {
                return "-j";
            }
            else {
                return "j";
            }
        }
        else if (fx == 'k') {
            if ((sx && sy) || (!sx && !sy)) {
                return "-k";
            }
            else {
                return "k";
            }
        }
    }
    else if (fy == 'i') {
        if (fx == '1') {
            if ((sx && sy) || (!sx && !sy)) {
                return "i";
            }
            else {
                return "-i";
            }
        }
        else if (fx == 'i') {
            if ((sx && sy) || (!sx && !sy)) {
                return "1";
            }
            else {
                return "-1";
            }
        }
        else if (fx == 'j') {
            if ((sx && sy) || (!sx && !sy)) {
                return "k";
            }
            else {
                return "-k";
            }
        }
        else if (fx == 'k') {
            if ((sx && sy) || (!sx && !sy)) {
                return "-j";
            }
            else {
                return "j";
            }
        }
    }
    else if (fy == 'j') {
        if (fx == '1') {
            if ((sx && sy) || (!sx && !sy)) {
                return "j";
            }
            else {
                return "-j";
            }
        }
        else if (fx == 'i') {
            if ((sx && sy) || (!sx && !sy)) {
                return "-k";
            }
            else {
                return "k";
            }
        }
        else if (fx == 'j') {
            if ((sx && sy) || (!sx && !sy)) {
                return "1";
            }
            else {
                return "-1";
            }
        }
        else if (fx == 'k') {
            if ((sx && sy) || (!sx && !sy)) {
                return "i";
            }
            else {
                return "-i";
            }
        }
    }
    else if (fy == 'k') {
        if (fx == '1') {
            if ((sx && sy) || (!sx && !sy)) {
                return "k";
            }
            else {
                return "-k";
            }
        }
        else if (fx == 'i') {
            if ((sx && sy) || (!sx && !sy)) {
                return "j";
            }
            else {
                return "-j";
            }
        }
        else if (fx == 'j') {
            if ((sx && sy) || (!sx && !sy)) {
                return "-i";
            }
            else {
                return "i";
            }
        }
        else if (fx == 'k') {
            if ((sx && sy) || (!sx && !sy)) {
                return "1";
            }
            else {
                return "-1";
            }
        }
    }
}

string solve(vector<string> ans, int x) {
    int n = ans.size();
    
    string unit = mul(ans);
    
    string whole = pow(unit, x);
    if (whole.compare("-1") != 0) {
        return "NO";
    }
    
    string *partial_left = new string[n];
    string *partial_right = new string[n];
    partial_left[0] = ans[0];
    partial_right[0] = div(unit, ans[0]);
    
    for (int i = 1; i < n; i++) {
        partial_left[i] = mul(partial_left[i - 1], ans[i]);
        partial_right[i] = div(unit, partial_left[i]);
    }
    
    vector<int> possible_mod_i, possible_mod_k;
    vector<int> possible_part_i, possible_part_k;
    
    // Find i part.
    for (int i = 0; i < 4; i++) {
        string pre = pow(unit, i);
        
        for (int j = 0; j < n; j++) {
            string part = pre;
            
            if (j > 0) {
                part = mul(pre, partial_left[j - 1]);
            }
            
            if (part.compare("i") == 0) {
                possible_mod_i.push_back(i);
                possible_part_i.push_back(j);
            }
        }
    }
    
    // Find k part.
    for (int i = 0; i < 4; i++) {
        string pre = pow(unit, i);
        
        for (int j = 0; j < n; j++) {
            string part = pre;
            
            if (j > 0) {
                part = mul(partial_right[n - j - 1], pre);
            }
            
            if (part.compare("k") == 0) {
                possible_mod_k.push_back(i);
                possible_part_k.push_back(j);
            }
        }
    }
    
    for (int i = 0, p = possible_mod_i.size(); i < p; i++) {
        int mod_i = possible_mod_i[i];
        
        if (mod_i <= x) {
            for (int j = 0, m = possible_mod_k.size(); j < m; j++) {
                int mod_k = possible_mod_k[j];
                
                if (mod_i + mod_k <= x) {
                    int remaining = x - mod_i - mod_k;
                    
                    if (remaining > 0) {
                        if (possible_part_i[i] > 0)
                            remaining--;

                        if (possible_part_k[j] > 0)
                            remaining--;

                        if (remaining > 0 || possible_part_i[i] + possible_part_k[j] <= n) {
//                            vector<string> first_part, middle_part, last_part;
//
//                            for (int k = 0; k < mod_i; k++) {
//                                for (int m = 0; m < n; m++) {
//                                    first_part.push_back(ans[m]);
//                                }
//                            }
//                            for (int k = 0; k < possible_part_i[i]; k++) {
//                                first_part.push_back(ans[k]);
//                            }
//
//                            for (int k = 0; k < possible_part_k[j]; k++) {
//                                last_part.push_back(ans[n - possible_part_k[j] + k]);
//                            }
//                            for (int k = 0; k < mod_k; k++) {
//                                for (int m = 0; m < n; m++) {
//                                    last_part.push_back(ans[m]);
//                                }
//                            }
//
//                            int end = n;
//                            if (remaining < 0) {
//                                end = n - possible_part_k[j];
//                            }
//                            if (possible_part_i[i] > 0) {
//                                for (int k = possible_part_i[i]; k < end; k++) {
//                                    middle_part.push_back(ans[k]);
//                                }
//                            }
//                            for (int k = 0; k < remaining; k++) {
//                                for (int m = 0; m < n; m++) {
//                                    middle_part.push_back(ans[m]);
//                                }
//                            }
//                            if (remaining >= 0 && possible_part_k[j] > 0) {
//                                for (int k = 0; k < n - possible_part_k[j]; k++) {
//                                    middle_part.push_back(ans[k]);
//                                }
//                            }
//
//                            cout << "Verification: " << mul(first_part) << ", " << mul(middle_part) << ", " << mul(last_part) << " mod: " << mod_i << ", " << mod_k << endl;

                            return "YES";
                        }
                    }
                }
            }
        }
    }
    
    delete[] partial_left;
    delete[] partial_right;
    
    return "NO";
}

/*
 * 
 */
int main(int argc, char** argv) {
    char in_file_name[256];
    char out_file_name[256];
    
    sprintf(in_file_name, "%s.in", argv[1]);
    sprintf(out_file_name, "%s.out", argv[1]);
    
    ifstream infile(in_file_name);
    ofstream outfile(out_file_name);
    string line;
    
    getline(infile, line);
    istringstream iss(line);
    int cases;
    
    iss >> cases;
    
    dp = new string*[10000];
    
    for (int i = 0; i < 10000; i++) {
        dp[i] = new string[10000];
    }
    
    for (int i = 0; i < cases; i++) {
        getline(infile, line);
        int l, x;
        
        istringstream iss(line);
        iss >> l >> x;
        
        vector<string> ans;
        getline(infile, line);

        for (char c : line) {
            string y;

            if (c == 'i' || c == 'j' || c == 'k') {
                y.push_back(c);

                ans.push_back(y);
            }
        }
        
        string rv = solve(ans, x);
        
        outfile << "Case #" << (i + 1) << ": " << rv << endl;
    }
    
    for (int i = 0; i < 10000; i++) {
        delete[] dp[i];
    }
    
    return 0;
}
