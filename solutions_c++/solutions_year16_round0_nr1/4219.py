#include<iostream>

using namespace std;

int main(){
    int t;
    cin >> t;
    int count = 0;
    while(t--){
        long long int N;
        cin >> N;

        cout << "Case #" << ++count << ":" << " ";

        if(N == 0) {
            cout << "INSOMNIA" << endl;
            continue;
        }
        int flag = 1;
        int arr[10] = {0};
        long long int M = N;
        while(M > 0){
            if(arr[M%10] == 0) {
                arr[M%10] = 1;
            }
            M = M/10;
        }
        int multiplier = 1;
        int shouldTry = 1;
        long long int result = N;
        while(flag){
            shouldTry = 0;
            for(int i=0; i< 10; i++){
                 if(arr[i] == 0) {
                      shouldTry = 1;
                      break;
                  }
            }
            if(shouldTry){
                M = N*multiplier;
                result = M;
                multiplier++;
                while(M > 0) {
                    if(arr[M%10] == 0){
                        arr[M%10] = 1;
                    }
                     M = M/10;
                }
            }
            flag = shouldTry;
        }
        cout << result << endl;
    }
    return 0;
}
