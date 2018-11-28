#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

long long A,B;
char s[100];

bool check(long long t)
{
    int len=0;
    while(t>0)
    {
        s[len++]=t%10;
        t/=10;
    }
    for(int i=0;i<len/2;i++)
    {
        if(s[i]!=s[len-1-i])
        {
            return false;
        }
    }
    return true;
}

int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("cout.txt","w",stdout);
    int T;
    scanf("%d",&T);
    for(int cas=1;cas<=T;cas++)
    {
        int ans=0;
        cin>>A>>B;
        long long i=sqrt(A);
        if(i*i<A)
        {
            i++;
        }
        for(;i*i<=B;i++)
        {
         //   cout<<i*i<<endl;
            if(check(i)&&check(i*i))
            {
                ans++;
        //        cout<<i<<" "<<i*i<<endl;
            }
        }
        printf("Case #%d: %d\n",cas,ans);
    }
	return 0;
}
