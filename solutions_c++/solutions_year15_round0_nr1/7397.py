#include<bits/stdc++.h>

using namespace std;

int main()
{
    int i,j,num,cnt,t,test,ans,val;
    string str;

    freopen("a-large.in","r",stdin);
    freopen("a-large.out","w",stdout);

    cin>>test;

    for(t=1;t<=test;t++)
    {
        cin>>num;
        cin>>str;
        cnt=0;
        ans=0;

        for(i=0;i<=num;i++)
        {
            val = str.at(i)-'0';

            if(cnt<i && val>0)
            {
                ans+=(i-cnt);
                cnt+=(i-cnt);
            }

            cnt+=val;
        }
        cout<<"Case #"<<t<<": ";
        cout<<ans<<endl;
    }


    return 0;
}
