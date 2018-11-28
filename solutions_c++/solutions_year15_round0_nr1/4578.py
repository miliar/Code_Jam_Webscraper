#include <cstring>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>
#include <climits>
#include <cctype>
#include <bitset>
#include <iostream>
#include <string>
#include <array>
#include <regex>


using namespace std;

#define all(v) v.begin(), v.endr()
#define rall(v) v.rbegin(), v.rendr()
#define sz(v) ((int)v.size())
#define read(x) scanf("%d",&(x))
#define read2(x, y) scanf("%d %d",&(x),&(y))
#define read3(x, y, z) scanf("%d %d %d",&(x),&(y),&(z))

typedef stringstream ss;
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<pii> vpii;
typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<double> vd;
typedef vector<vector<int> > vvi;
typedef long double ld;


int main(){
freopen("in.txt", "r",stdin);
freopen ("out.txt","w",stdout);
int i = 1;
int n;
cin >> n;
while(n--){
int num;
string s;
cin >> num >> s;
int counter =0;
int ans = 0;
for(int k=0;k<=num;k++){
    if(s[k]!='0'){
        if(counter - k >= 0){
            counter+= s[k]-'0';
        }
        else{
            ans+=k - counter ;
            counter+= (s[k]-'0') + k - counter;
        }
    }
}

printf("Case #%d: %d\n",i++,ans);


}
return 0;
}






