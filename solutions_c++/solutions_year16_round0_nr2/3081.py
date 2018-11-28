#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<int, int> pii;
#define mp make_pair
#define fst first
#define snd second
#define fr(i, a, b) for(int i=a; i<b; i++)


void main2() {
    string s;
    cin>>s;
    bool find = true;
    int cnt = 0;
    for(int i=0; i<s.size(); i++) {
        if(s[i]=='-'&&find) {
            find = false; cnt++;
        } else if(s[i]=='+') find = true;
    }
    if(s[0]=='-') {
        cout<<2*cnt-1<<endl;
    } else {
        cout<<2*cnt<<endl;
    }
}

int main() {
    int T;
    cin>>T;
    for(int i=1; i<=T; i++) {
        cout<<"Case #"<<i<<": ";
        main2();
    }
}
