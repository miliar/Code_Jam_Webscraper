#include <bits/stdc++.h>

using namespace std;

int main(){
    int t;
    cin >> t;
    int index=1;
    while(t--){
        set<long long int> S;
        long long int n;
        cin >> n;
        long long int ans=1;
        if(n==0){
            cout << "Case #" << index++ << ": " << "INSOMNIA" << endl;
            continue;
        }
        for(int i=1;;++i){
            long long int f=i*n;
            while(f){
                S.insert(f%10);
                f=f/10;
            }
            if(S.size()==10){
                ans=i*n;
                break;
            }
        }
       cout << "Case #" << index++ << ": " << ans << endl;

    }
    return 0;
}
