#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t;
    cin>>t;
    for(int t1=1;t1<=t;t1++){
    char s[104];
    cin>>s;
    int l=strlen(s),c=0;
    reverse(s,s+l);
    for(int i=0;i<l;i++)
    {
        if(s[i]=='-')
        {
            c++;
            for(int j=i+1;j<l;j++)
            {
                if(s[j]!=s[j-1])
                {
                    c++;
                }
            }
            break;
        }
    }
    cout<<"Case #"<<t1<<": "<<c<<endl;
    }
    return 0;
}
