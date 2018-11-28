#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#define max 1000
using namespace std;
string s;
int dp[max];
long process() {
    long ans = 0;
    int len = s.length();
    int i=0;
    while(i<len) {
        if(s[i] == '-') {
            while(s[i] == '-') i++;
            ans++;
        }
        else {
            while(s[i] == '+') i++;
            if(!(i<len)) break;
            while(s[i] == '-') i++;
            ans += 2;
        }        
    }
    return ans;
}
long processdp() {    
    int len = s.length();    
    for(int i=0;i<len;i++) dp[i] = 0;
    if(s[0] == '-') dp[0] = 1;
    else dp[0] = 0;
    for(int i=1;i<len;i++) {
        if(s[i] == '-') {
            if(s[i-1] == '+') dp[i] = dp[i-1]+2;
            else dp[i] = dp[i-1];
        }
        else {
            dp[i] = dp[i-1];
        }
    }
    return dp[len-1];
}

int main(){
    int t;
    cin>>t;    
    for(int i=1;i<=t;i++) {
        cin>>s;
        long ans = processdp();
        cout<<"Case #"<<i<<": "<<ans<<endl;        
    }
    return 0;
}
