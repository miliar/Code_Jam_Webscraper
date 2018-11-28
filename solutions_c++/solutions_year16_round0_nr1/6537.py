#include<bits/stdc++.h>
#define dt long long int
using namespace std;
map<int,int>mp;
int main()
{
    dt test,tc=1,n,m,i;
    cin>>test;
    while(test--)
    {
        cin>>n;
        if(n==0)
        {
            cout<<"Case #"<<tc++<<": INSOMNIA"<<endl;
            continue;
        }
        m=n;
        while(m!=0)
        {
            mp[m%10]=1;
            m/=10;
        }
        i=2;
        while(mp.size()!=10)
        {
            m=i*n;
            while(m!=0)
            {
                mp[m%10]=1;
                m/=10;
            }
            i++;
        }
        cout<<"Case #"<<tc++<<": "<<(i-1)*n<<endl;
        mp.clear();
    }
    return 0;
}
