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
typedef long double ld;
typedef unsigned long long ull;

ifstream fin("a.in");
ofstream fout("out.txt");

vector<ld>a , b , c , d;

int main()
{
   int t;
        fin>>t;
        for(int tt=1;tt<=t;tt++)
        {
                int n;
                fin>>n;
                for(int i=1;i<=n;i++)
                {
                        ld x;
                        fin>>x;
                        a.push_back(x);
                        c.push_back(x);
               }
               for(int i=1;i<=n;i++)
                 {
                        ld x;
                        fin>>x;
                        b.push_back(x);
                        d.push_back(x);
               }
               sort(a.begin()  , a.end());
               sort(b.begin()  , b.end());
               sort(c.begin()  , c.end());
               sort(d.begin()  , d.end());
               int ans=0;
                    for(int i=1;i<=n;i++)
                     {
                                int z=a.size()-1;
                                a.pop_back();
                                if(a[z]>b[z])
                                {
                                        ans++;
                                        b.erase(b.begin());
                                }
                                else
                                 b.pop_back();
                     }
                     int ans1=0;
                for(int i=1;i<=n;i++)
                {
                        if(c[0]>d[0])
                       {
                                ans1++;
                                c.erase(c.begin());
                                d.erase(d.begin());
                       }
                       else
                       {
                                c.erase(c.begin());
                                d.pop_back();
                       }
                }
                  fout<<"Case #"<<tt<<": "<<ans1<<" "<<ans<<endl;
        }
}
