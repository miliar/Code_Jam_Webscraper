#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<string>
#include<cstring>
#include<cstdlib>
#include<cmath>

using namespace std;

int main()
{
    freopen("A-small-attempt1.in","r",stdin);
    freopen("A-small-attempt1.out","w",stdout);

    long long int t,n,r,T,cnt,fst,area,cc=1;

    cin>>T;

    while(T--)
    {
        cnt = 0;

        cin>>r>>t;

        fst = r+1;

        while(t>=0)
        {
            area = fst*fst - (fst-1)*(fst-1);
            cnt++;
            t = t - area;

            fst += 2;

        }

        cout<<"Case #"<<cc++<<": "<<(cnt-1)<<endl;
    }

    return 0;
}
