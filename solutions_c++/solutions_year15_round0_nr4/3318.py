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

bool solve(int n,int r,int c) {
    if(n==1)return true;
    if(n==2) {
        if( (r*c)%2 == 0)return true;
        else return false;
    }
    if(n==3) {
        if(r==1 || c==1)return false;
        if( (r%3 ==0) || (c%3 ==0) )return true;
    }
    if(n==4) {
        if(r==3 && c==4) return true;
        if(r==4 && c==3) return true;
        if(r==4 && c==4) return true;
        return false;
    }
    return false;
}

int main() { //takeinput(); takeoutput();
    int TC;
    cin>>TC;

    int kase = 1;
    while(TC--) {
        cout<<"Case #"<<kase++<<": ";
        int n,r,c;
        cin>>n>>r>>c;
        bool ans;
        ans = solve(n,r,c);
        if(ans)cout<<"GABRIEL\n";
        else cout<<"RICHARD\n";
    }
    return 0;
}
