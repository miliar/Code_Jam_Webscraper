#include <iostream>
using namespace std;

int main() {
    int t;
    cin>> t;
    for(int ti=1;ti<=t;++ti){
        int a, b, k; cin>>a>>b>>k;
        int cnt = 0;
        for(int i=0;i<a;++i) {
            for(int j=0;j<b;++j){
                if( int(i & j) < k ) cnt ++;
            }
        }
        cout << "Case #" << ti << ": " << cnt << endl;
    }
    return 0;
}
