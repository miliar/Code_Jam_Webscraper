#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <cstring>
#include <map>
#include <set>
#include <cstdlib>
#include <cmath>
using namespace std;

int main()
{
    int T;
    cin>>T;

    for(int tc = 1; T--; tc++)
    {
        long long r, t, ans = 0, low = 0, up = 2000000000, mid;
        cin>>r>>t;
        //cout<<"DEBUG "<<r<<' '<<t<<endl;
        while(low <= up)
        {
            mid = (low+up)>>1;
            long long res = -mid+2*mid*mid+2*r*mid;
            //if(mid == 1) cout<<"WHY "<<res<<endl;
            if(res <= t) low = mid+1, ans = mid;
            else up = mid-1;
        }
        
        printf("Case #%d: ", tc);
        cout<<ans<<endl;
    }

    return 0;
}
