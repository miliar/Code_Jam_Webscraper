#include <string>
#include <cstring>
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath> 

using namespace std;

int main() {

    //num of test cases
    int test_cnt;
   
    cin >> test_cnt;

    for(int idx = 1; idx <= test_cnt; idx++) {
        int A,B,K;
        int result = 0;

        cin >> A; cin >> B; cin >> K;
        
        for(int i = 0; i < A; i++){
            for(int j = 0; j < B; j++){
                if ((i&j) < K){
                    result++;
                }    
            }
        }
      
        cout << "Case #"<<idx<<": "<<result<<endl;   
    }

    return 0;
}
