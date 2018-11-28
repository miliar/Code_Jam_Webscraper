#include "bits/stdc++.h"

using namespace std;

int main(){
    
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    
    int t;
    cin >> t;
    
    for(int i = 0; i < t; i++){
        string n;
        cin >> n;
        
        int count = 0;
        
        char check = '=';
        
        for(int i = 0; i < n.length(); i++){
            if(n[i] == '-' && check == '='){
                count++;
                check = '-';
            }else if(n[i] == '-' && check == '-'){
                continue;
            }else if(n[i] == '-' && check == '+'){
                count += 2;
                check = '-';
            }else{
                check = '+';
            }
        }
        
        
        cout << "Case #" << i+1 << ": " << count << endl;
    }
    
    return 0;
}