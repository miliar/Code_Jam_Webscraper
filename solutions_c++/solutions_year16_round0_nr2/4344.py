#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <stack>
#include <cmath>
#include <map>
#include <algorithm>
#include <string>

using namespace std;
typedef long long ll;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    scanf("%d",&t);
    int cass=1;
    while(t--)
    {
        string duru;
        cin>>duru;
        int len=duru.length();
        int cnt=0;
        char last=duru[0];
        for(int i=1;i<len;i++)
        {
            if(duru[i]==last) continue;
            else
            {
                cnt++;last=duru[i];
            }
        }
        if(last=='-')cnt++;
        printf("Case #%d: %d\n",cass++,cnt);
    }
    return 0;
}
