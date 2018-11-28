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
        double r=2.0,c,f,x,sec=0.0,cookies=0.0;
        cin>>c>>f>>x;
        if(x<=c)
        {
            sec=x/r;
            printf("Case #%d: %.7f\n",z,sec);
        }
        else
        {
            double time1,time2;
            bool farm=true;

            while(farm)
            {
                time1 = (x-c)/r;
                time2 = x/(r+f);
                //cout<<"time1 = "<<time1<<"\t time2 = "<<time2<<endl;
                if(time1<time2)
                {
                    sec+=(x/r);
                    farm=false;
                    break;
                }
                else
                {
                    sec+=c/r;
                    r+=f;
                }
            }

            printf("Case #%d: %.7f\n",z,sec);
        }
    }
    return 0;
}
