#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <math.h>
#include <iomanip>
#include <sstream>
#include <set>

using namespace std;

int TC = 1, T;
string S;
int a[26];

int main ()
{
    for (cin >> T; TC <= T; TC++) {
        memset(a, 0, sizeof(a));
        cin >> S;
        for (int i = 0; i < S.length(); i++) {
            a[S[i]-'A']++;
        }
        vector<int> result;
        int mini = a['Z'-'A'];
        mini = min(mini, a['E'-'A']);
        mini = min(mini, a['R'-'A']);
        mini = min(mini, a['O'-'A']);
        for (int i = 0; i < mini; i++) {
            result.push_back(0);
        }
        a['Z'-'A'] -= mini;
        a['E'-'A'] -= mini;
        a['R'-'A'] -= mini;
        a['O'-'A'] -= mini;
        
        mini = a['S'-'A'];
        mini = min(mini, a['I'-'A']);
        mini = min(mini, a['X'-'A']);
        for (int i = 0; i < mini; i++) {
            result.push_back(6);
        }
        a['S'-'A'] -= mini;
        a['I'-'A'] -= mini;
        a['X'-'A'] -= mini;
        
        
        mini = a['S'-'A'];
        mini = min(mini, a['E'-'A']/2);
        mini = min(mini, a['V'-'A']);
        mini = min(mini, a['N'-'A']);
        for (int i = 0; i < mini; i++) {
            result.push_back(7);
        }
        a['S'-'A'] -= mini;
        a['E'-'A'] -= mini*2;
        a['V'-'A'] -= mini;
        a['N'-'A'] -= mini;
        
        mini = a['F'-'A'];
        mini = min(mini, a['I'-'A']);
        mini = min(mini, a['V'-'A']);
        mini = min(mini, a['E'-'A']);
        for (int i = 0; i < mini; i++) {
            result.push_back(5);
        }
        a['F'-'A'] -= mini;
        a['I'-'A'] -= mini;
        a['V'-'A'] -= mini;
        a['E'-'A'] -= mini;
        
        mini = a['F'-'A'];
        mini = min(mini, a['O'-'A']);
        mini = min(mini, a['U'-'A']);
        mini = min(mini, a['R'-'A']);
        for (int i = 0; i < mini; i++) {
            result.push_back(4);
        }
        a['F'-'A'] -= mini;
        a['O'-'A'] -= mini;
        a['U'-'A'] -= mini;
        a['R'-'A'] -= mini;
        
        mini = a['T'-'A'];
        mini = min(mini, a['H'-'A']);
        mini = min(mini, a['R'-'A']);
        mini = min(mini, a['E'-'A']/2);
        for (int i = 0; i < mini; i++) {
            result.push_back(3);
        }
        a['T'-'A'] -= mini;
        a['H'-'A'] -= mini;
        a['R'-'A'] -= mini;
        a['E'-'A'] -= mini*2;
        
        mini = a['E'-'A'];
        mini = min(mini, a['I'-'A']);
        mini = min(mini, a['G'-'A']);
        mini = min(mini, a['H'-'A']);
        mini = min(mini, a['T'-'A']);
        for (int i = 0; i < mini; i++) {
            result.push_back(8);
        }
        a['E'-'A'] -= mini;
        a['I'-'A'] -= mini;
        a['G'-'A'] -= mini;
        a['H'-'A'] -= mini;
        a['T'-'A'] -= mini;
        
        mini = a['T'-'A'];
        mini = min(mini, a['W'-'A']);
        mini = min(mini, a['O'-'A']);
        for (int i = 0; i < mini; i++) {
            result.push_back(2);
        }
        a['T'-'A'] -= mini;
        a['W'-'A'] -= mini;
        a['O'-'A'] -= mini;
        
        
        mini = a['O'-'A'];
        mini = min(mini, a['N'-'A']);
        mini = min(mini, a['E'-'A']);
        for (int i = 0; i < mini; i++) {
            result.push_back(1);
        }
        a['O'-'A'] -= mini;
        a['N'-'A'] -= mini;
        a['E'-'A'] -= mini;

        
        mini = a['N'-'A']/2;
        mini = min(mini, a['I'-'A']);
        mini = min(mini, a['E'-'A']);
        for (int i = 0; i < mini; i++) {
            result.push_back(9);
        }
        a['N'-'A'] -= mini;
        a['I'-'A'] -= mini*2;
        a['E'-'A'] -= mini;
        
        cout << "Case #" << TC << ": ";
        sort(result.begin(), result.end());
        for (int i = 0; i < result.size(); i++) {
            cout << result[i];
        }
        cout << endl;
    }
    return 0;
}