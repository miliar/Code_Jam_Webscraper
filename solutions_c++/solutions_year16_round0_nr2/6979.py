#include <iostream>
#include <string>
#include <algorithm>
#include <climits>

using namespace std;

bool hasOnlyOneValue(string s, char value)
{
    for(int i=0; i<s.length(); i++)
        if (s.at(i) != value) return false;
    return true;
}
// +0
bool isAllHappySide(string s)
{
    return hasOnlyOneValue(s, '+');
}
// +1
bool isAllBlankSide(string s)
{
    return hasOnlyOneValue(s, '-');
}
// +2
bool happyBlank(string s)
{
    int p = 0;
    for(int i=0; i<s.length(); i++) {
        if (s.at(i) != '+') {
            p = i;
            break;
        }
    }
    return (p > 0 && isAllBlankSide(s.substr(p)));
}
// +1
bool blankHappy(string s)
{
    int p = 0;
    for(int i=0; i<s.length(); i++) {
        if (s.at(i) != '-') {
            p = i;
            break;
        }
    }
    return (p > 0 && isAllHappySide(s.substr(p)));
}

int findPoint(string s) 
{
    char value = s.at(0);
    for(int i=0; i<s.length(); i++) {
        if (s.at(i) != value) return i;
    }
    return 0;
}

int solve(string s, int totalCost)
{
    if (isAllHappySide(s)) return totalCost + 0;
    else if (isAllBlankSide(s)) return totalCost + 1;
    else if (happyBlank(s)) return totalCost + 2;
    else if (blankHappy(s)) return totalCost + 1;

    int p = findPoint(s);
    string top = s.substr(0, p);
    for(int i=0; i<top.length(); i++) {
        if (top.at(i) == '+') top[i] = '-';
        else if (top.at(i) == '-') top[i] = '+';
    }
    reverse(top.begin(), top.end());
    s.replace(0, p, top);
    return solve(s, totalCost+1);
}

int main()
{
    int T;

    cin >> T;
    for(int t=1; t<=T; t++) {
        string in;
        cin >> in;
        cout << "Case #" << t << ": " << solve(in, 0) << endl; 
    }
    return 0;
}
