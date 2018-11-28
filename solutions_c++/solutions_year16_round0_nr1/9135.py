#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

vector<int> a(10);

int main()
{
    ll n,t,j;

    freopen("large.in", "r", stdin);
    freopen("output.txt", "w", stdout);

    cin >> n;

    for(int i=0;i<n;i++){
        cin >> t;
        if(t == 0)
            cout << "Case #" << i+1 << ": INSOMNIA\n";
        else{
            a.assign(10,0);
            for(j = 1; ; j++){
                int tr = 1;
                ll p = t * j;

                while(p!=0){
                    ll k = p%10;
                    a[k]++;
                    p/=10;
                }

                for(int v = 0; v < 10; v++){
                    if(a[v] == 0){
                        tr = 0;
                    }
                }

                if(tr == 1) break;
            }
            cout << "Case #" << i+1 << ": " << t * j << "\n";
        }
    }


    return 0;
}
