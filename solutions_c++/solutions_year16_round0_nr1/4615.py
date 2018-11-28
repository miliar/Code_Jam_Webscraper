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
    long long N;
    cin>>N;
    if(N==0)
        cout<<"INSOMNIA"<<endl;
    else{
        long long i;
        set<int> lft;
        for(i=0;i<10;i++)
            lft.insert(i);
        i=1;

        while(!lft.empty()){
            long long M=N*i;
            int last;
            i++;
            while(M!=0){
                last=M%10;
                M=M/10;
                if(present(lft,last))
                    lft.erase(last);
            }
        }
        cout<<N*(i-1)<<endl;
    }
}
int main() {
     freopen("input/A-large.in","r",stdin);
     freopen("output/output.out","w",stdout);
     int T;
     cin>>T;
     for(int n=1;n<=T;n++) {
          cerr<<n<<endl;
          cout<<"Case #"<<n<<": ";
          solve();
     }
}
