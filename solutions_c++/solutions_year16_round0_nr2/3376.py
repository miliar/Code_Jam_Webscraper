#include<iostream>
#include<string>

using namespace std;

int main(){
    int t, out, i;
    string aux;
    cin >> t;
    for (int l = 0; l < t; l++){
        cin >> aux;
        out = 0;
        i = 0;
        if (aux[0] == '-'){
            out = 1;
            while (i < aux.size() && aux[i] == '-')
                i++;
        }
        while (i < aux.size()){
            if (aux[i] == '+')
                i++;
            else{
                out += 2;
                while (i < aux.size() && aux[i] == '-')
                    i++;
            }
        }
        cout << "Case #" << l+1 << ": " << out << "\n";
    }
    return 0;
}
