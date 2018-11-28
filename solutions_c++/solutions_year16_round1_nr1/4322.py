//
//  main.cpp
//  Google Code Jam
//
//  Created by Vivek Vichare on 4/9/16.
//  Copyright © 2016 Vivandro. All rights reserved.
//

#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <fstream>
#include <sstream>
#include <iomanip>

using namespace std;

typedef long long ll;
typedef vector <ll> vll;
typedef vector<vll> vvll;

typedef unsigned long long ull;
typedef vector <ull> vull;
typedef vector<vull> vvull;

typedef vector <string> vs;
typedef vector<vs> vvs;

void process_testcase_A()
{
    string S;
    cin >> S;
    
    char ch = S[0];
    string word = "";
    word += ch;
    for (int i = 1; i < S.length(); ++i) {
        string w = "";
        w += S[i];
        if (S[i] >= word[0]) {
            word = w + word;
        } else {
            word += w;
        }
    }
    cout << word;
}

void process_testcase_B()
{
    int/*string*/ pancakes;
    cin >> pancakes;
    cout << pancakes << endl;
    
    cin >> pancakes;
    cout << pancakes << endl;

    return;
//    
//    ull flips = 0;
//    char prev = '+';
//    auto rend = pancakes.rend();
//    for (auto i = pancakes.rbegin(); i != rend; ++i) {
//        if (*i != prev) {
//            prev = *i;
//            ++flips;
//        }
//    }
//    cout << flips;
}

void process_testcase_C()
{
    ll N;
    cin >> N;
//    cout << N << endl;
//    for (int i = 0; i < N; ++i) {
//        ll f;
//        cin >> f;
//        cout << f << endl;
//    }
//    
    ll bffs[1003];
    map<ll, set<ll> >fans;
    for (ll i = 0; i <= N; ++i) {
        set<ll>s;
        fans[0]=s;
    }
    
    for (ll i = 0; i < N; ++i) {
        ll f;
        cin >> f;
        bffs[i+1] = f; // <---- NOTE + 1
        fans[f].insert(i+1);
    }
    
    ll circles[1003][1003];
    memset(circles, 0, sizeof(circles));
    
    ll maxKidsInCircle = 0;
    for (ll i = 1; i <= N; ++i) {
        set<ll>seated;
        ll prevKid = i;
        seated.insert(prevKid);
        circles[i][0] = prevKid;
        for (ll kids = 1; kids < N; ++kids) {
            // forward arrow
            ll nextKid = bffs[prevKid];
            if (seated.find(nextKid) == seated.end()) {
                // found a new kid
                //                circles[i][kids] = nextKid;
                //                seated.insert(nextKid);
                //                prevKid = nextKid;
            } else {
                // backward arrow
                for (auto b = fans[prevKid].begin(); b != fans[prevKid].end(); ++b) {
                    nextKid = *b;
                    if (seated.find(nextKid) == seated.end()) {
                        // found a new kid
                        //                        circles[i][kids] = nextKid;
                        //                        seated.insert(nextKid);
                        //                        prevKid = nextKid;
                        break;
                    }
                }
            }
            if (prevKid != nextKid) {
                // found a new kid
                seated.insert(nextKid);
                circles[i][seated.size() - 1] = nextKid;
                prevKid = nextKid;
            } else {
                break;
            }
            
        }
        // check if we can seat another kid to the left of the first one.
        for (auto b = fans[i].begin(); b != fans[prevKid].end(); ++b) {
            ll nextKid = *b;
            if (seated.find(nextKid) == seated.end()) {
                seated.insert(nextKid);
                circles[i][seated.size() - 1] = nextKid;
                break;
            }
        }
        ll kidsInCircle = seated.size();
        if (kidsInCircle >= maxKidsInCircle) {
            cout << "\n New Winner : ";
            for (auto z = 0; z < seated.size(); ++z) {
                cout << " " << circles[i][z] << " ";
            }
            cout << endl;
        }
        maxKidsInCircle = max(maxKidsInCircle, kidsInCircle);
    }
    
    cout << maxKidsInCircle;
}

int main(int argc, char*argv[]) {
    int tc = 0;
    if(argc == 1) {
        freopen("/Users/vivandro/Downloads/inp.txt", "r", stdin);
    }
    else {
        freopen(argv[1], "r", stdin);
    }
    freopen("/Users/vivandro/Downloads/outp.txt", "w", stdout);
    
    // find total number of testcases
    cin >> tc;
    
    // for every testcase
    for(int i = 1; i <= tc; i++)
    {
        printf("Case #%d: ",i);
        process_testcase_A();
        cout << endl;
    }
    
    return 0;
}
