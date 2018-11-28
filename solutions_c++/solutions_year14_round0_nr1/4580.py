#include <iostream>
#include <cstdio>
#include <algorithm>
#include <set>

using namespace std;
int T,n,m;
int main()
{
 //   freopen("ex.in","r",stdin);
 //   freopen("ex.out","w",stdout);
    cin>>T;
    int X=1;
    while(T--)
    {
        set<int>st;
        cin>>n;
        int num=0,ans;
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)\
            {
                int t;
                cin>>t;
                if(i==n-1)
                {
                    st.insert(t);
                }
            }
        }
        cin>>m;
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)\
            {
                int t;
                cin>>t;
                if(i==m-1)
                {
                    if(st.count(t)>0)
                    num++,ans=t;
                }
            }
        }
        cout<<"Case #"<<X++<<": ";
        if(num==0)
        cout<<"Volunteer cheated!"<<endl;
        else if(num==1)
        cout<<ans<<endl;
        else
        cout<<"Bad magician!"<<endl;
    }
    return 0;
}
