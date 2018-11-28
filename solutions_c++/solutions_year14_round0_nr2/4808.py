#include <iostream>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
using namespace std;

int t;
double c,x,f;
double ans;
double tim[10000];
double tmp;

int main()
{
    freopen("B-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
    cin>>t;
    for(int i=0;i<t;i++)
    {
        for(int j=0;j<10000;j++)
        {
            tim[j]=10000.0;
        }
        cin>>c>>f>>x;
        tim[0]=x/2;
        //cout<<x/c<<endl;
        //int nc=1;
//while()
          //  {
            for(int j=1;j<x/c;j++)
        {
            tmp=0;
            for(int k=1;k<=j;k++)
            {
                tmp=tmp+1/(2+(k-1)*f);
            }
            tim[j]=x/(2+j*f)+c*tmp;
        }
        //}

        sort(tim,tim+10000);
        cout<<"Case #"<<i+1<<": ";
        cout << setiosflags(ios::fixed) << setprecision(7) << tim[0]<<endl;

    }
    return 0;
}
