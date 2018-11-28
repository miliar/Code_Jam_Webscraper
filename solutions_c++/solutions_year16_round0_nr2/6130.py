#include <bits/stdc++.h>
#define endl '\n'
using namespace std;
bool checar(string s) {
    for(char c:s) if(c=='-') return false;
    return true;
}
string invertir(string s) {
    reverse(s.begin(),s.end());
    return s;
}
string cambiar(string s) {
    string s1="";
    for(char c:s) {
        if(c=='-') s1+="+";
        else s1+="-";
    }
    return s1;
}
int contar(string s) {
    int cont =0;
    for(char c:s)
        if(c =='-')
            cont++;
    return cont;
}
string mover(int i, string s) {

    string sub1 = s.substr(0,i);
    string sub2 = s.substr(i,s.length() );
    return cambiar(invertir(sub1))+sub2;
}
int main() {
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    int n;
    cin >> n;
    for(int caso=1; caso<=n; caso++) {
        string str;
        cin >> str;
        int res=0;
        int indx=0;
        while(!checar(str)) {
            if(str[indx] == '-') {
                for( int i=0; i<str.length() ; i++) {
                    if(str[i] == '-') {
                        indx=i;
                    }
                }
                indx++;
            } else {
                for(indx=0; indx<str.length(); indx++) {
                    if(str[indx]=='-') break;
                }
            }
            str = mover(indx,str);
            res++;
        }
        cout << "Case #" << caso << ": " << res <<endl;
    }
    return 0;
}

