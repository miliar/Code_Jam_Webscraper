/* In the Name of God */
#include <iostream>
#include <set>
#include <iomanip>
#include <cstring>
#include <algorithm>
#include <string>
#include <fstream>
#include <cmath>
#include <deque>
#include <queue>
#include <vector>
#include <map>
#include <set>
#include<cstdio>
#define lch(r) (2*(r)+1)
#define rch(r) (2*(r)+2) 
#define inf (1<<30)
#define F first
#define S second
#define mod 1000000007
using namespace std;
typedef long long ll;
typedef pair<int ,int > pii;
typedef long double ld;
const int MAXN = 100000+10;
ifstream fin("B-large.in");
ofstream fout("ans.out");
int main()
{
   ios_base::sync_with_stdio(false);          
        int t;
        fin>>t;
        for(int tt=1;tt<=t;tt++)
        {
                ld ans = mod  , c, f , x;
                fin>>c>>f>>x;
                 ld time=0 , ted=2  ;
             
                for(int i=1;i<=100000;i++)
                {
                      
                         ans=min(time  + x/ted, ans);
                     time+=c/ted;
                        ted+=f;
                }
                fout<<"Case #"<<tt<<": ";
                fout<<fixed<<setprecision(7)<<ans<<endl;
        }
                
}
