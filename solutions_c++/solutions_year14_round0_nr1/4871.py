#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
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
#include <fstream>
#include <string.h>
#include <climits>

#define repx(i,x,n) for(int i=x;i<n;i++)
#define rep(i,n) repx(i,0,n)
#define pb push_back
#define full(v)	v.begin(),v.end()
#define VI vector<int>
#define VS vector<string>
#define LL long long
using namespace std;

int main()
{
    int test,cas=0;
    ifstream cin ("gcjin1.in");
    ofstream cout ("gcjout1.txt");
    cin>>test;
    while(test-- && ++cas)
    {
        int r1,r2;
        set <int> s1,s2;
        VI ans;
        cin>>r1;
        r1--;
        int temp;
        rep(i,4)
        rep(j,4)
         {
             cin>>temp;
             if(i==r1)
                s1.insert(temp);
         }
        cin>>r2;
        r2--;
        rep(i,4)
        rep(j,4)
        {
            cin>>temp;
            if(i==r2)
                s2.insert(temp);
        }
        set_intersection(s1.begin(),s1.end(),s2.begin(),s2.end(), std::back_inserter(ans));

        cout<<"Case #"<<cas<<": ";
        if(ans.size()==0)
            cout<<"Volunteer cheated!\n";
        else if(ans.size() > 1)
            cout<<"Bad magician!\n";
        else
            cout<<ans[0]<<"\n";

    }
    return 0;
}
