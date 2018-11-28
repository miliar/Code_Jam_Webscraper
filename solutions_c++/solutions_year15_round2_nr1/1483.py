#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <cstdlib>
#include <cmath>
#include <string>
#include <algorithm>
#include <cstdio>
#include <ctime>

using namespace std;


int rev(int x){
    vector <int> a;
    a.clear();
    int k = x;
    while (k){
        a.push_back(k%10);
        k/=10;
    }
    int res = 0;
    int s = 1;
    for (int i=0;i<a.size();i++){
        res += a[a.size()-i-1]*s;
        s*= 10;
    }
    return res;
}

int d[20000001];

int main(int argc, char **argv){
    freopen("/Users/Arseniy/All/Int/input.txt", "r", stdin);
    freopen("/Users/Arseniy/All/Int/int/output.txt", "w", stdout);
    int t;
    cin >> t;
    for (int i=0;i<=1000000;i++)
        d[i] = i;
    for (int i=0;i<=1000000;i++){
        d[i+1] = min(d[i+1], d[i]+1);
        int k = rev(i);
        d[k] = min(d[k], d[i]+1);
    }
    
    for (int o=0;o<t;o++){
        cout << "Case #" << o+1 <<": ";
        int n;
        cin >> n;
        int ans = d[n];
        cout << ans << endl;
    }

    return 0;
}