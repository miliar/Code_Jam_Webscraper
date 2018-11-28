
#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;
string s;

int solve(int x){
    int ans, smax;
    cin >> smax;
    cin >> s;
    int l = s.length();
    int sum=s[0]-'0';
    ans=0;
    for (int i=1; i<l; i++) {
        int n=s[i]-'0';
        if(i > sum) {
            ans += i-sum;
            sum = i + n;
        } else sum +=n;
    }
    cout << "Case #" << x <<": " << ans << endl;
    return 0;
}

int main(int argc, const char * argv[]) {
    int t;
    scanf("%d", &t);
    for(int x =1; x <=t; x++){
        solve(x);
    }
    return 0;
}
