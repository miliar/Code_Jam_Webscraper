#include <iostream>
#include <vector>
#include <fstream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <utility>
#include <set>
#include <stack>
#include <queue>
#include <algorithm>

#define pb push_back

using namespace std;

bool isVowel(char c){
    if (c == 'a' || c=='e' || c == 'i' || c == 'o' || c=='u')
        return true;
    return false;
}

int getAnswer(string word, int n){
    int ans = 0;
    int len = word.length();
    int start = 0;

    for (int i = 0; i <= len-n; i++){
        int j;
        for (j = i; j < i+n; j++){
            if (isVowel(word[j])){
                break;
            }
        }

        if (j == i+n){
            int totLeft = i;
            int totRight = len - j;

            ans += 1;
            ans += totRight;
            ans += totLeft-start;
            ans += (totLeft-start)*totRight;

            start = i+1;
        }
    }
    return ans;
}

int main(){
    ifstream cin ("A.txt");
    ofstream cout("Aout.txt");
    int nc;
    cin >> nc;

    for (int tc = 1; tc <= nc; tc++){
        string word;
        int n;
        cin >> word >> n;
        int answer = getAnswer(word, n);
        cout << "Case #" << tc << ": " << answer << endl;
    }

    return 0;
}
