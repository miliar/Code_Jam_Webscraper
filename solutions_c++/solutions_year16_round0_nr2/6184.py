#include<bits/stdc++.h>
using namespace std;

int main()
{
    freopen("input.in","r",stdin);
    freopen("output.txt","w",stdout);

    int n;
    cin>>n;
    int t;
    getchar();
    for(t=1;t<=n;t++)
    {
        char s[1000];
        gets(s);
        //cout<<s<<endl;
        int res=1;
        int len=strlen(s);
        int i;
        char ch=s[0];
        for(i=1;i<len;i++)
        {
            if(s[i]!=ch)
            {
                ch=s[i];
                res++;
            }
        }
        if(ch=='+')
            res--;
        cout<<"Case #"<<t<<": "<<res<<endl;
    }
    return 0;
}
