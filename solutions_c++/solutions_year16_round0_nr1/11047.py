#include <iostream>

using namespace std;

int main(){
    int T;
    cin >> T;

    for(int i = 0; i < T; i++){
        int N;
        cin >> N;
        if(N == 0){
            cout << "Case #" << (i + 1) << ": " << "INSOMNIA" << endl;;
        }
        else{
            bool digits[10];
            for(int j = 0; j < 10; j++){
                digits[j] = false;
            }
            long lastNum = N;
            while(true){
                long tmp = lastNum;
                while(tmp > 0){
                    digits[tmp % 10] = true;
                    tmp /= 10;
                }
                bool fallAsleep = true;
                for(int j = 0; j < 10; j++){
                    if(!digits[j]){
                        fallAsleep = false;
                        break;
                    }
                }
                if(fallAsleep){
                    cout << "Case #" << (i + 1) << ": " << lastNum << endl;;
                    break;
                }
                else{
                    lastNum += N;
                }
            }
        }
    }
}
