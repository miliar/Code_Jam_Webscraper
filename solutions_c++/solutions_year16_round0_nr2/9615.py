#include<bits/stdc++.h>

using namespace std;

int main()
{
    int T;
    cin>>T;
    string s;
    int a[1000];
    int inc=0;
    while(T--)
    {
        inc++;
        for(int i=0;i<1000;i++)
            a[i]=0;
        cin>>s;
        for(int i=0;i<s.length();i++)
        {
            if(s[i]=='+')
                a[i]=1;
            else
                a[i]=0;
        }
        int n=s.length();
        int t=a[0];
        int counter=1;
        for(int i=1;i<n;i++)
        {
            if(t!=a[i])
            {
                counter++;
                t=a[i];
            }
        }
        //cout<<counter<<endl;
        cout<<"Case #"<<inc<<": ";
        if(a[n-1]==0)
            cout<<counter<<endl;
        else
            cout<<counter-1<<endl;
    }
    return 0;
}
