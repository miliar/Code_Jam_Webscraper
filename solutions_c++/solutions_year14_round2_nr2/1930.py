#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <string>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>
#define inf 1000*1000*1000
//#define f first
//#define s second
#define mp make_pair
using namespace std;
int te, a, b, k, ans, ind;
int main()
{
    ifstream cin("B-small.in");
    ofstream cout("B-small.out");
    cin>>te;
    while(te--)
    {
        ind++;
        cin>>a>>b>>k;
        cout<<"Case #"<<ind<<": ";
        ans=0;
        for(int i=0;i<a;i++)
        {
            for(int j=0;j<b;j++)
            {
                int x=i&j;
                if(x<k)
                    ans++;
            }
        }
        cout<<ans<<endl;
    }
}
