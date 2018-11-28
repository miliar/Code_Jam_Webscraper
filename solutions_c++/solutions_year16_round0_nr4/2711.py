#include<iostream>

using namespace std;

int main(){
    int t, k, c, s;
    cin >> t;
    for (int l = 0; l < t; l++){
        cin >> k >> c >> s;
        cout << "Case #" << l+1 << ": 1";
        if (k == 1)
            cout << "\n";
        else{
            long long aux = 1;
            for (int i = 0; i < c; i++)
                aux *= k;
            if (k == 2)
                cout << " " << aux << "\n";
            else{
                aux /= (k-1);
                for (int i = 1; i < k; i++)
                    cout << " " << 1+i*aux;
                cout << "\n";
            }
        }
    }
    return 0;
}
