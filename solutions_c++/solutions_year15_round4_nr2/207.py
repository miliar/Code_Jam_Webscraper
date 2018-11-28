

#include <iostream>
#include <functional>
#include <algorithm>
#include <utility>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <bitset>
#include <unordered_set>
#include <unordered_map>

using namespace std;

typedef long long ll;


int answer(int x) {
    int s=1;
    for (int i = 1; i <=x; ++i)
    {
        //cout << s << endl;
        s = s*i ;
        while(s%10==0) s/=10;
        s = s%10000;
    }
    cout << s << endl;
    return s%10;
}


int g(int &x) {
    while(x%10==0) x/=10;
    x%=100;
    return x;
}

int mul(int& x, int num) {
    x = (x*num)%10;
    g(x);
}

int main() {

    freopen("//Users//osw//Desktop//in.txt", "r", stdin);
    
    int T, t = 0;
    cin >> T;
    while (T-(t++)) {
        int n; cin >> n;
        
        vector<int> v;
        for (int i = 0; i < n; ++i) {
            string s;   cin >> s;
            for (auto ch:s) v.push_back(ch-'0');
        }
        for (auto x:v) cout << x; cout << endl;cout << endl;

        int ans=1;
        int xx=0;

        vector<int> fig(10,1);
        vector<int> t(10,1);

        for (int i = 0; i < 10; ++i) cout << i << '\t'; cout << endl;

        for (auto &x:v) {
            for (auto k:{2,3,4,6,7,8,9})  if (k<=x) {
                mul(fig[k], k); 
            }

            for (int i = 0; i < 10; ++i) cout << fig[i] << '\t'; cout << endl;
            for (auto k:{2,3,4,6,7,8,9}) {
                int tt=1;
                for (int i = 0; i < 10; ++i) mul(tt,t[i]);

                if (k<=x) {

                }
                
            }
            for (int i = 0; i < 10; ++i) cout << fig[i] << '\t'; cout << endl;
            xx = x;
        }


        cout << ans%10 << endl;

    }
}



