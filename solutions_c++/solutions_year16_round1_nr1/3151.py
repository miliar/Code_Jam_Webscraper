#include <cstdio>
#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

int main(){
    int t, cases=1;
    string s, last_word, last_word_final, last_word_begin;

    scanf("%d", &t);

    while(t--){
        cin >> s;
        last_word.push_back(s[0]); last_word_final.push_back(s[0]); last_word_begin.push_back(s[0]);
        for(int i = 1 ; s[i] ; i++){
            last_word_final = last_word; last_word_begin = last_word;

            last_word_final.push_back(s[i]);
            last_word_begin.insert(0, 1, s[i]);
            //cout << last_word_final << endl;
            //cout << last_word_begin << endl << endl;
            last_word = max(last_word_final, last_word_begin);
        }

        cout << "Case #" << cases++ << ": " << last_word << endl;
        last_word.clear(); last_word_begin.clear(); last_word_final.clear();
    }

    return 0;
}
