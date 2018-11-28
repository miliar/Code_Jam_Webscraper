#include <set>
#include <bits/stdc++.h>

using namespace std;

void last_word(int i, const string &S) {
    cout << "Case #" << i << ": ";
    deque<char> word;
    char start;
    for (auto c: S) {
        if (!word.empty())
            start = word.front();
        else
            start = 'a';

        if (start <= c) {
            word.push_front(c);
        }
        else
            word.push_back(c);
    }
    for (auto c: word) {
        cout << c;
    }

    cout << "\n";
}

int main(int argc, char *argv[]) {
//    ifstream inputFile;
//    ofstream outputFile;
//    inputFile.open("/home/ars/ClionProjects/ForTests/input.txt");
//    outputFile.open("/home/ars/ClionProjects/ForTests/output.txt");
//    if (inputFile.fail()) {
//        cout << "Failed to open file\n";
//    }

    freopen("/home/ars/ClionProjects/ForTests/in", "r", stdin);
    freopen("/home/ars/ClionProjects/ForTests/out", "w", stdout);
    int T;
    string S;
    cin >> T;
    for (int i = 1; i <= T; i++) {
        cin >> S;
        last_word(i, S);
    }

    return 0;
}