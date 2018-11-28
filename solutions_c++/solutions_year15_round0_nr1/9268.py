#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstring>
#include <stack>
#include <queue>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <utility>
#include <algorithm>
#include <limits.h>
#include <functional>

typedef long long ll;
#define MOD 1000000007

using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);cin.tie(0);
    freopen("C:\\Users\\Rathi\\Desktop\\A-large.in","r",stdin);
    freopen("C:\\Users\\Rathi\\Desktop\\output.txt","w",stdout);
    int t,i,z;
    int sum=0,p,need,max;
    char x[1008];
    cin>>t;
    z=t;
    while(t--)
    {
        cin>>max>>x;
        ///cout<<x[0]<<endl;
        sum=x[0]-48;
        need=0;
        for(i=1;i<=max;i++)
        {

            if(sum>=i)
                {sum+=(x[i]-48);///cout<<sum<<" "<<i<<endl;
                }
            else
            {
                need+=(i-sum);
                ///cout<<"need when i= "<<i<<"is "<<(i-sum)<<endl;
                sum+=(x[i]-48)+(i-sum);

            }
        }
        cout<<"Case #"<<z-t<<": "<<need<<endl;
    }
    return 0;
}

