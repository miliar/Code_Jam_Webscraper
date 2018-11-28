#include<bits/stdc++.h>
using namespace std;
bool vis[10];
void visD(long long n)
{
    //cout<<n<<endl;
    while(n!=0)
    {
        vis[n%10]=1;
        n/=10;
    }
}
int main()
{
    freopen("E:/A-large.in","r",stdin);
    freopen("E:/output.txt","w",stdout);
    int t;
    cin>>t;
    int k=0;
    while(t--)
    {
        for(int i=0;i<10;i++)
        {
            vis[i]=0;
        }
        k++;
        int n;
        cin>>n;
        if(n==0)
        {
            cout<<"Case #"<<k<<": INSOMNIA\n";
            continue;
        }
        for(int i=1;i<100000;i++)
        {
            visD((long long)i*n);

            int co=0;
            for(int j=0;j<10;j++)
            {
                if(vis[j])
                    co++;
            }
            if(co==10){
                cout<<"Case #"<<k<<": "<<(long long)i*n<<"\n";
                break;
            }
        }
    }
}
