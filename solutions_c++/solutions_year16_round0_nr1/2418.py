#include <bits/stdc++.h>

using namespace std;
#define int long long
const int maxn = 11;
bool mark[maxn];
int Cnt = 0;
void doo(int x){
    while(x){
        int t = x % 10;
        if(!mark[t]) Cnt++;
        mark[t] = 1;
        x /= 10;
    }
}
int f(int x){
    Cnt = 0;
    memset(mark, 0, sizeof mark);
    if(x == 0) return -1;
    for(int i=x; i; i += x){
        doo(i);
        if(Cnt == 10)
            return i;
    }
}
int jav[1000010];
main(){
    for(int i=0; i<=1000000; i++)
        jav[i] = f(i);
    freopen("A-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    ios::sync_with_stdio(false);
    cin.tie(false);
    int T;
    cin >> T;
    for(int i=0; i<T; i++){
        cout << "Case #" << i + 1 << ": ";
        int x;
        cin >> x;
        if(jav[x] == -1)
            cout << "INSOMNIA" << endl;
        else
            cout << jav[x] << endl;
    }
}
