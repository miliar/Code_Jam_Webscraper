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

int T,D,P[1005];

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    cin>>T;
    for(int ca=1;ca<=T;ca++)
    {
        cin>>D;
        for(int i=0;i<D;i++) {
            cin>>P[i];
        }
        sort(P,P+D);
        int ans=P[D-1];
        for(int i=1;i<P[D-1];i++)
        {
            int tmp=i;
            for(int j=0;j<D;j++)
            {
                if(P[j]>i)
                {
                    int cwj=P[j]-i;
                    tmp+=(cwj/i);
                    if((cwj%i)!=0) tmp++;
                }
            }
            ans=min(ans,tmp);
        }
        cout<<"Case #"<<ca<<": "<<ans<<endl;
    }
    return 0;
}
