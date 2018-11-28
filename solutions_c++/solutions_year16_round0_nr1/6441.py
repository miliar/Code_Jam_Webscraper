#include <iostream>
#include <bits/stdc++.h>

using namespace std;
typedef long long i64;
typedef unsigned int uint;

int main(){
    ios_base::sync_with_stdio(false);
    int test;
    long N;
    cin >> test;
    for(int t = 0;t< test;t++){
        cin >> N;
        if ( N == 0) {cout <<"Case #"<<t+1<<": INSOMNIA\n";continue;}
        set<int> digits;
        uint multiple = 1;
        while(digits.size() < 10){
           long temp = N * multiple; 
           while(temp ){
                digits.insert(temp % 10);
                temp /= 10;
           }       
           multiple++;
        }
        cout << "Case #"<<t+1<<": " << N  * ( multiple -1) << "\n";                      
    
    }

        return 0;
}
