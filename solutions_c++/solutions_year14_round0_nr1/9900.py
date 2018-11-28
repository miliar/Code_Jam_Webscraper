#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <climits>

using namespace std;

#define REPEAT(i,a,b) for(int i=a;i<b;++i)
#define REP(i,n) REPEAT(i,0,n)
#define RREP(i,n) for(int i=n-1;i>=0;--i)
#define EACH(it,v) for(typeof(v.begin()) it=v.begin();it!=v.end();++it)
#define pb push_back
#define all(x) (x).begin(),(x).end()
#define CLEAR(x,with) memset(x,with,sizeof(x))
#define sz size()
#define mkp make_pair
typedef long long ll;
int main()
{
        int N;
        cin>>N;
        REPEAT(Case,1,N+1){
                cout<<"Case #"<<Case<<": ";
                //Code Starts Here
                int ans1,ans2;
                vector<int> ans;
                int mat1[4][4];
                int mat2[4][4];
                cin>>ans1;ans1--;
                REP(i,4)REP(j,4)cin>>mat1[i][j];
                cin>>ans2;ans2--;
                REP(i,4)REP(j,4)cin>>mat2[i][j];
                REP(i,4)REP(j,4) 
                {
                   if(mat1[ans1][i] == mat2[ans2][j]) ans.pb(mat1[ans1][i]);
                }
                if(ans.sz==0)cout<<"Volunteer cheated!";
                else if(ans.sz>1)cout<<"Bad magician!";
                else if(ans.sz==1)cout<<ans[0];
                //Code ends Here
                cout<<endl;
        }
        return 0;
}
