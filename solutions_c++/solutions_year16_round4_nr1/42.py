#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <queue>
#include <stack>
#include <algorithm>

using namespace std;
typedef long long ll;

string expand(char c, int n){
    if(n==0){
        string ans = "";
        ans += c;
        return ans;
    }
    string half1, half2;
    if(c=='P'){
        half1 = expand('P', n-1);
        half2 = expand('R', n-1);
    }else if(c=='S'){
        half1 = expand('P', n-1);
        half2 = expand('S', n-1);
    }else if(c=='R'){
        half1 = expand('R', n-1);
        half2 = expand('S', n-1);
    }
    
    if (half1 < half2) return half1 + half2;
    else return half2 + half1;
}

int main(){
    int T;
    cin >> T;
    for(int t=1;t<=T;t++){
        int N, R, P, S;
        cin >> N >> R >> P >> S;
        bool imposs = false;
        for(int i=0;i<N&&!imposs;i++){
            int half = (R+P+S)/2;
            int nR = half - P;
            int nP = half - S;
            int nS = half - R;
            if(nR < 0 || nP < 0 || nS < 0) imposs = true;
            R = nR;
            P = nP;
            S = nS;
        }
        
        if(imposs){
            cout << "Case #" << t << ": IMPOSSIBLE" << endl;    
        }else{
            char ans;
            if(R==1){
                ans = 'R';
            }else if(P==1){
                ans = 'P';
            }else if(S==1){
                ans = 'S';
            }
            
            
            
            cout << "Case #" << t << ": " << expand(ans, N) << endl;
        }
        
    }

    return 0;
}