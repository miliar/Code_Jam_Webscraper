#include<iostream>
#include<cstring>
using namespace std;
bool f[20];
int main()
{
    int t,num=0 ;
    cin>>t ;
    while (t--)
    {
        int a,b,x;
        cin>>a; ++num;
        memset(f,0,sizeof(f));
        for (int i=1; i<=4; ++i)
            for (int j=1; j<=4; ++j){
            cin>>x ;
            if (i==a) f[x] = 1;
        }
        cin>>b;
        int ans=0; bool good= 1 ;
        for (int i=1;i<=4; ++i)
        for (int j=1;j<=4; ++j){
            cin>>x;
            if (i==b) {
                if (f[x] && !ans)  ans =x;
                else if (f[x] && ans) good =0 ;
            }
        }
        cout<<"Case #"<<num<<": ";
        if (good && ans) cout<<ans<<endl;
        else if (!good) cout<<"Bad magician!"<<endl;
        else cout<<"Volunteer cheated!"<<endl;
    }
}
