#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<int, int> pii;
#define mp make_pair
#define fst first
#define snd second
#define fr(i, a, b) for(int i=a; i<b; i++)

int a[10];
set<ll> m;
ll num;

bool ok() {
    bool res = true;
    for(int i=0; i<=9; i++) if(a[i]==0) res = false;
    return res;
}


void main2() {
     m.clear();
     memset(a, 0, sizeof a);
     cin>>num;
     ll n = num;
     while(!ok()) {
         ll temp = n;
         while(temp) {
             a[temp%10] = 1;
             temp/=10;
         }
         if(ok()) {
             cout << n << endl; break;
         } else if(m.count(n)) {
             cout << "INSOMNIA" << endl; break;
         }
         m.insert(n);
         n += num;
     }
}

int main() {
    int T;
    cin>>T;
    for(int i=1; i<=T; i++) {
        cout<<"Case #"<<i<<": ";
        main2();
    }
}
