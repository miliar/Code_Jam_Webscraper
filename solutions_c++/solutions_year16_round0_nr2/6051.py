#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int cnt = 0;
string s;
stack <char> data;
bool f = 0;

void solve(){
    //mission complete check
    stack <char> st = data;
    bool f1 = 0;
    while(!st.empty()){
        if(st.top() == '-')
            f1 = 1;
        st.pop();
    }
    if(!f1){
        f = 1;
        cnt--;
        return;
    }

    char cur = data.top();
    vector <char> tmp;

    //start with negative sign
    if(cur == '-'){
        while(!data.empty() && data.top() == '-'){
            tmp.push_back('+');
            data.pop();
        }
    }
    //start with positive sign
    else{
        while(!data.empty() && data.top() == '+'){
            tmp.push_back('-');
            data.pop();
        }
    }
    for(int i = 0; i < tmp.size(); i++)
        data.push(tmp[i]);
}
int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t; cin >> t;
    int c = 1;
    while(t--){
        cout << "Case #"<<c++ <<": ";
        while(!data.empty())
            data.pop();

        cin >> s;
        for(int i = s.size()-1; i >= 0; i--)
            data.push(s[i]);
        cnt = 0;
        f = 0;

        while(!f){
            cnt++;
            solve();
        }

        cout << cnt << "\n";

    }
    return 0;
}
