/// GCJ Qualification Round 2015
/// Problem A. Standing Ovation
/// -- SeiF
#include <bits/stdc++.h>
using namespace std;

int main()
{
    freopen("A-large.in","r", stdin);
    freopen("A_large_output.txt","w", stdout);

    int i,j,n,T,t=1;
    int smax, cur, ans = 0;
    string aud;
    cin>>T;
    while (T--)
    {
        cin>>smax>>aud;
        cur = int(aud[0]-'0');
        ans = 0;
        aud = "";
        for(i=1;i<=smax;i++)
        {
            if(cur>=i)
            {
                cur+=int(aud[i]-'0');
            }
            else if(aud[i]!='0')
            {
                ans+=i-cur;
                cur+=(i-cur)+int(aud[i]-'0');
            }
            //cerr<<"Cur: "<<cur<<" Shy: "<<i<<endl;
        }
        printf("Case #%d: %d\n",t,ans);
        t++;
    }
}
