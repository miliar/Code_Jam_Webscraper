#include<iostream>
#include<fstream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<vector>
#include<set>
#include<map>
#include<queue>
#include<utility>
#include<string>

using namespace std;

int solve() {
    int D;
    vector<int> v(1001);

    cin >> D;

    for(int i=0; i<D; i++) {
        int x;
        cin >> x;

        v[x] += 1;
    }

//    for(int i=0; i<10; i++) {
//        cout << v[i] << " ";
//    }
//    cout << endl;

    int ans = 1001;

    for(int i=1; i<=1000; i++) {

        int specials = 0;

        for(int j=i+1; j<=1000; j++) {
            if(v[j] > 0) {
                specials += v[j] * ((j+i-1)/i - 1);
            }
        }

//        if(specials > ans) break;
//        cout << specials << " " << i << endl;
        if(specials + i < ans) ans = specials + i;
    }
    return ans;

}

int main() {
    freopen("Bin.txt", "r", stdin);
    freopen("Bout.txt", "w", stdout);

    int T;
    scanf("%d", &T);

    for(int i=1; i<=T; i++) {
        printf("Case #%d: %d\n", i, solve());
    }

    return 0;
}
