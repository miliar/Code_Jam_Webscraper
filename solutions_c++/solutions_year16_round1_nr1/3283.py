#include <iostream>
#include <stdio.h>
using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("myout2.txt","w",stdout);
    int T;
    cin >> T;

    for(int i = 1; i <= T; ++i){
        string letters;
        string lastWord = "";
        cin >> letters;
        lastWord = " ";
        lastWord[0] = letters[0];
        for(int j = 1; j < letters.length(); ++j){
            string l = " ";
            l[0] = letters[j];
            if(letters[j] >= lastWord[0]){
                lastWord = l + lastWord;
            }
            else{
                lastWord = lastWord + l;
            }
        }
        cout << "Case #" << i << ": " << lastWord <<endl;
    }
    return 0;
}
