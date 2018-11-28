#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t;
    cin>>t;
    for(int i=1;i<=t;i++)
    {
        long long int n,ans,val=0,count=0;
        bool a[11];
        memset(a,false,sizeof(a));
        cin>>n;
        if(!n)
        {
            cout<<"Case #"<<i<<": INSOMNIA\n";
            continue;
        }
        while(1)
        {
            val=val+n;
            int temp=val;
            while(temp)
            {
                int mod=temp%10;
                if(!a[mod])
                {
                    count++;
                    a[mod]=true;
                }
                temp/=10;
            }
            if(count==10)
                break;
        }
        cout<<"Case #"<<i<<": "<<val<<endl;
    }
    return 0;
}
