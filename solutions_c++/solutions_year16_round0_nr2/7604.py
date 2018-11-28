#include <bits/stdc++.h>
using namespace std;
int main(){
    freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int test;
    cin >> test;
    for(int i=1;i<=test;i++){
        string s;
        cin >> s;
        stack <char> ez;
        for(int i=0;i<s.size();i++)
            if (!ez.size() || ez.top() != s[i]) ez.push(s[i]);
        if (ez.top() == '+') ez.pop();
        cout << "Case #"<< i << ": " << ez.size() << endl;
    }
}
