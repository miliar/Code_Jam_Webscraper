#include <string>
#include "junction.h"

void round2a (){
    int T;
    string word;
    cin >> T;

    for (int i=0; i<T; i++){
        cin >> word;
        for (int j=1; j<word.size(); j++){
            if (word[j]>=word[0]){
                word.insert(word.begin(),word[j]);
                word.erase(word.begin()+j+1);
            }
        }

        cout << "Case #" << i+1 << ": " << word <<endl;

    }


}
