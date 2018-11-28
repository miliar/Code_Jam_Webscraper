#include<bits/stdc++.h>
#include <string>

using namespace std;

int main(){
    freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
    int tc;
    cin >> tc;
    for(int tci = 0; tci < tc; tci++){
            long long a;
            cin >> a;
            if(a == 0){
                cout << "Case #" << tci+1 << ": INSOMNIA"  << endl;
            }
            else{
                int st = 0;
                string str;
                long long aux, aux2;
                int mult = 1;
                while(st != 1023){
                    aux = a * mult;
                    stringstream ss;
                    ss << aux;
                    str = ss.str();
                    //cout << "aux " << aux << endl;
                    //cout << "string " << str << endl;
                    //cout << "st " << st << endl;
                    //getchar();
                    for(int i = 0; i < str.size(); i++) {
                        int digito = str[i] - '0';
                        //cout << "digito " << digito << endl;
                        //cout << "bit " << (1 << digito) << endl;
                        //cout << "bit " << (st | (1 << digito)) << endl;
                        st |= (1 << digito);
                    }
                    mult++;
                }
                cout << "Case #" << tci+1 << ": " << str<< endl;

            }

    }
    return 0;
}
