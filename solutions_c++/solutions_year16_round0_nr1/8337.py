#include <bits/stdc++.h>
#define filename "A-large.in"
using namespace std;

const int N = 1e6+10;



int main(){
    freopen(filename,"r", stdin);
    freopen("output.txt", "w", stdout);
    set<int> a;
    int ans[N];
    for(int i = 1; i < N; ++i){
        int mp = 1;
        int cr = i;
        while(a.size() < 10){
            while(cr){
                a.insert(cr%10);
                cr /= 10;
            }
            cr = i * ++mp;
        }
        ans[i] = --mp * i;
        a.clear();
    }
    int test;
    int x;
    cin >> test;
    for(int i = 1; i <= test; ++i){
        cin >> x;
        cout << "Case #" << i << ": ";
        if(x) cout << ans[x]<< endl;
        else cout << "INSOMNIA\n";
    }
    return 0;
}