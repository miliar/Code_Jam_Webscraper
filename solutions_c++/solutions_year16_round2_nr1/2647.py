#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <utility>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstdio>
#include <string>
#include <iomanip>

using namespace std;

#define REP(i,n) for((i)=0;(i)<(int)(n);(i)++)
#define foreach(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)
//vector< vector<int> > obj(H, vector<int>(W));
int main()
{   freopen("in.in","r",stdin); freopen("out.out","w",stdout);
    int T,t; cin>>T; REP(t,T)
    { int cur, ii, jj, kk;
        string str; cin>>str;
        int ans[10];
        int nletter[30];
        REP(ii, 30) nletter[ii]=0;
        
        REP(ii, str.length()) ++nletter[str[ii]-'A'];
        
        ans[0] = nletter['Z' - 'A'];
        REP(ii, ans[0]) {--nletter['E'-'A']; --nletter['R'-'A']; --nletter['O'-'A']; }
        ans[2] = nletter['W' - 'A'];
        REP(ii, ans[2]) {--nletter['T'-'A']; --nletter['O'-'A']; }
        
        ans[4] = nletter['U' - 'A'];
        REP(ii, ans[4]) {--nletter['F'-'A']; --nletter['O'-'A']; --nletter['R'-'A'];}
        
        ans[6] = nletter['X' - 'A'];
        REP(ii, ans[6]) {--nletter['S'-'A']; --nletter['I'-'A']; }
        
        
        ans[7] = nletter['S' - 'A'];
        REP(ii, ans[7]) {--nletter['E'-'A']; --nletter['V'-'A']; --nletter['E'-'A'];--nletter['N'-'A'];}
        
        ans[1] = nletter['O' - 'A'];
        REP(ii, ans[1]) {--nletter['E'-'A']; --nletter['N'-'A']; }
        
        ans[3] = nletter['R' - 'A'];
        REP(ii, ans[3]) {--nletter['T'-'A']; --nletter['H'-'A']; --nletter['E'-'A'];--nletter['E'-'A'];}
        
        ans[5] = nletter['F' - 'A'];
        REP(ii, ans[5]) {--nletter['I'-'A']; --nletter['V'-'A']; --nletter['E'-'A'];}
        
        ans[8] = nletter['H' - 'A'];
        REP(ii, ans[8]) {--nletter['E'-'A']; --nletter['I'-'A']; --nletter['G'-'A'];--nletter['T'-'A'];}
        ans[9] = nletter['I' - 'A'];
  
        cout<<"Case #"<<t+1<<": ";
        REP(ii,10){
            REP(jj, ans[ii]) cout<<ii;
        }
        cout<<endl;
        //cout<<"Case #:"<<t<<" "<<setprecision(9) << ans <<endl;
        //printf("Case #%d: %d\n",t+1,ans);
    }
    return 0;
}