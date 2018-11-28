#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <queue>
#include <stack>
#include <algorithm>

using namespace std;
typedef long long ll;

int main(){
    int T;
    cin >> T;
    for(int t=1;t<=T;t++){
        string S;
        cin >> S;
        
        int miss = 0;
        for(int i=0;i<S.length();i++){
            if(S[i]=='C'){
                if(i%2==0) miss++;
                else miss--;
            }
        }
        
        if(miss<0) miss=-miss;
        cout << "Case #" << t << ": " << 5*(S.length()-miss) << endl;
        /*
        stack<char> pre;
        pre.push(S[0]);
        int miss = 0;
        for(int i=1;i<S.length();i++){
            if(!pre.empty() && S[i]==pre.top()){
                pre.pop();
            }else{
                pre.push(S[i]);
            }
        }
        
        while(!pre.empty()){
            pre.pop();
            miss++;
        }
        cout << "Case #" << t << ": " << 5*(S.length()-miss/2) << endl;*/
    }

    return 0;
}