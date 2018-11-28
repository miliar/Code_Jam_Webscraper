#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
using namespace std;

void serase(vector<char> &letters, char c, int n) {
    int counter = 0;
    int i = 0;
    while (i < letters.size() && letters[i] != c)
        i++;
    letters.erase(letters.begin() + i, letters.begin() + i + n);
}

int count(vector<char> &letters, char c) {
    int i = 0;
    while (i < letters.size() && (letters[i] != c))
        i++;
    int j = i;
    while (j < letters.size() && (letters[j] == c))
        j++;
    return j - i;
}

int main()
{
    ifstream fin("A-large.in");
    ofstream fout("out.txt");
    int t;
    fin >> t;
    for (int glob = 0; glob < t; glob++) {
        string s;
        fin >> s;
        vector<char> letters(s.size());
        for (int i = 0; i < s.size(); i++)
            letters[i] = s[i];
        sort(letters.begin(), letters.end());
        vector<int> ans;

        int cur = 0;

        cur = count(letters, 'Z');
        for (int i = 0; i < cur; i++)
            ans.push_back(0);
        serase(letters, 'Z', cur);
        serase(letters, 'E', cur);
        serase(letters, 'R', cur);
        serase(letters, 'O', cur);

        cur = count(letters, 'W');
        for (int i = 0; i < cur; i++)
            ans.push_back(2);
        serase(letters, 'T', cur);
        serase(letters, 'W', cur);
        serase(letters, 'O', cur);

        cur = count(letters, 'U');
        for (int i = 0; i < cur; i++)
            ans.push_back(4);
        serase(letters, 'F', cur);
        serase(letters, 'O', cur);
        serase(letters, 'U', cur);
        serase(letters, 'R', cur);

        cur = count(letters, 'X');
        for (int i = 0; i < cur; i++)
            ans.push_back(6);
        serase(letters, 'S', cur);
        serase(letters, 'I', cur);
        serase(letters, 'X', cur);

        cur = count(letters, 'G');
        for (int i = 0; i < cur; i++)
            ans.push_back(8);
        serase(letters, 'E', cur);
        serase(letters, 'I', cur);
        serase(letters, 'G', cur);
        serase(letters, 'H', cur);
        serase(letters, 'T', cur);

        cur = count(letters, 'O');
        for (int i = 0; i < cur; i++)
            ans.push_back(1);
        serase(letters, 'O', cur);
        serase(letters, 'N', cur);
        serase(letters, 'E', cur);


        cur = count(letters, 'T');
        for (int i = 0; i < cur; i++)
            ans.push_back(3);
        serase(letters, 'T', cur);
        serase(letters, 'H', cur);
        serase(letters, 'R', cur);
        serase(letters, 'E', cur);
        serase(letters, 'E', cur);

        cur = count(letters, 'F');
        for (int i = 0; i < cur; i++)
            ans.push_back(5);
        serase(letters, 'F', cur);
        serase(letters, 'I', cur);
        serase(letters, 'V', cur);
        serase(letters, 'E', cur);

        cur = count(letters, 'S');
        for (int i = 0; i < cur; i++)
            ans.push_back(7);
        serase(letters, 'S', cur);
        serase(letters, 'E', cur);
        serase(letters, 'V', cur);
        serase(letters, 'E', cur);
        serase(letters, 'N', cur);

        for (int i = 0; i < letters.size() / 4; i++)
            ans.push_back(9);

        sort(ans.begin(), ans.end());

        fout << "Case #" << glob + 1 << ": ";
        for (int i = 0; i < ans.size(); i++)
            fout << ans[i];
        fout << endl;
    }
    return 0;
}
