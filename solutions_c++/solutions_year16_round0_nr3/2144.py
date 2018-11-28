#include<iostream>
#include<vector>
#include<string>
using namespace std;
long long ans[20];
void p(long long x,int n)
{
    for(int i=n-1;i>=0;i--)
    {
        if((x&(1LL<<i))==0)
        {
            cout<<0;
        }else
        {
            cout<<1;
        }
    }

}
int main()
{
    int i,j,k;
    int t,n,m,ca=1;
    cin>>t;
    while(t--)
    {
        cin>>n>>m;
        long long base=1+(1<<((n/2)-1));
        cout<<"Case #"<<ca<<": \n";
        ca++;
        for(i=2;i<=10;i++)
        {
            ans[i]=1;
            for(j=0;j<n/2;j++)
            {
                ans[i]*=i;
            }
            ans[i]+=1;
        }
        for(i=0;i<m;i++)
        {
            long long tmp = base+i*2;
            tmp = (tmp<<(n/2))+tmp;
            p(tmp,n);
            cout<<' ';
            for(j=2;j<=10;j++)
            {
                cout<<ans[j]<<' ';
            }
            cout<<endl;
        }
    }
}
