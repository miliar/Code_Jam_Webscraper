#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <algorithm>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <fstream>
#include <bitset>
#include <cstdlib>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cassert>
#include <climits>
using namespace std;

int main()
{
        freopen("b.in","r",stdin);
        freopen("out.txt","w",stdout);
        int tc;
        cin>>tc;
        for(int T=1;T<=tc;T++){
            long long int a,b,k;
            cin>>a>>b>>k;
            int count=0;
            for(int i=0;i<a;i++)
            for(int j=0;j<b;j++)
            {
               // cout<<i<<" "<<j<<" "<<(i&j)<<endl;

                if((i&j)<k)count++;
            }
                cout<<"Case #"<<T<<": "<<count<<endl;
        }

}

