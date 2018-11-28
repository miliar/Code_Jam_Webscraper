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
#include<time.h>
#include<assert.h>
#include<set>
#include <numeric>
#include <functional>
#include<cstring>
#include<cmath>
#include<iterator>
#include <memory.h>
#include<utility>
#include <ctime>
#include<algorithm>
#define read freopen("input.in","r",stdin)
#define write freopen("output.out","w",stdout)

using namespace std;

int main()
{
    read;write;
    int i,j,k,l,m,n;
    int nc,tc=0;
    cin>>nc;

    while(nc--)
    {
        map<int,int> mp;
        int c=0,res;
        cin>>m;

        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                cin>>k;
                if(i==m-1)
                    mp[k]++;
            }
        }
        cin>>m;

        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                cin>>k;
                if(i==m-1)
                    mp[k]++;
            }
        }

        for(i=0;i<=16;i++)
        {
            if(mp[i]==2)
            {
                c++;res=i;
            }
        }

        if(c==0)
            cout<<"Case #"<<++tc<<": Volunteer cheated!"<<endl;
        else if(c>1)
            cout<<"Case #"<<++tc<<": Bad magician!"<<endl;
        else
            cout<<"Case #"<<++tc<<": "<<res<<endl;
    }
    return 0;
}
