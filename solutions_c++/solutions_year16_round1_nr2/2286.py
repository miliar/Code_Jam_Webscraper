#include <bits/stdc++.h>
using namespace std;

int main(){
    int t, caso = 1, n, minimo, aux;
    map<int, int> dici;
    vector<int>lista;
    cin >> t;
    while(caso <= t){
        dici.clear();
        lista.clear();
        cin >> n;
        for (int i = 0; i < 2*n-1; ++i){
            for (int j = 0; j < n; ++j){
                cin >> aux;
                dici[aux]++;
            }
        }
        
        typedef std::map<int, int>::iterator it_type;
        for(it_type iterator = dici.begin(); iterator != dici.end(); iterator++) {
            // iterator->first = key
            // iterator->second = value
            if(iterator->second % 2 == 1)
                lista.push_back(iterator->first);
        }
        sort(lista.begin(), lista.end());

        cout << "Case #" << caso << ":";
        for (int i = 0; i < lista.size(); ++i){
            cout << " " << lista[i];
        }
        cout << endl;
        caso++;
    }

    return 0;
}