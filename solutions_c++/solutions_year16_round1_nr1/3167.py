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

//VARIABLES

void solve(){
    string s;
    getline(cin,s);
    list<char> lw;
    lw.push_back(s[0]);
    for(int i=1;i<sz(s);i++){
        if(s[i]>=lw.front())
            lw.push_front(s[i]);
        else
            lw.push_back(s[i]);
    }
    tr(lw,i){
        cout<<*i;
    }
    cout<<endl;
}
int main() {
     freopen("input/A-large.in","r",stdin);
     freopen("output/output.out","w",stdout);
     int T;
     cin>>T;
     cin.ignore(numeric_limits<streamsize>::max(), '\n');
     for(int n=1;n<=T;n++) {
          cerr<<n<<endl;
          cout<<"Case #"<<n<<": ";
          solve();
     }
}
