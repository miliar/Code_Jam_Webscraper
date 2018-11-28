#include <cstdio>
#include <iostream>
#include <cstring>

using namespace std;

int rev(int x) {
    int ans = 0;
    while(x) {
        ans *= 10;
        ans += x%10;
        x = x/10;
    }
    return ans;
}

bool isPalin(int x) {
    int y=rev(x);
    if(y == x) return true;
    else return false;
}

int main() {
    int fs[2009];
    memset(fs, 0, sizeof(fs));
    for(int i=0; i<101; i++) {
        if(isPalin(i) && isPalin(i*i)) {
            fs[i*i] = 1;
        }
    }
    int t,A,B;
    cin>>t;
    int tp = 0;
    while(t--) {
        tp ++;
        cin>>A>>B;
        int cnt = 0;
        for(int i=A; i<=B; i++) {
            if(fs[i] == 1) cnt++;
        }
        cout<<"Case #"<<tp<<": "<<cnt<<endl;
    }
    return 0;
}
