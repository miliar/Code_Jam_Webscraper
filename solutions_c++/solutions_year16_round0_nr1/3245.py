#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int main() {

    ll t, n, m, i, j, k, b, x;
    cin>>t;
    ll T = t;
    while(t--) {
        bool a[10] = {0};
        k = 0;
        cin>>n;
        if (n==0) {
            cout<<"Case #"<<(T-t)<<": "<<"INSOMNIA"<<endl;
            continue;        }
        i = 1;
        while(true) {
            m = n*i;
            while(m!=0) {
                if (a[m%10]==0) {
                   a[m%10] = 1;
                   k++; 
                }
                m/=10;
            }
            if (k==10) {
                m = n*i;
                break;
            }
            i++;
        }
        cout<<"Case #"<<(T-t)<<": "<<m<<endl;



    }


    return 0;

}