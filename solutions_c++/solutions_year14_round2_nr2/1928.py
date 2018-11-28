#include<functional>
#include<algorithm>
#include<iostream>
#include<fstream>
#include<sstream>
#include<iomanip>
#include<numeric>
#include<cstring>
#include<climits>
#include<cassert>
#include<cstdio>
#include<string>
#include<vector>
#include<bitset>
#include<queue>
#include<stack>
#include<cmath>
#include<ctime>
#include<list>
#include<set>
#include<map>
using namespace std;

int main(int argc,char *argv[])
{
    //freopen("B-small-attempt1.in","r",stdin);
    //freopen("B.out","w",stdout);
    int t,a,b,k, cas=0;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d %d %d",&a,&b,&k);
        long long sum=0;
        for(int i=0; i<a; i++)
        {
            for(int j=0; j<b; j++)
            {
                if((i&j)<k)
                {
                    sum++;
                }
            }
        }
        printf("Case #%d: ",++cas);
        cout<<sum<<endl;
    }
    return 0;
}
