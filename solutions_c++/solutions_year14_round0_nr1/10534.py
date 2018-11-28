#include<cstdio>
#include <iostream>
using namespace std;

int data[5][5];
int temp[5][5];

int main()
{
    freopen("in.in","r",stdin);
    freopen("out.out","w",stdout);
    int T,n=0;cin>>T;
    while(n++ < T)
    {
        int r1,r2;
        cin>>r1;r1--;
        for(int i=0;i<16;i++)
            cin>>data[i/4][i%4];
        cin>>r2;r2--;
        for(int i=0;i<16;i++)
            cin>>temp[i/4][i%4];
        int ans=0;

        for(int i=0;i<4; i++ )
        for(int j=0;j<4; j++ )
            if(data[r1][i]==temp[r2][j])
            {
                 ans=data[r1][i]*100+ans%100;
                 ans++;
            }
        cout<<"Case #"<<n<<": ";
        if(ans%100>1) cout<<"Bad magician!";
        else if(ans==0)
            cout<<"Volunteer cheated!";
        else cout<<ans/100;
        cout<<endl;
    }

}
