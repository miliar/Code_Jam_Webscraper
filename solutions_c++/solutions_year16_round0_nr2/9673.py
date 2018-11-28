#include<iostream>

#include<cstdio>
#include<algorithm>

#include<queue>

#define forn(a,b) for(int a = 0; a < int(b); ++a)
#define forr(a,c,b) for(int a = int(c); a < int(b); ++a)
using namespace std;
typedef long long ll;

int NN;

int greedy(string s){
    int sumpene = 0;
    for(int i = 1; i<s.size(); ++i)
        if( s[i] != s[i-1] ) ++sumpene;
    if( s.back() == '-' ) ++sumpene;
    return sumpene;
}

int main(){
    freopen("entrada.in", "r", stdin);
    freopen("salida.txt", "w", stdout);
    string svulva;

    cin>>NN;
    forn(i, NN){
        cin>>svulva;
        cout<<"Case #"<<i+1<<": "<<greedy(svulva)<<endl;
    }

    return 0;
}
