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
    string S;
    getline(cin,S);
    list<char> ch(all(S));
    string ans;
    while((cpresent(ch,'Z')&&cpresent(ch,'E')&&cpresent(ch,'R')&&cpresent(ch,'O'))){
        ch.erase(find(all(ch),'Z'));
        ch.erase(find(all(ch),'E'));
        ch.erase(find(all(ch),'R'));
        ch.erase(find(all(ch),'O'));
        ans.pb('0');
    }
    while((cpresent(ch,'T')&&cpresent(ch,'W')&&cpresent(ch,'O'))){
        ch.erase(find(all(ch),'T'));
        ch.erase(find(all(ch),'W'));
        ch.erase(find(all(ch),'O'));
        ans.pb('2');
    }
    while((cpresent(ch,'F')&&cpresent(ch,'O')&&cpresent(ch,'U')&&cpresent(ch,'R'))){
        ch.erase(find(all(ch),'F'));
        ch.erase(find(all(ch),'O'));
        ch.erase(find(all(ch),'U'));
        ch.erase(find(all(ch),'R'));
        ans.pb('4');
    }
    while((cpresent(ch,'S')&&cpresent(ch,'I')&&cpresent(ch,'X'))){
        ch.erase(find(all(ch),'S'));
        ch.erase(find(all(ch),'I'));
        ch.erase(find(all(ch),'X'));
        ans.pb('6');
    }
    while((cpresent(ch,'E')&&cpresent(ch,'I')&&cpresent(ch,'G')&&cpresent(ch,'H')&&cpresent(ch,'T'))){
        ch.erase(find(all(ch),'E'));
        ch.erase(find(all(ch),'I'));
        ch.erase(find(all(ch),'G'));
        ch.erase(find(all(ch),'H'));
        ch.erase(find(all(ch),'T'));
        ans.pb('8');
    }

    while((cpresent(ch,'O')&&cpresent(ch,'N')&&cpresent(ch,'E'))){
        ch.erase(find(all(ch),'O'));
        ch.erase(find(all(ch),'N'));
        ch.erase(find(all(ch),'E'));
        ans.pb('1');
    }
    while((cpresent(ch,'T')&&cpresent(ch,'H')&&cpresent(ch,'R')&&count(all(ch),'E')>=2)){
        ch.erase(find(all(ch),'T'));
        ch.erase(find(all(ch),'H'));
        ch.erase(find(all(ch),'R'));
        ch.erase(find(all(ch),'E'));
        ch.erase(find(all(ch),'E'));
        ans.pb('3');
    }
    while((cpresent(ch,'F')&&cpresent(ch,'I')&&cpresent(ch,'V')&&cpresent(ch,'E'))){
        ch.erase(find(all(ch),'F'));
        ch.erase(find(all(ch),'I'));
        ch.erase(find(all(ch),'V'));
        ch.erase(find(all(ch),'E'));
        ans.pb('5');
    }
    while((cpresent(ch,'S')&&cpresent(ch,'V')&&cpresent(ch,'N')&&count(all(ch),'E')>=2)){
        ch.erase(find(all(ch),'S'));
        ch.erase(find(all(ch),'E'));
        ch.erase(find(all(ch),'V'));
        ch.erase(find(all(ch),'E'));
        ch.erase(find(all(ch),'N'));
        ans.pb('7');
    }
    while((cpresent(ch,'I')&&cpresent(ch,'E')&&count(all(ch),'N')>=2)){
        ch.erase(find(all(ch),'N'));
        ch.erase(find(all(ch),'I'));
        ch.erase(find(all(ch),'N'));
        ch.erase(find(all(ch),'E'));
        ans.pb('9');
    }
    if(sz(ch)!=0){
        cerr<<"Error"<<endl;
    }
    sort(all(ans));
    cout<<ans<<endl;
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
