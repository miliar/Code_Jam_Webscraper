#include <deque>
#include <iostream>
#include <string>
using namespace std;

int main(){
    int T; cin>>T;
    for (int t = 1; t <= T ; t++) {
        string s; cin>>s;
        deque<char> word;
        word.push_back(s.front());
        for (int i = 1; i < s.length(); ++i) {
            if((int)s[i] >= (int) word.front()){
                word.push_front(s[i]);
            } else {
                word.push_back(s[i]);
            }
        }
        
        cout<<"Case #"<<t<<": ";
        for (auto & c: word) {
            cout<<c;
        }
        cout<<"\n";
    }
    
}