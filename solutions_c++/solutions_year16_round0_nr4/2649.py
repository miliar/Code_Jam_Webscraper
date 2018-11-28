#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
#include <climits>
#include <cassert>
using namespace std;

#define REP(i,n) for(int i=0;i<n;i++)
#define INF INT_MAX/3
#define LINF LLONG_MAX/3
#define MP make_pair
#define PB push_back
#define ALL(v) (v).begin(),(v).end()

typedef long long ll;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef vector<vi> vvi;

void solve(){
    int K,C,S;cin>>K>>C>>S;
    for(int i=0;i<K-1;i++) cout << i+1 << " ";
    cout << K << endl;
}

int main(){
    int T;cin>>T;
    for(int i=0;i<T;i++){
        printf("Case #%d: ",i+1);
        solve();
    }
}
