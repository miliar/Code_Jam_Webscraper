#include <bits/stdc++.h>
#define endl '\n'
using namespace std;
int arr[10];
int digitos(string str) {
    for(char c:str) arr[c-'0']=1;
}
bool check() {
    for(int i=0; i<10; i++) if(arr[i]==0) return false;
    return true;
}

int main() {
    cin.tie(0);
    ios_base::sync_with_stdio(0);
    int n,x;
    cin >> n;
    for(int caso=1; caso<=n; caso++) {
        memset(arr,0,sizeof arr);
        cin >> x;
        if(x==0) cout <<"Case #"<<caso<<": INSOMNIA"<<endl;
        else {
            int i=x;
            while(true) {
                digitos(to_string(i));
                if(check()) {
                    cout <<"Case #"<<caso<<": "<<i<<endl;
                    break;
                }
                i+=x;
            }

        }
    }
    return 0;
}

