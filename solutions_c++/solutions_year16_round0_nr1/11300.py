#include <bits/stdc++.h>
using namespace std;
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int test,t=1;
    cin>>test;
    map<int,int>mp;
    while(test--)
    {
        int n;
        cin>>n;
        cout<<"Case #"<<t++<<": ";
        if(n==0)
        {
            cout<<"INSOMNIA"<<endl;
        }
        else
        {
            mp.clear();
            int cnt=0;
            for(int i=1;i<=1234567890;i++)
            {
                int temp=i*n;
                while(temp>0)
                {
                    if(mp[temp%10]==0)
                    {
                        cnt++;
                        mp[temp%10]++;
                    }
                    temp/=10;
                }
                if(cnt==10)
                {
                    cout<<i*n<<endl;
                    break;
                }
            }
        }
    }

}

