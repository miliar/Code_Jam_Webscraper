#include <iostream>
#include <limits>
#include <cstdlib>
#include <cassert>
#include <string>
#include <sstream>
#include <cmath>
#include <climits>
#include <cctype>
#include <iterator>
#include <algorithm>
#include <utility>
#include <tuple>
#include <vector>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <list>

using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> ii;
#define sz(a) int((a).size())
#define pb push_back
#define all(c) (c).begin(),(c).end()
#define tr(c,i) for(auto i = (c).begin(); i != (c).end(); i++)
#define present(c,x) ((c).find(x) != (c).end())
#define cpresent(c,x) (find(all(c),x) != (c).end())


void solve(){
    int K,C,S;
    cin>>K>>C>>S;
    if(C==1){
        for(int i=1;i<=K;i++)
            cout<<" "<<i;
        cout<<endl;
    }
    else if(K==1){
        cout<<" 1"<<endl;
    }
    else{
        for(int i=2;i<=K;i++)
            cout<<" "<<i;
        cout<<endl;
    }
}
int main() {
     freopen("input/D-small-attempt0.in","r",stdin);
     freopen("output/output.out","w",stdout);
     int T;
     cin>>T;
     for(int n=1;n<=T;n++) {
          cerr<<n<<endl;
          cout<<"Case #"<<n<<":";
          solve();
     }
}
