//
//  main.cpp
//  ProblemOne
//
//  Created by Matt Slater on 5/12/13.
//  Copyright (c) 2013 OzS. All rights reserved.
//

#include <iostream>
#include <unordered_set>
#include <string>
#include <vector>

using namespace std;

int test = 0;
int i, j;

const char v[] = {'a', 'e', 'i', 'o', 'u'};


static bool is_vovel(const char c) {
    if (c == v[0] || c == v[1] || c == v[2] || c == v[3] || c == v[4]) {
        return true;
    }
    
    return false;
}


static void solve()
{
    cout<< "Case #" << ++test << ": ";
    
    string name; int N; cin >> name >> N;
    
    unsigned long len = name.length();
    
    //unordered_set<string> set;
    vector<string> names;
    
    for (i=0; i < len; i++) {
        string s = name.substr();
        for (j = N; j <= len - i; j++) {
            string s = name.substr(i, j);
            //names.emplace(s);
            names.push_back(s);
            //cout << s << endl;
        }
    }
    
    int res = 0;
    for (const string &str: names) {
        int count = 0;
        //for (i = 0; i < str.length() && N >= str.length() - i + count; i++) {
        for (i = 0; i < str.length() && N - count <= str.length() - i; i++) {
            if (!is_vovel(str[i])) {
                count++;
            } else {
                count = 0;
            }
            
            if (count == N) {
                res++;
                //cout << str << endl;
                break;
            }
        }
    }
    
    cout << res << endl;
}

int main(int argc, const char * argv[])
{

    int t = 1;
    cin >> t;
    
    while (t--) {
        solve();
    }
    
}

