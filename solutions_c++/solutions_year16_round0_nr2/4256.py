#include <iostream>
#include <string>
#include <queue>
#include <set>

using namespace std;

char flip(char c){
    if(c == '+'){
        return '-';
    }
    return '+';
}

string flip_from(string s, int n){
    for(int i = 0; i < n; i++){
        s[i] = flip(s[i]);
    }
    return s;
}

bool all_happy(string s){
    for(int i = 0; i < s.size(); i++){
        if(s[i] != '+'){
            return false;
        }
    }
    return true;
}

int bfs(string s){
    set <string> considered;
    queue <pair <int, string> > que;
    que.push(pair <int, string>(0, s));
    considered.insert(s);
    while(1){
        //cout << que.size() << endl;
        pair <int, string> p = que.front();
        que.pop();
        if(all_happy(p.second)){
            return p.first;
        } else {
            for(int i = 1; i <= p.second.size(); i++){
                string candidate = flip_from(p.second, i);
                if(considered.find(candidate) != considered.end()){
                    continue;
                } else{
                    considered.insert(candidate);
                    que.push(pair <int, string> (p.first + 1, candidate));
                }
            }
        }
    }
}

void solve(){
    string s; 
    cin >> s;

    cout << bfs(s) << endl;
}

int main(){
    int T;
    cin >> T;
    for(int i = 0; i < T; i++){
        cout << "Case #" << i + 1 << ": ";
        solve();
    }
    return 0;
}
