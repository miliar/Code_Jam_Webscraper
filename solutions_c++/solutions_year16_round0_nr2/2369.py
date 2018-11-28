#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <string>
using namespace std;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int T;cin>>T;int ca=0;
    while(T--)
    {
        string x;
        cin>>x;
        x.erase(unique(x.begin(),x.end()),x.end());
        if(*(--x.end())=='+') {
            x.erase(--x.end(),x.end());
        }
        printf("Case #%d: %d\n",++ca,x.length());
    }
    return 0;
}