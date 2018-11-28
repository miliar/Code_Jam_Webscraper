#include<iostream>
#include<string>
#include<cstdio>
#include<cstdlib>
#include<vector>
#include<algorithm>
#define all(x) x.begin(),x.end()
#define tr(container,iterator) for(typeof(container.begin()) iterator=container.begin();iterator!=container.end();++iterator)
#define lli long long int
using namespace std;
lli i,j;

lli solve(vector<int>& v){
    lli people = 0;
    lli shi_l = 0;
    lli res = 0;
    tr(v,it){
        if(shi_l > people and *it > 0){
            res += (shi_l-people);
            people += (shi_l-people);
        }
        people += *it;
        ++shi_l;
    }
    return res;
}

int main(){
    int t,tc=0;
    int s_m;
    string st;
    vector<int> v;
    st.reserve(1005);
    cin >> t;
    while(t--){
        cout << "Case #" << ++tc << ": ";
        cin >> s_m >> st;
        v.clear();
        for(i=0;i<s_m+1;++i){
            v.push_back(st[i]-48);
        }
        cout << solve(v);
        cout << endl;
    }
    return 0;
}