#include <iostream>
#include <cstdlib>
#include <vector>
#include <string>

using namespace std;

bool checkValidString(string line) {
    //cout << "checking: " << line << endl;
    bool letters[26];
    for (int i=0; i<26; ++i) {
        letters[i] = false;
    }

    letters[line[0] - 'a'] = true;
    for (int i=1; i<line.size(); ++i) {
        if ((line[i] == line[i-1]) || !letters[line[i] - 'a']) {
            letters[line[i] -'a'] = true;
        } else {
            //cout << "Not valid" << endl;
            return false;
        }
    }
    //cout << "Valid" << endl;
    return true;
}

long long doIt(vector<string> &cars, long long count, string current) {
    if (cars.size() == 0) {
        return (count +1) %1000000007;
    }
    for (int i=0; i<cars.size(); ++i) {
        if (checkValidString(current + cars[i])) {
            // Valid string, try all substrings
            vector<string> temp(cars);
            // New vector without the attemping car
            //cout << "about to erase: " << *(cars.begin() + i) << endl;
            temp.erase(temp.begin() + i);
            // Recursive call to solve
            count = doIt(temp, count, current + cars[i]);
        }
    }
    return count;
}

void refineStrings(vector<string> &cars) {
    for (int i=0;i<cars.size(); ++i) {
        string temp;
        temp = temp + cars[i][0];
        for (int j=1; j<cars[i].size(); ++j) {
            if (cars[i][j] != temp[temp.size()-1]) {
                temp = temp + cars[i][j];
            }
        }
        cars[i] = temp;
    }
}

int main() {
    int N;
    int sets;
    string temp;
    // cases
    cin >> N;
    for (int i=0; i<N; ++i) {
        vector<string> cars;
        cin >> sets;
        for (int j=0; j< sets; ++j) {
            cin >> temp;
            cars.push_back(temp);
        }
        refineStrings(cars);
        cout << "Case #" << i + 1 << ": " << doIt(cars, 0, "") << endl;
    }
    return 0;
}


















