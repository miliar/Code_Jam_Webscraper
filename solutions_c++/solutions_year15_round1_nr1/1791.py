#include<bits/stdc++.h>
using namespace std;

int t;
int n, m[1002];

int main(){

    ifstream in;
    ofstream out;

    in.open("A-large (1).in");
    out.open("Mushroom Monster.txt");

    in >> t;
    for (int tc=1; tc<=t; tc++){
        in >> n;
        for (int i=0; i<n; i++) in >> m[i];

        int ans1 = 0;
        int ans2 = 0;
        int maks = 0;
        for (int i=0; i<n-1; i++){
            if (m[i] > m[i+1]) ans1 += m[i] - m[i+1];
            maks = max(maks, m[i] - m[i+1]);
        }
        for (int i=0; i<n-1; i++) ans2 += min(maks, m[i]);

        out << "Case #" << tc << ": " << ans1 << " " << ans2 << endl;
    }

    in.close();
    out.close();

    return 0;
}
