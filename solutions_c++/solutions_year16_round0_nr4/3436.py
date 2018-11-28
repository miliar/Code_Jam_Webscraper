#include <iostream>
using namespace std;

int main()
{
    int t;
    cin>>t;
    for(int i=1;i<=t;i++)
    {
        int k,c,s;
        cin>>k>>c>>s;
        cout<<"Case #"<<i<<": ";
        if((c==1)&&(k!=s))
        {
                cout<<"IMPOSSIBLE"<<endl;
                continue;
        }
        if((c==1)&&(k==s))
        {
            for(int l=1;l<=k;l++)cout<<l<<" ";
            cout<<endl;
            continue;
        }


        if(c>1)
        {

            if(k%2!=0)
            {
                int m=k/2+1;
                if(s<m)
                {
                    cout<<"IMPOSSIBLE"<<endl;
                    continue;
                }
                cout<<(k/2+1)<<" ";
            }
            else
            {
                int m=k/2;
                if(s<m)
                {
                    cout<<"IMPOSSIBLE"<<endl;
                    continue;
                }
            }
            if(k>1)
            cout<<k<<" ";
            for(int j=2;j<=k/2;j++)
            {
                cout<<j*k-(j-1)<<" ";
            }
        }
        cout<<endl;


    }
    return 0;
}
