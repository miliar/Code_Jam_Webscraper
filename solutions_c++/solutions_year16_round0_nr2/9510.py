#include <iostream>

using namespace std;

int main(){
    int T;
    cin >> T;
    string eatline;
    getline(cin, eatline);
    int CN = 0;
    while(T--){
        ++CN;
        string seq;
        getline(cin, seq);
        int length = seq.length();
        int count = 0;
        bool flipped = false;
        for(int i = length;i>=0; i--){
            char state = seq[i];
            if(flipped){
                state = ((state == '+') ? '-' : '+');
            }
            if(state == '-'){
                ++count;
                flipped = !flipped;
            }

        }
        cout << "Case #" << CN << ": " << count << endl;        
    }
}
