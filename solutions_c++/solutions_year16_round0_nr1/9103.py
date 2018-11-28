#include <iostream>
#include <fstream>

using namespace std;

int T, s;
int Ap[17];

///ifstream cin("a.in");
///ofstream cout("a.out");

int main(){
    cin >> T;
    int x = 0;
    while(T--){
        cin >> s;
        ++x;
        cout << "Case #" << x << ": ";
        if(s == 0)
            cout << "INSOMNIA" << "\n";
        else{
            int ok = 1, w = s;
            for(int i = 0; i <= 9; ++i)
                Ap[i] = 0;
            while(ok == 1){
                int l = w;
                while(l > 0){
                    Ap[l % 10] = 1;
                    l /= 10;
                }
                ok = 0;
                for(int i = 0; i <= 9; ++i)
                    if(Ap[i] == 0)
                        ok = 1;
                if(ok == 1)
                    w = w + s;
            }
            cout << w << "\n";
        }
    }
    return 0;
}
