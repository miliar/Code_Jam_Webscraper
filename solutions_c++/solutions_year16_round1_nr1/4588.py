#include <iostream>
#include <cstdio>
#include <set>

using namespace std;

void make(string& S, string& lastword, string& best) {
    if (S.empty()) {
        if (lastword.compare(best) > 0) {
            best = lastword;
        }
        return;
    }
    
    char c = S[0];
    
    S.erase(S.begin());
    lastword.insert(lastword.begin(), c);
    make(S, lastword, best);
    lastword.erase(lastword.begin());
    
    lastword.insert(lastword.end(), c);
    make(S, lastword, best);
    lastword.erase(lastword.end() - 1);
    
    S.insert(S.begin(), c);
}

int main() {
    int numCases, caseNum = 1;
    string S, lastword, best;
    
    scanf("%d", &numCases);
    
    while(numCases--) {
        cin >> S;
        
        lastword = "";
        best = "";
        lastword.insert(lastword.begin(), S[0]);
        S.erase(S.begin());
        make(S, lastword, best);
        
        printf("Case #%d: %s\n", caseNum++, best.c_str());
    }
    
    return 0;
}