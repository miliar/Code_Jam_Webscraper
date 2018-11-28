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

#define all(v) v.begin(), v.end()
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
read(n);
while(n--){
int x,r,c;
read3(x,r,c);

if(x == 1){
printf("Case #%d: GABRIEL\n",i++);
continue;
}
else if(x == 2){
if(r*c % 2 == 0){
printf("Case #%d: GABRIEL\n",i++);
continue;
}
else{
printf("Case #%d: RICHARD\n",i++);
continue;
}
}
else if(x == 3){
//1 2 3 4 8 16    r
//6  9  12    g
int val = r*c;
if(val == 6 || val == 9 || val == 12){
printf("Case #%d: GABRIEL\n",i++);
continue;
}
else{
    printf("Case #%d: RICHARD\n",i++);
continue;
}
}
else{
    if(r*c <=9){
        printf("Case #%d: RICHARD\n",i++);
        continue;
    }
    else{
        printf("Case #%d: GABRIEL\n",i++);
        continue;
    }
}
}
return 0;
}
