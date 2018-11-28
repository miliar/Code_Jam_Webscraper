#include<cstdio>
#include<iostream>
#include<algorithm>
#include<deque>
#include<queue>
#include<string>

using namespace std;
int t, smax, k, friends;
string s;

int main(){       
    cin >> t;
    for(int ncase = 1; ncase <= t; ncase++){
        cin >> smax >> s;
        
        k = 0;
        friends = 0;
        
        for(int i = 0; i <= smax; i++){
            if(k < i){
               friends += i-k;
               k += i-k;               
            }           
            k+=s[i]-'0';    
        }
        
        cout << "Case #" << ncase << ": " << friends << endl;
    }   
    
    return 0;
}
