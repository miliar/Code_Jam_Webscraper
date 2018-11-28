#include <bits/stdc++.h>
using namespace std;
int a[10];

bool check() {
        for(int j = 0;j < 10;j++)
            if(a[j] != 1) 
                return false;
    return true;
}
int main()
{
    int tests;
    long long N;
    string input;
    cin >> tests;
    
    for(int i = 1;i <= tests;i++) {
        cin >> N;
        memset(a,0,sizeof(a));
        input = to_string(N);
        int length = input.length();
        for(int j = 0 ;j < length; j++) {
            a[input[j]-'0'] = 1;
        }
        
        // check if it is done. Else continue
        
        long long prev = N,base = N;
        int k = 1;
        if(check()){ cout<< "Case #" << i <<": " << N << endl; continue;}
        else {
                while(!check()) {
                    prev = N;
                    N = (k+1) * base;
                    k++;
                    input = to_string(N);
                    length = input.length();
                    for(int j = 0 ;j < length; j++) {
                        a[input[j]-'0'] = 1;
                    }
                    if(N == prev) break;
                }            
        }
        
        
    
        if(check())
            cout<< "Case #" << i <<": " << N << endl;
        else 
            cout<< "Case #" << i <<": INSOMNIA"  << endl;
    }
    
    
    
    return 0;
}
