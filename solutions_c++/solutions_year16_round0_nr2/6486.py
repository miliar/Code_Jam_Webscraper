#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t,x=0;
    char s[200];
    cin>>t;
    while(t--)
    {
        cin>>s;
        int l=strlen(s);
        int c=1;
        char cc=s[0];
        for(int i=1;i<l;i++)
        {
            if(s[i]!=cc)
            {
                c+=1;
                cc=s[i];
            }
        }
        if(s[l-1]=='+')c-=1;
        cout<<"Case #"<<++x<<": "<<c<<endl;
    }
    return 0;
}
