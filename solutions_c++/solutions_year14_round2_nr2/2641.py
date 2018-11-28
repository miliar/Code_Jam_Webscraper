#include <iostream>
#include <cstring>
using namespace std;

int main(){
    int t;
    int a, b, k;
    cin >> t;
    for(int tt = 1; tt <= t; tt++){
        int tot = 0;
        cout << "Case #" << tt << ": " ;
        cin  >> a >> b >> k;
        for(int i = 0; i < a; i++)
            for(int j = 0; j < b; j++)
                tot += (i & j) < k;
        cout << tot << endl;
    }
    return 0;
}
