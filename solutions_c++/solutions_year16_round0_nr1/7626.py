#include<bits/stdc++.h>

using namespace std;

int main(){
    ifstream fin("inputt.txt");
    ofstream fout("output.txt");
    #define cin fin
    #define cout fout
    long long n;
    cin >> n;
    for(int i = 0; i < n; ++i){
        int x;
        cin >> x;
        if(x == 0){
            cout << "Case #" << i + 1 << ": INSOMNIA\n";
            continue;
        }
        int y = 0;
        vector<bool> v(10, false);
        int k = 0;
        while(k != 10){
            y += x;
            int yy = y;
            while(yy != 0){
                if(v[yy % 10] == false){
                    v[yy % 10] = true;
                    ++k;
                }
                yy /= 10;
            }
        }
        cout << "Case #" << i + 1 << ": " << y << endl;
    }
}
