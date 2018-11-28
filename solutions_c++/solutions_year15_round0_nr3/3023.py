//
//  main.cpp
//  CodeJame2015_3_CPP
//
//  Created by Nataphol Baramichai on 4/11/2558 BE.
//  Copyright (c) 2558 krabrr. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <iterator>
#include <string>
#include <vector>
#include <stdio.h>

using namespace std;

string multiply(string a, string b) {
    string c = "";
    bool minus = false;
    if (a[0] == '-') {
        minus = !minus;
        a = a.substr(1);
    }
    if (b[0] == '-') {
        minus = !minus;
        b = b.substr(1);
    }
    
    if (a == "i") {
        if (b == "i") {
            minus = !minus;
        }
        else if (b == "j") {
            c = "k";
        }
        else if (b == "k") {
            minus = !minus;
            c = "j";
        }
    }
    else if (a == "j") {
        if (b == "i") {
            minus = !minus;
            c = "k";
        }
        else if (b == "j") {
            minus = !minus;
        }
        else if (b == "k") {
            c = "i";
        }
    }
    else if (a == "k") {
        if (b == "i") {
            c = "j";
        }
        else if (b == "j") {
            minus = !minus;
            c = "i";
        }
        else if (b == "k") {
            minus = !minus;
        }
    }
    
    if (minus)
        c = "-" + c;

    return c;
}

string decode(string str) {
    int idx  = 0;
    vector<string> s_arr;
    unsigned long len = str.size();
    if (len == 0)
        return str;
    for (int i = 0; i < len; i++) {
        char c = str[i];
        if (c == '-')
            continue;
        string t_str = "";
        t_str.push_back(c);
        if (i != 0 && str[i-1] == '-')
            t_str.insert(t_str.begin(), '-');
        
        s_arr.push_back(t_str);
        
        if (s_arr.size() == 2) {
            idx = i+1;
            break;
        }
    }
    
    if (s_arr.size() != 2)
        return str;

    str = str.substr(idx, str.size());
    string c = multiply(s_arr[0], s_arr[1]);
    str = c + str;
    return str;
}

string solve(int num_char, int num_repeat, string str) {
    //printf("num_char: %d num_repeat: %d, str: %s\n", num_char, num_repeat, str.c_str());
    if (str.size() == 1)
        return "NO";
    if (str == "ijk")
        return "YES";
    
    string tok = str;
    for (int i = 1; i < num_repeat; i++)
        str += tok;
    
    string ans = "";
    
    while (true) {
        //cout << "str: " << str << "\n";
        string tmp = decode(str);
        //cout << "decode str: " << tmp << "\n";
        if (tmp == str)
            break;
        str = tmp;
        if (str == "")
            break;
        if (ans == "") {
            if (str[0] == 'i') {
                ans = "i";
                str = str.substr(1);
            }
        }
        else if (ans == "i") {
            if (str[0] == 'j') {
                ans = "ij";
                str = str.substr(1);
            }
        }
    }
    
    str = ans + str;
    cout << "str: " << str << "\n";
    if (str == "ijk")
        return "YES";
    else
        return "NO";
}

int main() {
    string line;
    //ifstream input ("test_input.txt");
    ifstream input ("C-small-attempt2.in.txt");

    ofstream output ("output.txt");
    
    if (input.is_open()) {
        
        getline(input, line);
        int num_case = stoi(line);
        int caseIdx = 1;
        
        while (getline(input, line)) {
            vector <string> s_arr;
            istringstream iss(line);
            copy(istream_iterator<string>(iss),
                 istream_iterator<string>(),
                 back_inserter(s_arr));
            
            int num_char = stoi(s_arr[0]);
            int num_repeat = stoi(s_arr[1]);
            
            getline(input, line);
            string str = line;
            
            string result = solve(num_char, num_repeat, str);
            
            result = "Case #" + to_string(caseIdx) + ": " + result + "\n";
            
            if (output.is_open()) {
                output << result;
            }
            
            caseIdx++;
        }
        input.close();
        output.close();
    }
    else {
        cout << "Unable to open file";
    }
    return 0;
}
