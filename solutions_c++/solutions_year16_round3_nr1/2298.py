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

#define FOR(i, a, b) for (int i = (a); i < (b); ++i)
#define REP(i, n) FOR(i, 0, n)
#define foreach(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)

void ee(vector<string> & ans, vector<int> & pnum, int N, int x)
{
if (x!=0){
    int x=0; string str=""; char c;
    REP(i,N){
        if(pnum[i]!=0 && x<2)
        {++x; --pnum[i]; c=i+'A'; str+=c;}
    }

    ans.push_back(str);
    
    int y=0;
    REP(i,N) {if(pnum[i]!=0) y++;}
    
    ee(ans, pnum, N, y);
    
    }}




void work(int t)
{
    vector<string> ans; vector<int> pnum;
    int N;
    cin>>N; REP(i, N) {int x; cin>>x; pnum.push_back(x);}
    
    ee(ans, pnum, N, N);
    
    reverse(ans.begin(), ans.end());
    cout<<"Case #"<<t+1<<":";
    REP(i,ans.size()) cout<<" "<<ans[i];
    cout<<endl;
    //cout<<"Case #"<<t+1<<": "<<setprecision(9) << ans <<endl;
    //printf("Case #%d: %d\n",t+1,ans);
}

int main()
{
    freopen("in.in","r",stdin);
    freopen("out.out","w",stdout);
    int T; cin>>T; REP(t,T) work(t);
    return 0;
}