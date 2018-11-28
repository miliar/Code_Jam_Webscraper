#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <bitset>
#include <algorithm>

using namespace std;

int findChar(string& s, char c) {
    int rc = -1;
    for (int i=0; i<s.length(); i++) {
        if ((s[i] != 'A') && (s[i] == c)) {
            rc = i;
            break;
        }
    }
    return rc;
}

int markFound(string& s1, int index1, string s2, int index2)
{
    int count = 0;
    while(count < s2.length()) {
        if (count == index2) {
            s1[index1] = 'A';
            count++;
            continue;
        }
        int index = findChar(s1, s2[count]);
        if (index > -1) {
            s1[index] = 'A';
            count++;
        }
    }
    return count;
}

string findNumber(string& numString)
{
    string rs;
    int count = 0;
    while (count < numString.length()) {
        // incr the count on match of any string
        int index = -1;
        index = findChar(numString, 'Z');
        if (index > -1) {
            count += markFound(numString, index, string("ZERO"), 1);
            rs +="0";
            continue;
        }

        index = findChar(numString, 'W');
        if (index > -1) {
            count += markFound(numString, index, string("TWO"), 1);
            rs +="2";
            continue;
        }
        
        index = findChar(numString, 'U');
        if (index > -1) {
            count += markFound(numString, index, string("FOUR"), 2);
            rs +="4";
            continue;
        }

        index = findChar(numString, 'O');
        if (index > -1) {
            count += markFound(numString, index, string("ONE"), 0);
            rs +="1";
            continue;
        }

        index = findChar(numString, 'R');
        if (index > -1) {
            count += markFound(numString, index, string("THREE"), 2);
            rs +="3";
            continue;
        }

        index = findChar(numString, 'F');
        if (index > -1) {
            count += markFound(numString, index, string("FIVE"), 0);
            rs +="5";
            continue;
        }

        index = findChar(numString, 'X');
        if (index > -1) {
            count += markFound(numString, index, string("SIX"), 2);
            rs +="6";
            continue;
        }

        index = findChar(numString, 'G');
        if (index > -1) {
            count += markFound(numString, index, string("EIGHT"), 2);
            rs +="8";
            continue;
        }

        index = findChar(numString, 'V');
        if (index > -1) {
            count += markFound(numString, index, string("SEVEN"), 2);
            rs +="7";
            continue;
        }

        index = findChar(numString, 'N');
        if (index > -1) {
            count += markFound(numString, index, string("NINE"), 0);
            rs +="9";
            continue;
        }
    }
    return rs;
}

int main()
{
    int T = 0;
    cin >> T;
    cin.get();

    for (int i=0; i<T; i++) {
        string s;
        getline(cin, s);
        string rs = findNumber(s);
        sort(rs.begin(), rs.end());
        cout << "Case #" << i+1 << ": " << rs << endl;
    }
    return 0;
}
