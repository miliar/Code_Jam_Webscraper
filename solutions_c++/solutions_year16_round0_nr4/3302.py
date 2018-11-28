#include<iostream>
#include<math.h>

using namespace std;

int main(){
    int T;
    cin >> T;
    int count = 0;
    while(T--){
        long long int K, C, S;
        cin >> K ;
        cin >> C;
        cin >> S;
        cout << "Case #" << ++count << ":" << " " ;
        if(ceil(K/C) > S){
            cout << "IMPOSSIBLE" << endl;
            continue;
        }
        long long int power[200] = {1};
        power[0] = 1;
        for(int i = 1; i<= C ;i++){
            power[i] = power[i-1]*K;
        }
        
        int i = 0;
        while(true) {
            long long int sum = 0;
            for(int j = C-1 ; j >=0 ; j-- ){
                if(i == K) {
                    i = K-1;
                }
                sum += i*power[j];
                i++;
            }
            cout << sum+1 << " " ;
            if(i >= K) {
                 break;
            }

        }
        cout << endl;
    }
    return 0;
}
