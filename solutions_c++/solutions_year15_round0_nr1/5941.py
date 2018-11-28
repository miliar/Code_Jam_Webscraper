#include <iostream>
#include <cstdio>
#include <cstdlib>
using namespace std;
int t;
int main()
{
    //freopen("in.txt","r",stdin);
    //freopen("out.txt","w",stdout);
    scanf("%d",&t);
    int tc=0;
    while(t--)
    {
        int n;
        cin>>n;
        string s;
        cin>>s;
        int arr[n+1];
        for(int i=0;i<=n;i++)
            arr[i]=s[i]-'0';
        int cnt=arr[0],ans=0;
        for(int i=1;i<n+1;i++)
        {
            if(cnt<i)
            {
                ans+=(i-cnt);
                cnt=i;
            }
            cnt+=arr[i];
        }
        cout<<"Case #"<<++tc<<": "<<ans<<endl;
    }
}
