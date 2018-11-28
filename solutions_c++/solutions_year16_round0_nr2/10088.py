#include<cmath>
#include<cstdlib>
#include<string>
#include<sstream>
#include<vector>
#include<iostream>
#include<queue>
#include<deque>
#include<map>
#include<set>
#include<stack>
#include<list>
#include<algorithm>
using namespace std;

bool all_happy(string s){
    for(int i=0; i<s.size(); i++){
        if(s[i] == '-') return false;
    }
    return true;
}

string flipped(string s, int i){
    string r = "";
    for(int j=0; j<i; j++){
        if(s[j] == '-') r += '+';
        if(s[j] == '+') r += '-';
    }
    for(int j=i; j<s.size(); j++){
        r += s[j];
    }
    return r;
}

void solve(int t, string s){
    set<string> searched;
    int l = s.size();
    string snew;
    queue<string> q, qnew;
    if(all_happy(s)) cout << "Case #" << t << ": " << 0 << endl;
    else{
        int n = 1;
        q.push(s);
        while(true){
            qnew = queue<string>();
            while(!q.empty()){
                string r = q.front();
                searched.insert(r);
                q.pop();
                for(int i=1; i<l+1; i++){
                    snew = flipped(r, i);
                    if(all_happy(snew)){
                        cout << "Case #" << t << ": " << n << endl;
                        return;
                    }
                    if(searched.find(snew) == searched.end())
                        qnew.push(snew);
                }
            }
            n++;
            q = qnew;
        }
    }
}

int main(){
    int T;
    cin >> T;
    for(int t=1; t<=T; t++){
        string s;
        cin >> s;
        solve(t, s);
    }
}
