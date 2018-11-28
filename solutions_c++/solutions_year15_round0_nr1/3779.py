#include <cstdio>
#include <iostream>

using namespace std;

int T, MX;
string S;

int main(){

        cin >> T;

        for(int cas=1; cas<=T; cas++){
                cin >> MX;
                cin >> S;

                int ct = 0;
                int fr = 0;
                for(int pos = 0; pos<= MX; pos++){
                        int nm = S[pos] - '0';
                        if( fr + ct < pos) fr++;
                        ct += nm;

                }
                cout << "Case #" << cas << ": " << fr << "\n";

        }

        return 0;
}
