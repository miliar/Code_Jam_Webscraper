#include <iostream>
#include <cstdio>
#include<stack>
#include <cstdlib>
#include <cstring>
#include <set>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <map>
#include <algorithm>
#include <iomanip>
#include <queue>
#include <cctype>
#include <cmath>
#include <ctime>
#include<cassert>

using namespace std;

typedef long long ll;
typedef vector<int> vi;

int main() {
    int t,n,m,ele;
    freopen("/Users/shalini/Downloads/A.txt", "r", stdin);
    freopen("/Users/shalini/Downloads/A1.txt", "w", stdout);
    cin>>t;
    int x = 0;
    for(int counter = 1;counter <= t;++counter) {
        //cout<<counter<<"\n";
        x++;
        cin>>n;
        assert(n > 0);
        //mistake
        int row[17];
        memset(row, 0, sizeof(row));
        for(int i = 0;i < 4;++i) {
            for(int j = 0;j < 4;++j) {
                cin>>ele;
                if(i == (n-1)) {
                    row[ele] += 1;
                }
            }
        }
        cin>>m;
        assert(m > 0);
        for(int i = 0;i < 4;++i) {
            for(int j = 0;j < 4;++j) {
                cin>>ele;
                if(i == (m-1)) {
                    row[ele] += 1;
                }
            }
        }
        int cnt = 0, ans = 0;
        for(int i = 1;i <= 16;++i) {
            if(row[i] == 2) {
                ans = i;
                ++cnt;
            }
        }
        if(cnt == 0) {
            cout<<"Case #"<<x<<": "<<"Volunteer cheated!\n";
        }
        else if(cnt == 1) {
                cout<<"Case #"<<x<<": "<<ans<<"\n";
        }
        else {
            cout<<"Case #"<<x<<": "<<"Bad magician!\n";
        }
    }
    return 0;
}