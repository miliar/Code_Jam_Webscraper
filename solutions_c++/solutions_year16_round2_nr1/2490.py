#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;
int letters[26];

int main() {
    freopen("A-large.in", "rt", stdin);
    freopen("A-large.out", "wt", stdout);
    
    int numTests;
    cin >> numTests;
    
    for (int i = 0; i < numTests; ++i) {
        string str;
        vector <int> numbers;
        cin >> str;
        memset(letters, 0, sizeof(letters));
        
        for (int j = 0; j < (int) str.size(); ++j) {
            ++letters[str[j] - 'A'];
        }
        
        letters['E' - 'A'] -= letters['Z' - 'A'];
        letters['R' - 'A'] -= letters['Z' - 'A'];
        letters['O' - 'A'] -= letters['Z' - 'A'];
        while (letters['Z' - 'A'] > 0) {
            numbers.push_back(0);
            --letters['Z' - 'A'];
        }
        
        letters['T' - 'A'] -= letters['W' - 'A'];
        letters['O' - 'A'] -= letters['W' - 'A'];
        while (letters['W' - 'A'] > 0) {
            numbers.push_back(2);
            --letters['W' - 'A'];
        }
        
        letters['S' - 'A'] -= letters['X' - 'A'];
        letters['I' - 'A'] -= letters['X' - 'A'];
        while (letters['X' - 'A'] > 0) {
            numbers.push_back(6);
            --letters['X' - 'A'];
        }
        
        letters['E' - 'A'] -= 2 * letters['S' - 'A'];
        letters['V' - 'A'] -= letters['S' - 'A'];
        letters['N' - 'A'] -= letters['S' - 'A'];
        while (letters['S' - 'A'] > 0) {
            numbers.push_back(7);
            --letters['S' - 'A'];
        }
        
        letters['E' - 'A'] -= letters['G' - 'A'];
        letters['I' - 'A'] -= letters['G' - 'A'];
        letters['H' - 'A'] -= letters['G' - 'A'];
        letters['T' - 'A'] -= letters['G' - 'A'];
        while (letters['G' - 'A'] > 0) {
            numbers.push_back(8);
            --letters['G' - 'A'];
        }

        letters['F' - 'A'] -= letters['V' - 'A'];
        letters['I' - 'A'] -= letters['V' - 'A'];
        letters['E' - 'A'] -= letters['V' - 'A'];
        while (letters['V' - 'A'] > 0) {
            numbers.push_back(5);
            --letters['V' - 'A'];
        }

        letters['O' - 'A'] -= letters['F' - 'A'];
        letters['U' - 'A'] -= letters['F' - 'A'];
        letters['R' - 'A'] -= letters['F' - 'A'];
        while (letters['F' - 'A'] > 0) {
            numbers.push_back(4);
            --letters['F' - 'A'];
        }
        
        letters['T' - 'A'] -= letters['R' - 'A'];
        letters['H' - 'A'] -= letters['R' - 'A'];
        letters['E' - 'A'] -= 2 *letters['R' - 'A'];
        while (letters['R' - 'A'] > 0) {
            numbers.push_back(3);
            --letters['R' - 'A'];
        }
        
        letters['N' - 'A'] -= letters['O' - 'A'];
        letters['E' - 'A'] -= letters['O' - 'A'];
        while (letters['O' - 'A'] > 0) {
            numbers.push_back(1);
            --letters['O' - 'A'];
        }
        
        while (letters['I' - 'A'] > 0) {
            numbers.push_back(9);
            --letters['I' - 'A'];
        }
        
        cout << "Case #" << i + 1 << ": ";
        
        sort(numbers.begin(), numbers.end());
        for (int j = 0; j < (int) numbers.size(); ++j) {
            cout << numbers[j];
        }
        cout << endl;
    }
    
    return 0;
}
