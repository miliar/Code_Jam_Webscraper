#include <iostream>
#include <string>
using namespace std;

string s;


int solve(){
    //while loop and check
    int steps = 0;
    while(1){
        int ff = s[0], i = -1;
        
        if(ff == '-'){
            for(int k = 0; k < s.size(); k++){
                if(s[k] == '-')i = k;
            }
            if(i != -1){
                i++;
                int sz = i/2, en = i-1;
                for(int k = 0; k < sz; k++){
                    swap(s[k],s[en]);
                    en--;
                }
                
                for(int k = 0; k < i; k++){
                    if(s[k] == '-')s[k] = '+';
                    else if(s[k] == '+')s[k] = '-';
                }
            }
            else{
                return steps;
            }
            
            
        }
        else{
            for(int k = 0; k < s.size(); k++){
                if(s[k] == '-'){i = k;break;}
            }
            
            if(i != -1){
                i--;
                for(int k = 0; k <= i; k++){
                    if(s[k] == '+')s[k] = '-';
                }
            }
            else{
                return steps;
            }
        }
        
        steps++;	
    }
    
    
}


int main() {
    freopen("/Users/koushikroy/Desktop/algos/Toph-Contest/inp.txt","r",stdin);
    freopen("/Users/koushikroy/Desktop/algos/Toph-Contest/out.txt","w",stdout);
    int T;
    cin >> T;
    for(int k = 0; k < T; k++){
        cin >> s;
        cout << "Case #" << k+1 << ": " << solve() << endl;
    }
}