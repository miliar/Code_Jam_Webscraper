#include<bits/stdc++.h>
using namespace std;
char s[1005];
bool a[1005];int o;
int letter(int l)
{
    int i,pos=0;
    o=0;
    for(i=0;i<l;i++)
    {
        if(s[i]==s[pos])
                o++;
        if(s[i]>s[pos])
            {
                pos=i;
                o=1;
            }
    }
    return pos;
}
int main()
{
    int t,pos,i,l,c,p;
    cin>>t;
    for(c=1;c<=t;c++)
    {
        cin>>s;
        memset(a,true,sizeof(a));
        cout<<"Case #"<<c<<": ";
        pos=0;o=0;
        for(i=0;i<strlen(s);i++)
        {
            if(s[i]==s[pos])
                o++;
            if(s[i]>s[pos])
            {
                pos=i;
                o=1;
            }
        }
        if(pos==0&&o==1)
            cout<<s<<endl;
        else
        {
            for(i=0;i<strlen(s);i++)
            {
                if(s[i]==s[pos])
                {
                    cout<<s[pos];
                    a[i]=false;
                }
            }
            while(1)
            {
                if(pos==0)
                    break;
                p=letter(pos);
                if(p==0&&o==1)
                    break;
                for(i=pos-1;i>0;i--)
                {
                    if(s[i]==s[p])
                    {
                        cout<<s[i];
                        a[i]=false;
                    }
                }
                pos=p;
            }
            for(i=0;i<strlen(s);i++)
            {
                if(a[i]==true)
                    cout<<s[i];
            }
            cout<<endl;
        }
    }
    return 0;
}
