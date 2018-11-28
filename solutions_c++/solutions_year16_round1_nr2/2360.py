#include<iostream>

using namespace std;

int main()
{
    int t,t1;
    cin>>t;
    t1=t;
    while(t--)
    {
        int n,x,ns;
        int a[2502]={0};
        cin>>n;
        ns=2*(n*n)-n;
        for(int i=0;i<ns;i++)
        {
            cin>>x;
            a[x]++;
        }
        cout<<"Case #"<<t1-t<<": ";
        for(int i=1;i<2501;i++)
        {
            if(a[i]%2)
            {
                cout<<i<<" ";
            }
        }
        cout<<endl;
    }

    return 0;
}

