#include <bits/stdc++.h>
#define FOR(i,a) for(i = 0; i < a; i++)
#define FR(i,a,b) for(i = a; i < b; i++)
using namespace std;

int main(){
    long long i,j,T,n,b;
    cin >> T;
    for(int test = 1; test<=T; test++){
        cin >> n;
        int a[2501] = {0};
        vector<int> l;
        FOR(i,2*n-1){
            FOR(j,n){
                cin >> b;
                a[b]++;
            }
        }
        FOR(i,2501){
            if(a[i]%2!=0){
                l.push_back(i);
            }
        }
        cout << "Case #" << test << ": ";
        FOR(i,l.size()){
            cout << l[i] << " ";
        }
        cout << endl;
        // cout << "Case #" << test << ": " << s1 << endl;        
    }
    return 0;
}