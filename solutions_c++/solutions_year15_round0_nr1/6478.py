/*
   Author : skrcode
*/

#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <fstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <string.h>
#include <cassert>
#include <climits>
#include <ctime>

using namespace std;

const int oo = int(2e9) + 9;
const double eps = 1e-9;
const double pi = 3.14159265358979323846264338327950;

#define debug printf("ERROR DETECTED...!!\n");
#define debug1(p)        cerr << #p << ": " << p << endl;
#define debug2(p, q)     cerr << #p << ": " << p << " | " << #q << ": " << q << endl;
#define debug3(p, q, r)  cerr << #p << ": " << p << " | " << #q << ": " << q << " | " << #r << ": " << r << endl;

#define  takeinput() freopen("ip.txt","r",stdin);
#define  takeoutput() freopen("op.txt","w",stdout);

typedef vector < int > vi;
typedef pair < int, int> ii;
typedef vector < ii > vii;

#define trvi(c, it) for (vi::iterator it = (c).begin(); it != (c).end(); it++)
#define trvii(c, it) for (vii::iterator it = (c).begin(); it != (c).end(); it++)
#define pb push_back
#define mp make_pair
#define F first
#define S second

typedef long long int64;
typedef double float64;

//START

int main() { //takeinput(); takeoutput();
    int TC;
    cin>>TC;

    int kase = 1;
    while(TC--) {
        int n;
        cin>>n;
        string str;
        cin>>str;
        cout<<"Case #"<<kase++<<": ";
        int cur = 0;
        int ans = 0;
        for(int i=0;i<=n;i++) {
            if(str[i]=='0')continue;
            if(cur>=i) {
                cur+=(str[i]-'0');
            }
            else {
                ans+=(i-cur);
                cur+=(i-cur);
                cur+=(str[i]-'0');
            }
        }
        cout<<ans<<endl;
    }
    return 0;
}
