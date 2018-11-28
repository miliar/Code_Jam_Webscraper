#include<iostream>
#include<cstdio>

using namespace std;

int main()
{
    freopen("C:\\Users\\Saurabh Prakash\\Desktop\\in.txt","r",stdin);
    freopen("C:\\Users\\Saurabh Prakash\\Desktop\\out.txt","w",stdout);
    int t,cas=1;
    cin>>t;
    while(t--)
    {
        int smax,i,sum=0,ans=0;
        string s;
        cin>>smax>>s;
        for(i=0;i<s.size();i++)
        {
            if(sum<i)
                ans+=i-sum,sum=i;
            sum+=s[i]-'0';
        }
        cout<<"Case #"<<cas++<<": "<<ans<<endl;
    }

    return 0;
}
