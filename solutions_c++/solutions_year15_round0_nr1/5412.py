#include<iostream>
using namespace std;

int main()
{
    std::ios::sync_with_stdio(false);
    int s,x,sum=0,ans=0;
    int T;
    char t;
    cin>>T;
    for(int j=0;j<T;j++)
    {
    ans=0;
    sum=0;
    cin>>s;
    for(int i=0;i<=s;i++)
    {
        cin>>t;
        x=int(t)-int('0');
        if(sum<i)
        {
            ans+=i-sum;
            sum=i;
        }
            sum+=x;
    }
    cout<<"Case #"<<j+1<<": "<<ans<<endl;
    }
}
