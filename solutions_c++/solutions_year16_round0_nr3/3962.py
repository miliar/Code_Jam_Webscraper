#include <bits/stdc++.h>
using namespace std;

string toBinary(long long n) {
    string r;
    while(n!=0) {r+=(n%2==0 ?"0":"1"); n/=2;}
    return r;
}

map<int, vector<int>> ans;

bool prime_check(long long num) {
    if(num<2) return 0;
    if(num % 2 ==0 && num!=2) return 0;
    for(int i = 3; i*i <= num; i++) {
        if(num % i == 0) return 0;
    }
    return 1;
}

map<string,int> xx;

void solve() {
    int n,j;
    cin>>n>>j;
    string p;
    ans.clear();
    
    
    for(long long i=(1<<(n-1))+1 ; j ; i++, i++) {
        p = toBinary(i);
        //cerr<<i<<" "<<endl;

        vector<int> zz;
        zz.clear();
        for(int j=2 ; j<= 10 ; j++) {
            long long s=0,k=1;
            for(auto v:p) {
                if (v=='1') {
                    s+=k;
                }
                k*=j;
            }
            //cerr<<s<<" "<<endl;

            if(s % 2 ==0) {
                zz.emplace_back(2);
                continue;
            }
            int zv =sqrt(s);
            for(int k = 3; k <= zv; k+=2) {
                if(s % k == 0) {
                   // cerr<<s<<" "<<k<<" "<<endl;
                    zz.emplace_back(k);
                    break;
                }
            }
        }
        if (zz.size()==9) {
            string zp = toBinary(i);
            reverse(zp.begin(), zp.end());
            string q = zp;

            if (xx[q]) {
                continue;
            }
            j--;
            xx[q] = 1;
            //cerr<<j<<" CASE "<<endl;

            cout<<q<<" ";
            for(auto k:zz) {
                cout<<k<<" ";
            }
            cout<<endl;

        }
        
    }
}

int main(int argc, const char **argv) {
    if(argc>=2) {
        freopen(argv[1], "r", stdin);
        freopen(argv[2], "w", stdout);
    }
    int T;
    cin>>T;
    
    for(int t=1 ; t<=T ; t++) {
        cout<<"Case #"<<t<<": \n";
        
        solve();
    }

}
