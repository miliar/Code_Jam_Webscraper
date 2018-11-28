#include <bits/stdc++.h>
using i64 = long long;
using u64 = unsigned long long;
using namespace std;

// DFS & BFS
/*
const u64 MAX_NUMBER_OF_VERTEXES = 2;
bool used[MAX_NUMBER_OF_VERTEXES];
list<u64>* g;
void DFS(u64 s){
    if (used[s])
        return;

    used[s] = true;

    for(auto it = g[s].begin(); it != g[s].end(); ++it){
        if (!used[*it]) {
            DFS(*it);
        }
    }
}
void BFS(u64 s){
    queue<u64> q;
    q.push(s);
    used[s] = true;

    while(!q.empty()){
        u64 cur = q.front();
        q.pop();

        for(auto it = g[cur].begin(); it != g[cur].end(); ++it){
            if (!used[*it]){
                q.push(*it);
                used[*it] = true;
            }
        }
    }
}
*/

int main() {
    ifstream in("in.txt");
    ofstream out("out.txt");
    assert(in.is_open() && out.is_open());
    const vector<string> numbers = {
            "ZERO",
            "ONE",
            "TWO",
            "THREE",
            "FOUR",
            "FIVE",
            "SIX",
            "SEVEN",
            "EIGHT",
            "NINE"
    };
    i64 T;
    in >> T;
    for(size_t test = 0; test < T; test++) {
        string S;
        in >> S;
        i64 letters[30];
        memset(letters, 0, sizeof(u64) * 30);
        i64 SLen = S.length();
        for (size_t i = 0; i < SLen; ++i)
            letters[S[i] - 'A']++;

        vector<i64> ans;
        //find zeros
        while (letters['Z' - 'A'] != 0) {
            i64 idx = 0;
            i64 len = numbers[idx].length();
            for (size_t j = 0; j < len; ++j)
                letters[numbers[idx][j] - 'A']--;

            ans.push_back(idx);
        }

        //find twos
        while (letters['W' - 'A'] != 0) {
            i64 idx = 2;
            i64 len = numbers[idx].length();
            for (size_t j = 0; j < len; ++j)
                letters[numbers[idx][j] - 'A']--;

            ans.push_back(idx);
        }

        //find fours
        while (letters['U' - 'A'] != 0) {
            i64 idx = 4;
            i64 len = numbers[idx].length();
            for (size_t j = 0; j < len; ++j)
                letters[numbers[idx][j] - 'A']--;

            ans.push_back(idx);
        }

        //find sixes
        while (letters['X' - 'A'] != 0) {
            i64 idx = 6;
            i64 len = numbers[idx].length();
            for (size_t j = 0; j < len; ++j)
                letters[numbers[idx][j] - 'A']--;

            ans.push_back(idx);
        }

        //find eights
        while (letters['G' - 'A'] != 0) {
            i64 idx = 8;
            i64 len = numbers[idx].length();
            for (size_t j = 0; j < len; ++j)
                letters[numbers[idx][j] - 'A']--;

            ans.push_back(idx);
        }

        //find sevens
        while (letters['S' - 'A'] != 0) {
            i64 idx = 7;
            i64 len = numbers[idx].length();
            for (size_t j = 0; j < len; ++j)
                letters[numbers[idx][j] - 'A']--;

            ans.push_back(idx);
        }

        //find fives
        while (letters['F' - 'A'] != 0) {
            i64 idx = 5;
            i64 len = numbers[idx].length();
            for (size_t j = 0; j < len; ++j)
                letters[numbers[idx][j] - 'A']--;

            ans.push_back(idx);
        }

        //find threes
        while (letters['T' - 'A'] != 0) {
            i64 idx = 3;
            i64 len = numbers[idx].length();
            for (size_t j = 0; j < len; ++j)
                letters[numbers[idx][j] - 'A']--;

            ans.push_back(idx);
        }

        //find nines
        while (letters['I' - 'A'] != 0) {
            i64 idx = 9;
            i64 len = numbers[idx].length();
            for (size_t j = 0; j < len; ++j)
                letters[numbers[idx][j] - 'A']--;

            ans.push_back(idx);
        }

        //find ones
        while (letters['E' - 'A'] != 0) {
            i64 idx = 1;
            i64 len = numbers[idx].length();
            for (size_t j = 0; j < len; ++j)
                letters[numbers[idx][j] - 'A']--;

            ans.push_back(idx);
        }

        sort(ans.begin(), ans.end());
        out << "Case #" << test + 1 << ": ";
        cout << "Case #" << test + 1 << ": ";
        for (auto i : ans)
            out << i;
        out << "\n";
        for (auto i : ans)
            cout << i;
        cout << "\n";
    }
    return 0;
}