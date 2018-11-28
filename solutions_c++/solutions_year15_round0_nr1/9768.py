#include"iostream"
using namespace std;
int main()
{
    int t;
    cin>>t;
    for(int k=1;k<=t;k++)
    {
        int smax;
        cin>>smax;
        char a[smax+1];
        cin>>a;
        long long int ans=0;
        long long need=0;
        for(int i=0;i<=smax;i++)
        {
            if(i==0)
            {
                ans=ans+(int )a[i]-48;
            }
            else
            {
                if(((int)a[i]-48)!=0)
                {
                    if(ans>=i)
                    {
                        ans=ans+(int )a[i]-48;
                    }
                    else
                    {
                        need=need+i-ans;
                        ans=ans+need+((int)a[i]-48);
                    }
                }
            }
        }
        cout<<"Case #"<<k<<":"<<" "<<need<<endl;
    }
    return 0;
}
