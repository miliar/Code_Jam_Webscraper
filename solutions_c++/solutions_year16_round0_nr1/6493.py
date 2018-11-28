#include<bits/stdc++.h>
using namespace std;
#define pb push_back
#define mp make_pair
typedef long long ll;
typedef long long unsigned llu;
typedef pair<int, int> pii;
typedef vector<int> vi;
int main() {
    int n, t;
    cin>>t;
    for(int k = 1; k <= t; ++k) {
        cin>>n;
        cout<<"Case #"<<k<<": ";
        int a[10] = {0};
        if(n == 0) {
            cout<<"INSOMNIA"<<endl;
            continue;
        }
        for(int i = 1; i > 0; ++i) {
            int p = i*n;
            while(p) {
                a[p%10] = 1;
                p /= 10;
            }
            int flg = 1;
            for(int j = 0; j < 10; ++j) {
                if(a[j] == 0) {
                    flg = 0;
                    break;
                }
            }
            if(flg == 1) {
                cout<<i*n<<endl;
                break;
            }
        }
    }
    return 0;
}

