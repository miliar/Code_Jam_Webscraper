#include <bits/stdc++.h>

using namespace std;

int main() {
    int T;
    scanf("%d", &T);
    for(int z=1;z<T+1;++z) {
        long long k,c,s;
        cin >> k >> c >> s;
        cout << "Case #" << z << ":" ;
        for(long long i=1;i<=powl(k,c);i+=powl(k,c)/k){
            cout << " " << i;
        }
        cout << endl;
    }
    return 0;
}
