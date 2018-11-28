#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>

#include <algorithm>
#include <iostream>
#include <set>
#include <map>
#include <vector>
#include <string>

using namespace std;

int tc;
string str;

int cnt[26];
int digits[10];

string dstr[10] = { "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE" };
int priority[10][2] = { {0, 'Z'}, {2, 'W'}, {6, 'X'}, {8, 'G'}, {3, 'H'}, {4, 'U'}, {5, 'F'}, {7, 'V'}, {1, 'O'}, {9, 'N'}};

int main()
{
    cin >> tc;
    
    
    
    for (int tt=1; tt<=tc; tt++) {
        cin >> str;
        
        memset(cnt, 0, sizeof(cnt));
        memset(digits, 0, sizeof(digits));
        
        for (int i=0; i<str.length(); i++)
            cnt[str[i] - 'A']++;
        
        for (int d=0; d<10; d++) {
            while (cnt[priority[d][1] - 'A'] > 0) {
                string &s = dstr[priority[d][0]];
                digits[priority[d][0]]++;
                for (int i=0; i<s.length(); i++)
                    cnt[s[i] - 'A']--;
            }
        }
        
        string result = "";
        for (int i=0; i<10; i++)
            for (int j=0; j<digits[i]; j++)
                result += '0' + i;
        
        cout << "Case #" << tt << ": " << result << endl;
    }
    
    return 0;
}