#include<iostream>
using namespace std ;
int main()
{
    int t,x ;
    cin>>t;
    x=t;
    while(t--)
    {
        string s;
        cin>>s;
        int l,i,ans=0;
        l = s.length();
        //cout<<l<<endl;
        char a[l];
        for(i=0;i<l;i++)
        {
            if(s[i]=='+')
                a[i]=1;
            else
                a[i]=0;
        }
        int flag=1;
        for(i=l-1;i>=0;i--)
        {
            if(a[i]!=flag)
            {
                ans+=1;
            }
            flag=a[i];
        }
        cout<<"Case #"<<x-t<<": "<<ans<<endl;

    }
}
