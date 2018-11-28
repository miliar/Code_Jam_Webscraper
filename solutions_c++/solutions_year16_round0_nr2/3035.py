#include <bits/stdc++.h>
using namespace std;

int test;
string s;
void input(){
    cin>>s;
}

void sol(){
    test++;

    int ans=(s.back()=='-');
    for (int i=1;i<s.size();i++)
        ans+=(s[i]!=s[i-1]);
    cout<<"Case #"<<test<<": "<<ans<<endl;
}

int main() {
    freopen("B-large.in","r",stdin);
    freopen("B1.txt","w",stdout);
    int t;
    cin>>t;
    while (t--){
        input();
        sol();
    }
    return 0;
}
