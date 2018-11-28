#include <vector>
#include <list>
#include <map>
#include <math.h>
#include <cmath>
#include <set>
#include <queue>
#include <deque>
#include <string>
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
#include <string.h>
#include <cstdlib>
#include <ctime>
using namespace std;

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    cin>>t;
    for(int F=1;F<=t;F++)
    {
        cout<<"Case #"<<F<<": ";
        double time=0,a=2,x,f,c;
        cin>>c>>f>>x;
        while(true)
        {
            if(c/a+x/(a+f)<x/a)
            {
                time+=c/a;
                a+=f;
            }
            else
            {
                time+=x/a;
                break;
            }
        }
        cout<<fixed<<setprecision(7)<<time<<endl;
    }
}
