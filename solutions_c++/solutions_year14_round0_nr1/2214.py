//ShivamRana...
#include <cassert>
#include <cctype>
#include <cmath>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <list>
#include <deque>
#include <stack>
#include <iterator>
#include <string>
#include <sstream>
#include <iostream>
#include <fstream>
#include <functional>
#include <numeric>
#include <algorithm>
using namespace std;
int main()
{
  //  freopen("1a.in","r",stdin);
    //freopen("1a.out","w",stdout);
    int t;
    cin>>t;
    for(int cs=1;cs<=t;cs++)
    {
        int f[4][4],s[4][4];
        int n,m;
        cin>>n;
        for(int i=0;i<4;i++)
        for(int j=0;j<4;j++)
        scanf("%d",&f[i][j]);
        cin>>m;
        for(int i=0;i<4;i++)
        for(int j=0;j<4;j++)
        scanf("%d",&s[i][j]);
        int common=0,ans;
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            if(f[n-1][i]==s[m-1][j]){common++;ans=f[n-1][i];}
        }
        if(common==1)
        printf("Case #%d: %d\n",cs,ans);
        else if(common==0)
        printf("Case #%d: Volunteer cheated!\n",cs);
        else if(common>1)
        printf("Case #%d: Bad magician!\n",cs);
    }
    return 0;
}





