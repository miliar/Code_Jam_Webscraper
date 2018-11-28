#include <iostream>
#include <stdio.h>
#include <vector>
#include <algorithm>
#include <string>
#include <map>
#include <set>

using namespace std;

typedef long long ll;


int main(){
    freopen("/home/xiaodot/Downloads/A-large.in", "r", stdin);
    freopen("../out.txt", "w", stdout);
    int T;
    cin >> T;

    for(int test=0; test<T; test++){
        int n;
        cin >> n;

        if(n == 0){
            cout << "Case #" << test+1 << ": " << "INSOMNIA" << endl;
            continue;
        }
        set<int> s;
        ll res = n;

        ll t = res;

        while(t){
            int digit = t % 10;
            s.insert(digit);
            t /= 10;
        }

        while(s.size() < 10){
            ll t = res;
            while(t){
                int digit = t % 10;
                s.insert(digit);
                t /= 10;
            }
            if(s.size() < 10) res += n;
        }

        cout << "Case #" << test+1 << ": " << res << endl;
    }
    return 0;
}
