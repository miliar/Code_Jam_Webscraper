#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
string s;
int dp[1005];

string solve(int start, int end) {
    //cout<<start<<" "<<end<<endl;
    string ans;
    if(start > end) return "";        
    if(start == end) {
        ans += s[start];
        return ans;
    }
    ans += s[dp[end]];    
    string x = solve(start, dp[end]-1);
    //cout<<x<<" ";
    ans += x;
    //cout<<ans<<endl;
    for(int i = dp[end]+1;i<=end;i++) {
        ans += s[i];
    }
    //cout<<ans<<endl;
    return ans;
}

string process() {
    int len = s.length();
    dp[0] = 0;
    for(int i=1;i<len;i++) {
        if(s[i] >= s[dp[i-1]]) {
            dp[i] = i;
        } else {
            dp[i] = dp[i-1];
        }
    }    
    return solve(0, len-1);    
}

int main(){
    int t;
    cin>>t;
    for(int i=1;i<=t;i++) {
        cin>>s;
        string ans = process();
        cout<<"Case #"<<i<<": "<<ans<<endl;
    }
    
    return 0;
}
