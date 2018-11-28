#include<iostream>
#include<string.h>

using namespace std;

int main(){
    int T;
    cin >> T;
    int count = 0;
    while(T--){
        char S[200];
        cin >> S;
        cout << "Case #" << ++count << ":" << " ";
        int len = strlen(S);
        bool isFlipRequired = false;   
        for(int i=0; i< len; i++){
            if(S[i] == '-') {
                isFlipRequired = true;
                break;
            }
        }
        if(!isFlipRequired) {
            cout << 0 << endl;
            continue;
        }
        int flip = 0;
        for(int i = len-1; i>= 0 ; i--){
            if(S[i] == '-'){
                flip++;
                for(int j = 0; j <= i ; j++) {
                    if(S[j] == '+'){
                        S[j] = '-';
                    }else{
                        S[j] = '+';
                    }
                }
            }
        }
        cout << flip << endl;
    }
    return 0;
}
