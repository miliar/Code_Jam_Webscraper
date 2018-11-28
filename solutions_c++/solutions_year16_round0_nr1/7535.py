#include <bits/stdc++.h>

//Team UzhNU_MagicalPony
//Author Egor Bobyk

using namespace std;

const long long md = 1e9 + 7;

bool f[11];

int main(){
    freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);

    //freopen("quant.in","r",stdin);
    //freopen("quant.out","w",stdout);

    int tests;
    cin>>tests;
    int t = 0;
    while (tests--){
        for (int i = 0; i <= 9; i++){
            f[i] = false;
        }
        long long n;
        cin>>n;
        t++;
        cout<<"Case #"<<t<<": ";
        if (n == 0) {cout<<"INSOMNIA"<<endl; continue;}
        int kol = 0;
        int k = 0;
        while (true){
            k++;
            long long nn = n*k;
            while (nn){
                int q = nn % 10;
                if (f[q] == false) {f[q] = true; kol++;}
                if (kol == 10) break;
                nn /= 10;
            }
            if (kol == 10) break;
        }
        cout<<n*k<<endl;
    }

}
