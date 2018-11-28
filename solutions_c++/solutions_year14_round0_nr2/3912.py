//IN THE NAME OF GOD
//BENYAM1N

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

using namespace std;

const long long MAX_N = 100000+100;

#define lc(x) 2*x
#define rc(x) 2*x+1
#define inf 1<<30

typedef pair<int,int> pii;
typedef long long ll;
typedef unsigned long long ull;

ifstream fin("a.in");
ofstream fout("out.txt");

int main()
{
   int t;
        fin>>t;
        for(int tt=1;tt<=t;tt++)
        {
                long double ans = 1000000007  , c, f , x;
                fin>>c>>f>>x;
                 long double time=0 , ted=2  ;

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
