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
long long a,b,k;
long long cnt;
long long tmp;
int main()
{
    freopen("B-small-attempt0 .in","r",stdin);
    freopen("out.txt","w",stdout);
    cin>>t;
    for(int i=0;i<t;i++)
    {
        cnt=0;
        cin>>a>>b>>k;
        for(long long j=0;j<a;j++)
        {
            for(long long m=0;m<b;m++)
            {
                tmp=j&m;
                //cout<<j<<" "<<m<<" "<<tmp<<endl;
                if(tmp<k)
                    cnt++;
            }
        }
        cout<<"Case #"<<i+1<<": "<<cnt<<endl;
    }
    return 0;
}
