#include <bits/stdc++.h>
#include <fstream>
using namespace std;
ifstream fentrada("A-large.in");
ofstream fsalida("respuestalarga.out");

int main(){
    int t; fentrada >> t;
    //cin >> t;
    for( int i = 1 ; i <= t ; ++i ){
        int n, c = 1, cur, aux; fentrada >> n;
        //cin >> n;
        set<int>st;
        bool ok = true;
        while((int)st.size() < 10 && ok ){
            cur = c*n;
            if(cur == 0){
                fsalida << "Case #" << i << ": INSOMNIA\n";
                //cout << "Case #" << i << ": INSOMNIA\n";
                ok = false;
            }
            aux = cur;
            while(cur != 0 ){
                st.insert(cur%10);
                cur/=10;
            }
            c++;
        }
        if(ok) fsalida << "Case #" << i << ": " << aux << '\n';
            //cout << "Case #" << i << ": " << aux << '\n';
    }
}
