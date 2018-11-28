#include <iostream>
#include <string>
#include <vector>

using namespace std;

void remove(int i, vector<int>& count, vector<vector<int> >& digits) {
    for(int j = 0; j < 30; ++j)
        count[j] -= digits[i][j];
}

void reduce(char c, int d, vector<int>& count, vector<vector<int> >& digits, vector<int>& result) {
    while(count[c - 'A'] > 0) {
        remove(d, count, digits);
        result[d]++;
    }
}

void solve() {
    
    string s;
    cin >> s;
    
    vector<int> count(30, 0);
    for(int i = 0; i < s.size(); ++i)
        count[s[i] - 'A']++;
    
    vector<vector<int> > digits(10, vector<int>(30, 0));
    
    digits[0]['Z' - 'A']++;
    digits[0]['E' - 'A']++;
    digits[0]['R' - 'A']++;
    digits[0]['O' - 'A']++;
    
    digits[1]['O' - 'A']++;
    digits[1]['N' - 'A']++;
    digits[1]['E' - 'A']++;
    
    digits[2]['T' - 'A']++;
    digits[2]['W' - 'A']++;
    digits[2]['O' - 'A']++;
    
    digits[3]['T' - 'A']++;
    digits[3]['H' - 'A']++;
    digits[3]['R' - 'A']++;
    digits[3]['E' - 'A']++;
    digits[3]['E' - 'A']++;
    
    digits[4]['F' - 'A']++;
    digits[4]['O' - 'A']++;
    digits[4]['U' - 'A']++;
    digits[4]['R' - 'A']++;
    
    digits[5]['F' - 'A']++;
    digits[5]['I' - 'A']++;
    digits[5]['V' - 'A']++;
    digits[5]['E' - 'A']++;
    
    digits[6]['S' - 'A']++;
    digits[6]['I' - 'A']++;
    digits[6]['X' - 'A']++;
    
    digits[7]['S' - 'A']++;
    digits[7]['E' - 'A']++;
    digits[7]['V' - 'A']++;
    digits[7]['E' - 'A']++;
    digits[7]['N' - 'A']++;
    
    digits[8]['E' - 'A']++;
    digits[8]['I' - 'A']++;
    digits[8]['G' - 'A']++;
    digits[8]['H' - 'A']++;
    digits[8]['T' - 'A']++;
    
    digits[9]['N' - 'A']++;
    digits[9]['I' - 'A']++;
    digits[9]['N' - 'A']++;
    digits[9]['E' - 'A']++;
    
    vector<int> result(10, 0);
    
    reduce('Z', 0, count, digits, result);
    reduce('W', 2, count, digits, result);
    reduce('U', 4, count, digits, result);
    reduce('X', 6, count, digits, result);
    reduce('G', 8, count, digits, result);
    reduce('O', 1, count, digits, result);
    reduce('H', 3, count, digits, result);
    reduce('F', 5, count, digits, result);
    reduce('S', 7, count, digits, result);
    reduce('I', 9, count, digits, result);
    
    for(int i = 0; i < 10; ++i) {
        while(result[i] --> 0)
            cout << i;
    }
    
    for(int i = 0; i < 30; ++i) {
        if(count[i] != 0) {
            //cout << static_cast<char>('A' + i) << ": " << count[i] << endl;
            cout << "LOOOOOOOOOOOOOOOOOOOOL" << endl;
        }
    }
    
    cout << endl;
}

int main() {
    
    int T;
    cin >> T;
    int c = 1;
    while(T --> 0) {
        cout << "Case #" << c++ << ": ";
        solve();
    }
    
    return 0;
}
