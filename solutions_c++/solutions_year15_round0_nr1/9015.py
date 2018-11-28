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
#include <cstring>
#include <limits>

#define pb push_back
#define VI vector<int>

using namespace std;

int main() {
    int te;
    cin>>te;
    for(int test=1;test<=te;test++)
    {
        int n;
        cin>>n;
        string s;
        cin>>s;
        int cou=0,ans=0;
        for(int i=0;i<s.size();i++)
        {
            if(cou<i)
            {
                   ans+=i - cou ;
                cou+=i- cou ;
            }
            cou+=s[i]-48;
        }
        cout<<"Case #"<<test<<": "<<ans<<endl;
    }
}
