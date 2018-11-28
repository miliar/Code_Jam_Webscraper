#include<bits/stdc++.h>

using namespace std;

void solve(){
    string s;
    cin >> s;

    deque<char> cs;

    for(char c: s){
        if(cs.size()){
            if(cs.front() > c){
                cs.push_back(c);
            }else{
                cs.push_front(c);
            }
        }else{
            cs.push_back(c);
        }
    }

    cout << string(cs.begin(), cs.end()) << endl;
}

int main(){

    int N;
    cin >> N;

    for(int i=0;i<N;i++){
        cout << "Case #" << i+1<< ": ";
        solve();
    }

    return 0;
}
