#include <iostream>
using namespace std;

 string flip(string s) {
    for (size_t i = 0; i < s.length(); i++) {
        if (s[i] == '+') {
            s[i] = '-';
        }
        else {
            s[i] = '+';
        }
    }
    return s;
 }

int checkHappyBottom(string s) {
    int index;
    index = s.length()-1;

    for (std::string::reverse_iterator rit=s.rbegin(); rit!=s.rend(); rit++) {
        if (s[s.length()-1] == '-') {
            index = s.length()-1;
            break;
        }
        if (*rit == '+') {
            if (s[index] == s[index - 1]) {
            }
            else {
                break;
            }
        }
        index--;
    }

    return index;
}

int numberOfFlips(string& s) {
    string sub;
    int count = 0;

    if (s.length() == 1) {
        if (s[0] == '-') {
            return 1;
        }
        else {
            return 0;
        }
    }

    while(checkHappyBottom(s) != 0) {
        if (s[s.length()-1] == '-') {
            sub = s;
            s = flip(sub);
        }
        else {
            sub = s.substr(0,checkHappyBottom(s));
            s = flip(sub);
        }
        count++;
    }
    return count;
}

int main()
{

    int i = 1;
    int testCases;
    string input;

    cin >> testCases;

    while (i <= testCases && cin >> input) {
        cout << "Case #" << i << ": ";
        cout << numberOfFlips(input) << endl;
        i++;
    }

    return 0;
}
