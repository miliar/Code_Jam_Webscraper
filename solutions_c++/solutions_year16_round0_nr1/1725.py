#include <bits/stdc++.h>

using namespace std;

int main() {
    int T;
    scanf("%d", &T);
    set<long long> s;
    for(int z=1;z<T+1;++z) {
        long long n;
        cin >> n;
        if(n==0){
            printf("Case #%d: INSOMNIA\n", z);
            continue;
        }
        s.clear();
        for(long long i=1;;++i){
            long long temp=i*n;
            while(temp){
                s.insert(temp%10);
                temp/=10;
            }
            if((int)s.size()==10){
                cout << "Case #" << z << ": " << (i*n) << "\n";
                break;
            }
        }
    }
}
