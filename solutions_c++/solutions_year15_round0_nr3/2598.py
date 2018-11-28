#include <bits/stdc++.h>
#define optimizar ios_base::sync_with_stdio(0); cin.tie(0)
using namespace std;

int n, m;
string a;

string _real;

void replica() {
    _real.clear();
    for(int i = 1; i<=m; i++) {
        for(int j = 0; j < a.size(); j++)
            _real.push_back(a[j]);
    }
}

int busca(int pos, char car) {
    char aux = 1;
    int negativo = 0;
    while((aux != car || negativo) && pos + 1 < _real.size()) {
        pos++;
        if(aux == 1) {
            aux = _real[pos];
        } else {
            if(aux == _real[pos]) {
                aux = 1;
                negativo^= 1;
            } else {
                if(aux == 'i') {
                    if(_real[pos] == 'j') aux = 'k';
                    if(_real[pos] == 'k') {
                        negativo^=1;
                        aux = 'j';
                    }
                } else {
                    if(aux == 'j') {
                        if(_real[pos] == 'i') {
                            negativo^=1;
                            aux = 'k';
                        }
                        if(_real[pos] == 'k') aux = 'i';
                    }  else {
                        if(_real[pos] == 'i') aux = 'j';
                        if(_real[pos] == 'j') {
                            negativo^=1;
                            aux = 'i';
                        }
                    }
                }
            }
        }
    }

    if(aux == car && !negativo)
        return pos;

    return _real.size();
}

bool cmp(int pos) {
    char aux = 1;
    int negativo = 0;
    while(pos + 1 < _real.size()) {
        pos++;
        if(aux == 1) {
            aux = _real[pos];
        } else {
            if(aux == _real[pos]) {
                aux = 1;
                negativo^= 1;
            } else {
                if(aux == 'i') {
                    if(_real[pos] == 'j') aux = 'k';
                    if(_real[pos] == 'k') {
                        negativo^=1;
                        aux = 'j';
                    }
                } else {
                    if(aux == 'j') {
                        if(_real[pos] == 'i') {
                            negativo^=1;
                            aux = 'k';
                        }
                        if(_real[pos] == 'k') aux = 'i';
                    }  else {
                        if(_real[pos] == 'i') aux = 'j';
                        if(_real[pos] == 'j') {
                            negativo^=1;
                            aux = 'i';
                        }
                    }
                }
            }
        }
    }
    if(aux == 1 && !negativo)
        return true;
    return false;
}

bool can_solve() {
    int pos = busca(-1, 'i');
    pos = busca(pos, 'j');
    pos = busca(pos, 'k');
    if(pos >= _real.size()) return false;
    return cmp(pos);
}

int main()
{
    freopen("case.txt", "r", stdin);
    freopen("case.out", "w", stdout);
    optimizar;
    int T;
    cin >> T;
    for(int cases = 1; cases <= T; cases++) {
        cin >> n >> m;
        cin >> a;
        replica();
        cout << "Case #" << cases << ": ";
        if(can_solve())
            cout << "YES\n";
        else
            cout << "NO\n";
    }
    return 0;
}
