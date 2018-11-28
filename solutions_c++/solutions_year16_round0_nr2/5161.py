#include<bits/stdc++.h>
using namespace std;
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(false);
    int t;
    cin>>t;
    int k=1;
    while(t--)
    {
        string s;
        cin>>s;
        int l=s.length();
        int f=0;
        int c=0;
        if(s[0]=='-')
            c=c+1;
        else
            f=1;
        for(int i=1;i<l;i++)
        {
            if(s[i]=='-'&&f==1)
            {
                c=c+2;
                f=0;
            }
            else if(s[i]=='+')
            f=1;
        }
        cout<<"Case #"<<k<<":"<<" "<<c<<"\n";
        k++;
    }
    return 0;
}
