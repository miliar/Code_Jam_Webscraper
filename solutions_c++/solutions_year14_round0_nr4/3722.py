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
using namespace std;

typedef long double ld;

ifstream fin("D-large.in");
ofstream fout("ans.out");
vector<ld>a , b , c , d;

int main()
{
   ios_base::sync_with_stdio(false);          
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
