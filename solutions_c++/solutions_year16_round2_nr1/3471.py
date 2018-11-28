#include <bits/stdc++.h>
using namespace std;

string numbers[] = { "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE" };
vector<int> solution;

void solve (map<char,int>* occur, vector<int>* chosen) {
    bool isEmpty = true;
    for (map<char,int>::iterator it = occur->begin(); it != occur->end(); it++)
        if (it->second > 0) {
            isEmpty = false;
            break;
        }
    if (isEmpty) {
        solution = *chosen;
        return;
    }
    for (int i = 0; i < 10; i++) {
        map<char,int> cop;
        vector<int> cop2;
        cop.insert(occur->begin(), occur->end());
        cop2 = *chosen;
        for (int j = 0; j < numbers[i].size(); j++) {
            if ((*occur)[numbers[i][j]] == 0) break;
            (*occur)[numbers[i][j]]--;
            if (j == numbers[i].size()-1) {
                chosen->push_back(i);
                solve(occur, chosen);
            }
        }
        occur->clear();
        occur->insert(cop.begin(), cop.end());
        (*chosen) = cop2;
    }
}

int main (int argc, char** argv) {
    int cases;
    cin >> cases;
    for (int t = 1; t <= cases; t++) {
        cout << "Case #" << t << ": ";
        string input; cin >> input;
        vector<int> chosen;
        map<char,int> occur;
        for (int i = 0; i < input.size(); i++)
            occur[input[i]]++;
        solve(&occur, &chosen);
        sort(solution.begin(), solution.end());
        for (int i = 0; i < solution.size(); i++)
            cout << solution[i];
        cout << endl;
    }
    return 0;
}
