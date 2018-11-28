#include <bits/stdc++.h>

using namespace std;
int main(){
    freopen("test.in","r",stdin);
    freopen("test.out","w",stdout);
    int T;
    cin >> T;
    int t = 1;
    while(T--){
        cout << "Case #"<<t++<<": ";
        long long k;
        long long c;
        long long s;
        cin >> k >> c >> s;
        long long temp = 1;
        long long acc = 1;
        for(int i=0;i<c-1;i++)temp*=k, acc+=temp;
        for(int i=0;i<k;i++)cout <<acc*i+1 << " ";
        cout << endl;
    }
    return 0;
}
