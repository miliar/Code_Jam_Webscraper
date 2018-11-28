#include<cstdio>
#include<iostream>
#include<vector>
#include<map>
#include<stack>
#include<cstdio>
#include<iostream>
#include<vector>
#include<map>
#include<stack>
#include<queue>
#include<bitset>
#include<list>
#include<iomanip>
#include<string>
#include<climits>
#include <sstream>
#include <fstream>
#include<cctype>
#include<ctime>
#include<cassert>
#include <numeric>
#include <functional>
#include<cstring>
#include<cmath>
#include<iterator>
#include <memory.h>
#include<utility>
#include <ctime>
#include<deque>
#define ll long long

using namespace std;
int main()
{
    ll i,j,k,l,m,n,tc=1,nc,count,a[1000];
    freopen("input.in","r",stdin);
    freopen("output.in","w",stdout);
    cin>>nc;
    while(nc--)
    {
        cin>>n>>m;
        count=0;
        for(i=n;i<=m;i++)
        {
            if(i==1||i==4||i==9||i==121||i==484)
                count++;
        }
        cout<<"Case #"<<tc++<<": "<<count<<endl;
    }

    return 0;
}
