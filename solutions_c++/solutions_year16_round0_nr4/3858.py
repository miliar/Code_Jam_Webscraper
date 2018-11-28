#include <bits/stdc++.h>
#define optimizar_ ios_base::sync_with_stdio(0);cin.tie(0);

using namespace std;

long long k, c, s;

int main(){
    optimizar_

    ifstream cin2;
    ofstream cout2;
    cin2.open("a.in", ios::in);
    cout2.open("result.txt", ios::out);

    int T;
    cin2 >> T;

    for(int i = 1; i <= T; i++){
        cout2 << "Case #" << i << ": ";
        cin2 >> k >> c >> s;
        c--;

        for( long long z = 0; z < k; z++ ){
            long long p = z;
            for( long long j = 0; j < c; j++ ){
                p *= k;
                p += z;
            }
            cout2 << " " << p + 1;
        }
        cout2 << "\n";
    }

    cout2 << flush;
    cout2.flush();
    cout2 << endl;

    cin2.close();
    cout2.close();

    return 0;
}