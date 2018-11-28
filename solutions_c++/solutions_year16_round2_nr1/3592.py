/*
 ID: jonnyko1
 PROG: milk2
 LANG: C++11
*/

#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <stack>
#include <unordered_map>
#include <limits.h>
#include <time.h>
#include <queue>
#include <fstream>
#include <set>
#include <time.h>
using namespace std;

#define RELEASE 1

vector<string> table{"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};

void dfs(vector<int> & remain, vector<int> & number) throw(int) {
    bool end_out = 1;
    for(int i = 0; i < remain.size(); ++i){
        if(remain[i]){
            end_out = 0;
            break;
        }
    }
    if(end_out){
        throw 0;
    }
    for(int i = 0; i < 10; ++i){
        string str = table[i];
        end_out = 0;
        for(int i = 0; i < str.length(); ++i){
            --remain[str[i] - 'A'];
            if(remain[str[i] - 'A'] < 0){
                end_out = 1;
            }
        }
        if(end_out){
            for(int i = 0; i < str.length(); ++i){
                ++remain[str[i] - 'A'];
            }
            continue;
        }
        ++number[i];
        dfs(remain, number);
        for(int i = 0; i < str.length(); ++i){
            ++remain[str[i] - 'A'];
        }
        --number[i];
    }
}

int main(){
#if RELEASE
    freopen("/Users/jonnykong/Downloads/A-small-attempt0.in.txt", "r", stdin);
    freopen("/Users/jonnykong/Desktop/outPut.txt", "w", stdout);
#endif
    int T; cin >> T;
    for(int z = 0; z < T; ++z){
        cout << "Case #" << z + 1 << ": ";
        string str; cin >> str;
        int length = str.length();
        vector<int> digits(26);
        vector<int> number(10);
        for(int i = 0; i < length; ++i){
            ++digits[str[i] - 'A'];
        }
        //for_each(digits.begin(), digits.end(), [](int & a){ cout << ' ' << a; }); cout << endl;
        try{
            dfs(digits, number);
        }
        catch(int a) {}
        for(int i = 0; i < 10; ++i){
            for(int j = 0; j < number[i]; ++j){
                cout << i;
            }
        }
        cout << endl;
    }
    return 0;
}





