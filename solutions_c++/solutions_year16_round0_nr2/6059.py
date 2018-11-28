#include <bits/stdc++.h>
#define optimizar_ ios_base::sync_with_stdio(0);cin.tie(0);

using namespace std;

string s;

int main(){
    optimizar_

    ifstream cin2;
    ofstream cout2;
    cin2.open("a.in", ios::in);
    cout2.open("result.txt", ios::out);

    int T;
    cin2 >> T;

    for(int i = 1; i <= T; i++){
        cout2 << "Case #" << i << ": ";
        cin2 >> s;

        int cont = 0;
        for(int k = 1; k < s.size(); k++)
            if(s[k] != s[k - 1])
                cont++;

        if(s[s.size() - 1] == '-')
            cont++;
        cout2 << cont << "\n";
    }

    cout2 << flush;
    cout2.flush();
    cout2 << endl;

    cin2.close();
    cout2.close();

    return 0;
}