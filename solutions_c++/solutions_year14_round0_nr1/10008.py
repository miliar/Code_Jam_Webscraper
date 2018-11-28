#include<bits/stdc++.h>
#define pii pair<long int,long int>
#define mp make_pair
using namespace std;
pii A[515],B[515];
struct _ {
    ios_base::Init i;

    _() {
        cin.sync_with_stdio(0);
        cin.tie(0);
    }
} _;
main()
{
     //freopen("C:\\Users\\codersan\\Desktop\\cc\\input.in", "r", stdin);
     //freopen("C:\\Users\\codersan\\Desktop\\cc\\output.txt", "w", stdout);
    int t;
    cin>>t;
   for(int x=1;x<=t;x++)
    {
        int *a=new int [17];
        int n,temp,dummy;
        cin>>n;
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                cin>>temp;
                if(i+1==n){a[temp]=1;}
            }
        }
        cin>>n;
        int cnt=0;
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                cin>>temp;
                if(i+1==n)
                {
                    if(a[temp]==1){cnt++;dummy=temp;}
                }
            }
        }
        cout<<"Case #"<<x<<": ";
        if(cnt==1)
            cout<<dummy;
        else if(cnt==0)
            cout<<"Volunteer cheated!";
        else cout<<"Bad magician!";
        cout<<endl;
    }
}
