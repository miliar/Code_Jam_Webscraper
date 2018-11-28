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

using namespace std;

int main()
{
    freopen("D-small-attempt5.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    cin>>t;
    for(int i=0;i<t;i++)
    {
        int x,r,c;
        cin>>x>>r>>c;
        if((r*c)%x==0 && x<7 && max(r,c)>=x && (x==2 || min(c,r)>x/2)){cout<<"Case #"<<i+1<<": "<<"GABRIEL"<<endl;}
        else{cout<<"Case #"<<i+1<<": "<<"RICHARD"<<endl;}
    }
    return 0;
}
