#include <iostream>
#include <bits/stdc++.h>

using namespace std;
typedef long long i64;

int main(){
    ios_base::sync_with_stdio(false);
    int test;
    string input;
    cin >> test;
    for(int t =0 ; t < test;t++){
        cin >> input;
        int len = input.length();
        int count = input[len-1] == '-' ? 1 :0;
        for(int i=1;i<len;i++){
            if(input[i] != input[i-1]) count++;        
        }
        cout << "Case #" << t + 1 << ": " << count <<"\n";    
    }
    return 0;
}
