
#include <iostream>
#include <cstdio>
#include <cstdlib>

using namespace std;

int main(void) {
    int n;
    string word, nword;
    
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    
    cin >> n;
    
    for (int i = 1; i <= n; i++) {
        cin >> word;
        nword = "";
        
        for (int j = 0; j < word.length(); j++) {
            if (nword.length() == 0 || nword[0] <= word[j]) {
                nword = word[j] + nword;
            } else {
                nword = nword + word[j];
            }
        }
        
        cout << "Case #" << i << ": " << nword << endl;
    }
    
    return 0;
}
