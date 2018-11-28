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
int a[4][4],b[4][4];
int t;
int a1,a2;
int cnt;
int ans;

int main()
{
    freopen("A-small-attempt1.in","r",stdin);
    freopen("out1.txt","w",stdout);
    cin>>t;
    for(int i=0;i<t;i++)
    {
        cnt=0;
        ans=0;
        cin>>a1;
        for(int j=0;j<4;j++)
        {
            for(int k=0;k<4;k++)
            {
                cin>>a[j][k];
            }
        }
        cin>>a2;
        for(int j=0;j<4;j++)
        {
            for(int k=0;k<4;k++)
            {
                cin>>b[j][k];
            }
        }
        for(int j=0;j<4;j++)
        {
            for(int k=0;k<4;k++)
            {
                if(a[a1-1][j]==b[a2-1][k])
                {
                    ans=a[a1-1][j];
                    cnt++;
                }
            }
        }
        if(cnt==0)
        {
            cout<<"Case #"<<i+1<<": Volunteer cheated!"<<endl;
        }
        else if(cnt==1)
        {
            cout<<"Case #"<<i+1<<": "<<ans<<endl;
        }
        else
        {
            cout<<"Case #"<<i+1<<": Bad magician!"<<endl;
        }
    }
    return 0;
}
