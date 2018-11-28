// Coder nyble
#include <algorithm>
#include <bitset>
#include <deque>
#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pi;
typedef vector<string> vs;

#define fi          first
#define se          second
#define all(x)      (x).begin(), (x).end()
#define ini(a, v)   memset(a, v, sizeof(a))
#define re(i,s,n)  	for(int i=s;i<(n);++i)
#define fr(i,n)     re(i,0,n)
#define tr(i,x)     for(__typeof(x.begin()) i=x.begin();i!=x.end();++i)
#define pu          push_back
#define mp          make_pair
#define sz(x)       (int)(x.size())
#define nl          printf("\n")

int main()
{
    int t;
    cin>>t;
    for(int z=1; z<=t; z++)
    {
        int n;
        double temp;
        cin>>n;
        set<double> naomi,ken,kend;

        fr(i,n)
        {
            cin>>temp;
            naomi.insert(temp);
        }
        fr(i,n)
        {
            cin>>temp;
            ken.insert(temp);
        }

        //nl;
        //tr(it,naomi)cout<<*it<<" ";nl;
        //tr(it,ken)cout<<*it<<" ";nl;

        kend.insert(ken.begin(),ken.end());

        //WAR

        set<double>::iterator it1=naomi.begin(),it2=ken.begin();
        int war_ken=0, war_naomi=0;
        bool found;

        for(; it1!=naomi.end(); it1++)
        {
            found=false;
            for(it2=ken.begin(); it2!=ken.end(); it2++)
            {
                if(*it1<*it2)
                {
                    war_ken++;
                    found=true;
                    ken.erase(it2);
                    break;
                }
            }
            if(!found)war_naomi++;
        }

        //DECEITFUL WAR

        int dwar_ken=0,dwar_naomi=0;

        for(it1=naomi.begin(); it1!=naomi.end(); it1++)
        {
            found=false;
            it2=kend.begin();
            if(*it1<*it2)
            {
                dwar_ken++;
            }
            else
            {
                dwar_naomi++;
                kend.erase(kend.begin());
            }
        }

        printf("Case #%d: %d %d\n",z,dwar_naomi,war_naomi);

    }
    return 0;
}
