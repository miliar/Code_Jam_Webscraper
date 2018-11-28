#include <algorithm>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <string>
#include <vector>
using namespace std;

int T,N;
char str[1005];

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    cin>>T;
    for(int ca=1;ca<=T;ca++)
    {
        cin>>N;
        cin>>str;
        int ans=0;
        int cwj=0;
        for(int i=0;i<=N;i++) {
            int h=(int)(str[i]-'0');
            if(cwj>=i)
            {
                cwj+=h;
            }
            else
            {
                ans+=(i-cwj);
                cwj=i+h;
            }
        }
        cout<<"Case #"<<ca<<": "<<ans<<endl;
    }
    return 0;
}
