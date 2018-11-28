#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <algorithm>
#include <queue>
using namespace std;

string compute_lastword(string& word)
{
    vector<string> combinations;
    queue<string> q1;
    queue<string> q2;
    string w;
    w = word[0];
    q1.push(w);

    for (int i=1; i<word.size(); i++) {
        while(!q1.empty()) {
            string s = q1.front();
            q1.pop();
            string s1 = word[i] + s;
            string s2 = s + word[i];
            q2.push(s1);
            q2.push(s2);
        }
        swap(q1, q2);
    }

    while (!q1.empty()) {
        combinations.push_back(q1.front());
        q1.pop();
    }

    sort(combinations.begin(), combinations.end());
    return combinations[combinations.size()-1];
}

void func(vector<string>& words, vector <string>& lastwords)
{
    for (int i=0; i<words.size(); i++) {
        string word = compute_lastword(words[i]);
        lastwords.push_back(word);
    }
}


int main()
{
    int T = 0;
    vector <string> words;
    vector <string> lastwords;

    cin >> T;
    cin.get();

    for (int i=0; i<T; i++) {
        string line, word;
        getline(cin, line);
        istringstream stream(line);
        stream >> word;
        words.push_back(word);
    }
 
    func(words, lastwords);
    for (int j=0; j<T; j++) {
        cout << "Case #" << j+1 << ": " << lastwords[j] << endl;
    }
    return 0;
}
