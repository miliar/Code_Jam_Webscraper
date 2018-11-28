#include "bits/stdc++.h"

using namespace std;

int len(int n){
    int length = 0;
    while(n){
        length++;
        n /= 10;
    }
    
    return length;
}

int main(){
    
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    
    int t;
    cin >> t;
    for(int i = 1; i <= t; i++){
        bitset<10> check(0);
        
        long long int n;
        cin >> n;
        
        long long int incre = n;
        
        if(n == 0){
            cout << "Case #" << i << ": INSOMNIA" << endl;
        }else{
            while(1){
                
                string temp = to_string(n);
                
                for(int i = 0; i < temp.length(); i++){
                    check[temp[i]-'0'] = 1;
                }
                
                if(check == 2047){
                    break;
                }
                
                n += incre;
                
            }
            cout << "Case #" << i << ": " << n << endl;
        }
        
    }
    
    return 0;
}