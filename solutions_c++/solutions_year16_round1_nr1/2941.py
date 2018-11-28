#include <bits/stdc++.h>

using namespace std;

string last(string S){
    int i;
    deque<char> a;
    a.push_back(S[0]);
    for(i = 1; S[i]; i ++){
        if(S[i] >= a[0])
            a.push_front(S[i]);
        else
            a.push_back(S[i]);
    }
    string out(a.begin(), a.end());
    return out;
}

int main() {
    ifstream fileIn;
    ofstream fileOut;
    fileIn.open("A-large.in");
    fileOut.open("out.txt");
    int T;
    fileIn >> T;
    for(int i = 1; i <= T; i ++){
        string S;
        fileIn >> S;
        fileOut << "Case #" << i << ": " << last(S) << "\n";
    }
    return 0;
}
