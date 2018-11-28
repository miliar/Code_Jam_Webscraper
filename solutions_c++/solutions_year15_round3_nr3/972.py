/* 
 * File:   main.cpp
 * Author: watcharin
 *
 * Created on April 12, 2015, 3:30 AM
 */

#include <stdio.h>

#include <cstdlib>

#include <algorithm>
#include <fstream>

#include <iomanip>
#include <iostream>

#include <queue>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

// Type definitions
typedef unsigned int uint;
typedef long long int ll_int;
typedef vector<int>::const_iterator int_const_itr;

//== Vector operations ==
template<typename T> T max(vector<T>& v) {
    T rv = *max_element(v.begin(), v.end());
    
    return rv;
}

template<typename T> vector<T>& sort_asc(vector<T>& v) {
    sort(v.begin(), v.end());
    
    return v;
}

template<typename T> vector<T>& sort_desc(vector<T>& v) {
    sort(v.begin(), v.end(), greater<T>());
    
    return v;
}
//== Vector operations ==

//== String Manipulation ==
bool equals(string& s, const char *t) {
    return s.compare(string(t)) == 0;
}

bool equals(string& s, string& t) {
    return s.compare(t) == 0;
}

template<typename T> T parse(string& s) {
    istringstream iss(s);
    T x;
    
    iss >> x;
    
    return x;
}

template<typename T> vector<T> parse_array(string& s) {
    vector<T> v;
    istringstream iss(s);
    string item;
    
    while (getline(iss, item, ' ')) {
        v.push_back(parse<T>(item));
    }
    
    return v;
}

string trim(string s) {
    int cnt = 0;
    
    for (string::size_type i = 0; i < s.length(); i++) {
        if (s[i] == ' ' || s[i] == '\t' || s[i] == '\r' || s[i] == '\n') {
            cnt++;
        }
        else {
            break;
        }
    }
    
    if (cnt > 0)
        s.erase(0, cnt);
    
    cnt = 0;
    
    for (string::size_type i = s.length() - 1; i >= 0; i--) {
        if (s[i] == ' ' || s[i] == '\t' || s[i] == '\r' || s[i] == '\n') {
            cnt++;
        }
        else {
            break;
        }
    }
    
    if (cnt > 0)
        s.erase(s.length() - cnt, cnt);
    
    return s;
}
//== String Manipulation ==

//== File reader ==
template<typename T> T read(ifstream& infile) {
    string line;
    getline(infile, line);
    
    return parse<T>(line);
}

template<typename T> vector<T> read_array(ifstream& infile) {
    string line;
    getline(infile, line);
    
    return parse_array<T>(line);
}
//== File reader ==

int solve(int c, vector<int> d, int lim) {
    int dp[100][101];
    
    for (int i = 0; i < 100; i++) {
        for (int j = 0; j < 101; j++) {
            dp[i][j] = 0;
        }
    }
    
    int n = d.size();
    
    for (int i = 0; i < n; i++) {
        for (int j = 1; j <= c; j++) {
            if (i == 0 && j == 1) {
                dp[0][1] = d[0] > 1 ? 0 : d[0];
            }
            else if (j == 1) {
                dp[i][1] = dp[i - 1][1];
                
                if (dp[i][1] + 1 >= d[i]) {
                    dp[i][1] = d[i] + dp[i - 1][1];
                }
            }
            else {
                int old = dp[i][j];
                
                dp[i][j] = dp[i][j - 1] + dp[i][1];
                
                if ((dp[i][j] + 1) % d[i] == 0) {
                    dp[i][j] = d[i] * j;
                }
                
                if (dp[i][j] >= lim) {
                    return 0;
                }
                
                if (old == dp[i][j]) {
                    d.push_back(old + 1);
                    
                    return 1 + solve(c, sort_asc<int>(d), lim);
                }
            }
            
            if (dp[i][j] >= lim) {
                return 0;
            }
        }
    }
    
    if (dp[n - 1][c] < lim) {
        d.push_back(dp[n - 1][c] + 1);
        
        return 1 + solve(c, sort_asc<int>(d), lim);
    }
    
    return 0;
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
    
    int cases = read<int>(infile);
    
    for (int i = 0; i < cases; i++) {
        vector<int> v = read_array<int>(infile);
        int c = v[0], lim = v[2];
        
        vector<int> d = read_array<int>(infile);
        
        cout << "Solving Case " << (i + 1) << " ..." << endl;
        int rv = solve(c, d, lim);
        cout << "Solving Case " << (i + 1) << " ... OK" << endl;
        
        outfile << "Case #" << (i + 1) << ": " << rv << endl;
    }
    
    return 0;
}
