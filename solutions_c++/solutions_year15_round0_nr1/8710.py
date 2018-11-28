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
    int t,check=1,k,clap,ans,d,add;
    string str;
    cin>>t;
    while(t--)
    {
        cin>>k>>str;
        clap=0,ans=0;
        for(int i=0;i<=k;i++)
        {
            d=str[i]-'0';
            add=0;
            if(i>clap)
            add=(i-clap);
            ans+=add;
            clap+=(d+add);
        }
        printf("Case #%d: %d\n",check++,ans);
    }
    return 0;
}
