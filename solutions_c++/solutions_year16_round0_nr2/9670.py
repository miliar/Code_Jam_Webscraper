#include<iostream>
#include<cstdio>
#include<algorithm>
#include<queue>
#define forn(a,b) for(int a = 0; a < int(b); ++a)
#define forr(a,c,b) for(int a = int(c); a < int(b); ++a)
using namespace std;
typedef long long ll;

int N;

int greedy(string s){
    int sum = 0;
    for(int i = 1; i<s.size(); ++i)
        if( s[i] != s[i-1] ) ++sum;
    if( s.back() == '-' ) ++sum;
    return sum;
}

int main(){
    freopen("entrada.in", "r", stdin);
    freopen("salida.txt", "w", stdout);
    string s;

    cin>>N;
    forn(i, N){
        cin>>s;
        cout<<"Case #"<<i+1<<": "<<greedy(s)<<endl;
    }

    return 0;
}
