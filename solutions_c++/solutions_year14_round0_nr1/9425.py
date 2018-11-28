#include<iostream>
#include<sstream>
#include<cstdio>
#include<string>
#include<cstring>
#include<cmath>
#include<climits>
#include<iomanip>
#include<cstdlib>
#include<ctype.h>
#include<algorithm>
#include<numeric>
#include<vector>
#include<list>
#include<set>
#include<bitset>
#include<map>
#include<queue>
#include<deque>
#include<stack>
#define PI acos(-1)
#define EPS 1e-8
#define INF 2147483647
#define INIT(x,y) memset(x,y,sizeof(x))
#define INITip(x,y,n) memset(x,y,n*sizeof(int))
#define INITbp(x,y,n) memset(x,y,n*sizeof(bool))
#define Readfile(x) freopen(x,"r",stdin)
#define Writefile(x) freopen(x,"w",stdout)
typedef long long LL;
typedef long double LD;
using namespace std;
#define N 1000000007

int main() {
    ios_base::sync_with_stdio(false);
    Readfile("A-small-attempt0.in");
    Writefile("A-small-attempt0.out");
    int t;
    cin>>t;
    int nf,ns,af[4][4],as[4][4];
    for(int k=1;k<=t;++k) {
        cin>>nf;
        for(int i=0;i<4;++i)
            for(int j=0;j<4;++j)
                cin>>af[i][j];
        cin>>ns;
        for(int i=0;i<4;++i)
            for(int j=0;j<4;++j)
                cin>>as[i][j];
        set<int> ans;
        for(int i=0;i<4;++i) {
            int d=af[nf-1][i];
            for(int j=0;j<4;++j) {
                if(d==as[ns-1][j])
                    ans.insert(d);
            }
        }
        int x=ans.size();
        cout<<"Case #"<<k<<": ";
        if(x==0)
            cout<<"Volunteer cheated!"<<endl;
        else if(x==1)
            cout<<*ans.begin()<<endl;
        else
            cout<<"Bad magician!"<<endl;
    }
    return 0;
}
