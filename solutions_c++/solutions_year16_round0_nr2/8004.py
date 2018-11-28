#include <iostream>

using namespace std;

int main() {

    int n;
    cin>>n;
    for(int cases = 0; cases < n; cases++) {
        string s;
        cin>>s;

        int voyBien = s.size()-1;
        for( ; voyBien >= 0; voyBien--) {
            if(s[voyBien] == '-')
                break;
        }

        int cont = 0;

        while(true) {

            int voyBien = s.size()-1;
            for( ; voyBien >= 0; voyBien--) {
                if(s[voyBien] == '-')
                    break;
            }
            if(voyBien == -1)
                break;

            bool isPlus = true;
            if(s[0] == '-') isPlus = false;
            int i = 1;
            for( ; i < s.size(); i++) {
                if(isPlus) {
                    if (s[i] == '+') {
                        // nada
                    } else {
                        break;
                    }
                } else {
                    if (s[i] == '-') {
                        // nada
                    } else {
                        break;
                    }
                }
            }

            if (isPlus && i != s.size())
                for (int j = 0; j < i; j++) {
                        s[j] = '-';
                }


            if(!isPlus) {
                string copia = s;
                int j = 0;
                for (int k = voyBien; k >= 0; k--) {
                    if(copia[k] == '+')
                        s[j++] = '-';
                    else
                        s[j++] = '+';
                }
            }

            //cout << " --->> " << s << endl;

            cont++;
        }

        cout << "Case #" << cases+1 << ": " << cont << endl;
    }

    return 0;
}
