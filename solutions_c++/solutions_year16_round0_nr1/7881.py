#include <iostream>
#include <set>
#include <string>
#include <sstream>
using namespace std;

int convertToInt(string s) {
    int number = 0;

    stringstream convert(s);
    convert >> number;

    return number;
}

string convertToString(int n) {
    string temp = "";

    ostringstream convert;
    convert << n;
    temp = convert.str();

    return temp;
}

set<int> parseInt(string n) {
    set<int> nums;
    int num = 0;
    string temp = "";

    for (size_t i = 0; i < n.length(); i++) {
        temp += n[i];
        num = convertToInt(temp);
        nums.insert(num);
        temp = "";
    }

    return nums;
}

void lastNumberBeforeAsleep(string n) {
    int multiplier = 1;
    int result = 0;
    int number = 0;
    string tempnum = "";
    set<int> digits = parseInt(n);
    set<int> moredigits;
    set<int> sum;
    sum.insert(digits.begin(),digits.end());

    while (multiplier < 1000000) {
        number = convertToInt(n);
        multiplier++;
        result = number*multiplier;
        tempnum = convertToString(result);
        moredigits = parseInt(tempnum);
        sum.insert(moredigits.begin(),moredigits.end());
        if (sum.size() == 10) {
            cout << tempnum << endl;
            break;
        }
        if (number == 0 || number > 1000000) {
            cout << "INSOMNIA" << endl;
            break;
        }
        tempnum = "";
        result = 0;
    }
}

int main()
{
    int i = 1;
    int testCases;
    string input;

    cin >> testCases;

    while (i <= testCases && cin >> input) {
        cout << "Case #" << i << ": ";
        lastNumberBeforeAsleep(input);
        i++;
    }

    return 0;
}
