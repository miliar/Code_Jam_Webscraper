#include<bits/stdc++.h>
using namespace std;

int main()
{
    freopen("chuitiye.in","r",stdin);
    freopen("Ss.txt","w",stdout);
    int t;
    cin>>t;
    for(int i=0;i<t;i++)
    {
        char x[10000];
        cin>>x;
        int le=strlen(x);
        int ans=0;
        for(int i=le-1;i>=0;i--)
        {
            if(x[i]=='-')
            {
                //flip all kira
                for(int j=0;j<i;j++)
                {
                    if(x[j]=='-')
                        x[j]='+';
                    else
                        x[j]='-';

                }
                ans++;


            }

        }
        cout<<"Case #"<<i+1<<": "<<ans<<endl;

    }
    return 0;
}
