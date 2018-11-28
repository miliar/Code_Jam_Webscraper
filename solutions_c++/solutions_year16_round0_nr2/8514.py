#include <iostream>

using namespace std;

int main(){
    int T;
    string S;
    cin >> T;
    for(int i = 1; i <= T ; ++i){
        cin >> S;
        int len = S.length();
        int chk = 0;
        int j;
        int countt = 0;
        while(true){
            for(j = len-1; j >= 0 ; --j){
                if(S[j] == '-'){
                    break;
                }
            }
            //cout << "J = " << j << endl;
            if(j == -1){
                break;
            }else{
                for(int k = 0;k <= j ; ++k){
                    if(S[k] == '-'){
                        S[k] = '+';
                    }else if(S[k] == '+'){
                        S[k] = '-';
                    }
                }
                countt++;
            }
        }
        cout << "Case #" << i << ": " << countt << endl;
    }
    return 0;
}
