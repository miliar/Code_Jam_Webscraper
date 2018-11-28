/*
Try Try & Try until you solve the problem...
Nothing is impossible for the problem solvers... :)
*/
/*

*/
#include <iostream>
#include <string>
#include <cstring>
#include <sstream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <utility>
#include <numeric>

#include <cmath>
#include <cstdio>

#define IP(n) for(i=0;i<n;i++)
#define JP(n) for(j=0;j<n;j++)
#define KP(n) for(k=0;k<n;k++)

#define vi vector<int>
#define vi2 vector<vector<int>>
#define vs vector<string>

#define pb push_back
#define TC int t,check=1;cin>>t;while(check<=t)
#define FORIT(i,m) for(__typeof((m).begin()) i=(m).begin();i!=(m).end();i++)
#define ms(x,a) memset(x,a,sizeof(x))
#define read(a) freopen(a,"r",stdin)
#define write(a) freopen(a,"w",stdout)

using namespace std;

int main()
{
    read("A.in");
    write("A.out");
    int t,r,x,check=1;
    cin>>t;
    while(t--)
    {
        vector<int> v1,v2,ans;
        cin>>r;
        for(int i=1;i<=4;i++)
        {
            for(int j=1;j<=4;j++)
            {
                cin>>x;
                if(i==r)
                v1.pb(x);
            }
        }

        cin>>r;
        for(int i=1;i<=4;i++)
        {
            for(int j=1;j<=4;j++)
            {
                cin>>x;
                if(i==r)
                v2.pb(x);
            }
        }

        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                if(v1[i]==v2[j])
                ans.pb(v1[i]);
            }
        }

        printf("Case #%d: ",check++);

        if(ans.size()==0)
        cout<<"Volunteer cheated!"<<endl;
        else if(ans.size()==1)
        cout<<ans[0]<<endl;
        else
        cout<<"Bad magician!"<<endl;
    }
    return 0;
}
