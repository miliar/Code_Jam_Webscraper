#include<iostream>
using namespace std;
int main()
{
    ios::sync_with_stdio(false);
    int test,a,i;
    cin>>test;
    for(a=1;a<=test;a++)
    {
        int smax,cnt=0,ans=0;
        cin>>smax;
        char s[smax+1];
        cin>>s;
        for(i=0;s[i];i++)
        {
            if((s[i]!='0')&&(cnt<i))
            {
                ans=ans+(i-cnt);
                cnt+=(i-cnt)+s[i]-'0';
            }
            else
                cnt=cnt+s[i]-'0';
        }
        cout<<"Case #"<<a<<": "<<ans<<endl;
    }
}
