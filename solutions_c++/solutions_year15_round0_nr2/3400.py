#include <iostream>
#include <cmath>
#include <algorithm>
#include <cstdio>
using namespace std;

int main(void)
{


//freopen("input.txt", "r", stdin);
//freopen("output.txt", "w", stdout);


    long long int t;
    cin>>t;

    for(long long int test=1; test<=t; test++)
    {
        long long int D, P[1009],ans, maxx,tmpans,minn,cnt,tmp;
        cin>>D;

        maxx = -1;
        minn = 1009;

        for(int i=0; i<D; i++)
        {
            cin>>P[i];
            maxx = max(maxx, P[i]);
            minn = min(minn,P[i]);
        }

        ans = maxx;

        for(long long int mx = 1; mx <= maxx; mx++)
        {
            cnt = 0;
            for(long long int i=0; i<D; i++)
            {
                tmp = P[i];

                if( tmp <= mx )
                {
                    cnt +=1;
                }

                else
                {
                    //cnt += (tmp/mx) + 1;

                    if( tmp%mx==0 )
                        cnt += tmp/mx;
                    else
                        cnt += tmp/mx + 1;
                }
            }

            tmpans = abs(cnt-D) + mx;
            //cout<<mx<<" "<<tmpans<<endl;

            ans = min(tmpans, ans);
        }

        cout<<"Case #"<<test<<": "<<ans<<endl;
    }
}
