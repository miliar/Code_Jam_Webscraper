/*
 * =====================================================================================
 *
 *       Filename: Debug
 *
 *    Description:
 *
 *        Version:  1.0
 *        Created:  2016-05-28-19.44.22, Saturday
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:
 *
 *   ________                          ___.
 *  /  _____/_____   __ ______________ \_ |__
 * /   \  ___\__  \ |  |  \_  __ \__  \ | __ \
 * \    \_\  \/ __ \|  |  /|  | \// __ \| \_\ \
 *  \______  (____  /____/ |__|  (____  /___  /
 *         \/     \/                  \/    \/
 *
 *   Organization:  Shahjalal University of Science and Technology
 *
 * =====================================================================================
 */

#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <cstdio>
#include <climits>
#include <vector>
#include <cstring>
#include <cstdlib>
#include <numeric>
#include <utility>
#include <sstream>
#include <iomanip>
#include <iostream>
#include <algorithm>

using namespace std;

typedef long long Long;
typedef double DD;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef pair<int, int> PII;
typedef pair<Long, Long> PLL;
typedef vector<PII> VPII;
typedef vector<PLL> VPLL;
typedef vector<string> VS;
typedef vector<DD> VD;
typedef vector<Long> VL;
typedef vector<VL> VVL;

const int INF = 2000000000;
const int MOD = 1000000007;
const Long L_MAX = 9223372036854775807;
const int I_MAX = 2147483647;


#define sf scanf
#define pf printf
#define mem(a,b)          memset(a,b,sizeof(a))
#define pb push_back
#define REP(i,a,b)        for(int i=a; i<=b; ++i)
#define REPI(i,a,b,c)     for(int i=a; i<=b; i+=c)
#define REPR(i,a,b)       for(int i=b; i>=a; --i)
#define REPRD(i,a,b,c)    for(int i=b; i>=a; i-=c)
#define REPB(i,a)         for(int i=a; ;i++)
#define REPRB(i,a)        for(int i=a; ; i--)
#define mp(a,b)   make_pair(a,b)
#define fs        first
#define sc        second
#define SZ(s)     ((int)s.size())
#define PI        3.141592653589793
#define lim       1007
#define tlim      (1<<((int)ceil(log2(lim))+1))
#define unq(vec)  stable_sort(vec.begin(),vec.end());\
				  vec.resize(distance(vec.begin(),unique(vec.begin(),vec.end())));
#define BE(a)     a.begin(),a.end()
#define rev(a)    reverse(BE(a))
#define sorta(a)  stable_sort(BE(a))
#define sortc(a, comp)  sort(BE(a),comp)

//int X[]={1,1,2,2,-1,-1,-2,-2},Y[]={2,-2,1,-1,2,-2,1,-1};//knight move
//int X[]={0,-1,-1,-1,0,1,1,1},Y[]={-1,-1,0,1,1,1,0,-1};//8 move
//int X[]={-1,0,1,0},Y[]={0,1,0,-1};//4 move

int n,r,s,p;
string ss;

void generate_lineup(int ii,char ch) {
    if(ii==n) {
        ss+=ch;
        return;
    }
    if(ch=='P') {
        generate_lineup(ii+1,'P');
        generate_lineup(ii+1,'R');
    } else if(ch=='R') {
        generate_lineup(ii+1,'R');
        generate_lineup(ii+1,'S');
    } else {
        generate_lineup(ii+1,'P');
        generate_lineup(ii+1,'S');
    }
    return;
}

bool ok() {
    int rr=0,_ss=0,pp=0;
    for(int i=0; i<SZ(ss); i++) {
        if(ss[i]=='P')pp++;
        else if(ss[i]=='R')rr++;
        else _ss++;
    }
    if(rr==r && _ss==s && pp==p)return 1;
    return 0;
}

void csort(int ii,int jj) {
    if(ii+1==jj) {
        if(ss[ii]>ss[jj])swap(ss[ii],ss[jj]);
        return;
    }
    int dd=(jj-ii+1)/2;
    csort(ii,ii+dd-1);
    csort(ii+dd,jj);
    string x=ss.substr(ii,dd);
    string y=ss.substr(ii+dd,dd);
    if(x>y) {
        for(int i=0; i<dd; i++) {
            swap(ss[ii+i],ss[ii+dd+i]);
        }
    }
    return;
}

int main(int argc, const char **argv) {
    //ios::sync_with_stdio(false);
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int Test;
    cin>>Test;
    REP(kase,1,Test) {
        cin>>n>>r>>p>>s;
        ss.clear();
        generate_lineup(0,'P');
        csort(0,ss.size()-1);
        string ans="";
        if(ok())ans=ss;
        ss.clear();
        generate_lineup(0,'R');
        csort(0,ss.size()-1);
        if(ok()) {
            if(ans=="")ans=ss;
            else ans=min(ans,ss);
        }
        ss.clear();
        generate_lineup(0,'S');
        csort(0,ss.size()-1);
        if(ok()) {
            if(ans=="")ans=ss;
            else ans=min(ans,ss);
        }
        cout<<"Case #"<<kase<<": ";
        if(ans!="")cout<<ans<<"\n";
        else cout<<"IMPOSSIBLE\n";
    }
    //double st=clock(),en;
    //en=clock();
    //cerr<<(double)(en-st)/CLOCKS_PER_SEC<<endl;
    return 0;
}



