# include <iostream>
# include <fstream>
# include <sstream>
# include <algorithm>
# include <numeric>
# include <cstdio>
# include <cmath>
# include <cstdlib>
# include <cstring>
# include <vector>
# include <list>
# include <set>
# include <map>
# include <stack>
# include <queue>
# include <cctype>
# include <climits>
# include <string.h>
using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef vector<vector<int> > vvi;

#define GI ({int t;scanf("%d",&t);t;})
#define REP(i,a,b) for(int i=a;i<b;i++)
#define ALL(v) (v).begin(),(v).end()
#define TR(i,x) for(typeof(x.begin()) i=x.begin();i!=x.end();i++)
#define pb push_back
#define mp make_pair
#define INF (int)1e9
#define EPS (double)(1e-9)
#define PI (double)(3.141592653589793)
bool myfunction (double i,double j) { return (i>j); }

int main()
{
    int T;
    cin>>T;
    REP(in,1,T+1)
    {
        int N;
        cin>>N;
        vector<double> ken,naomi;
        REP(i,0,N)
            {
                double val;
                cin>>val;
                naomi.push_back(val);
            }
        REP(i,0,N)
            {
                double val;
                cin>>val;
                ken.push_back(val);
            }
        int decietful=0,optimal=0;
        sort(naomi.begin(),naomi.end());
        sort(ken.begin(),ken.end());
        vector<double> ken2(ken.begin(),ken.end());

        REP(i,0,N)
        {
            double val=naomi.at(i);
            //cout<<val<<"\n";
            if(val<ken.at(0))
            {
                ken.erase(ken.end()-1);
                continue;
            }
            else
            {
                ken.erase(ken.begin());
                decietful++;
            }
        }
        sort(naomi.begin(),naomi.end(),myfunction);
        REP(i,0,N)
        {
            double val=naomi.at(i);
            if(val>ken2.at(ken2.size()-1))
            {
                ken2.erase(ken2.begin());
                optimal++;
            }
            else
            {
                ken2.erase(ken2.end()-1);
                continue;
            }
        }
        cout<<"Case #"<<in<<": "<<decietful<<" "<<optimal<<"\n";
    }
    return 0;
}
