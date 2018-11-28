#include <iostream>
#include <string>
using namespace std;

long moves(string s,int st,int en)
{
    if(st==en+1) return 0;
    if(s[en]=='+') return moves(s,st,en-1);
    if(s[en]=='-'&&s[st]=='-')
    {
        int i=st,j=en;
        while(i<=j)
        {
            char tmp = s[i];
            s[i]=s[j];
            s[j]=tmp;
            i++;
            j--;
        }
        for(int k=st;k<=en;k++) if(s[k]=='+') s[k]='-'; else s[k]='+';
        return 1+moves(s,st,en-1);
    }
    if(s[en]=='-'&&s[st]=='+')
    {
        for(int i=st;i<=en;i++) if(s[i]=='-') break; else s[i]='-';
        int l=st,m=en;
        while(l<=m)
        {
            char tmp = s[l];
            s[l]=s[m];
            s[m]=tmp;
            l++;
            m--;
        }
        for(int k=st;k<=en;k++) if(s[k]=='+') s[k]='-'; else s[k]='+';
        return 2+moves(s,st,en);
    }
}
main()
{
int t;
cin>>t;
for(int i=1;i<=t;i++)
{
    string s;
    cin>>s;
    long mov = moves(s,0,s.length()-1);
    cout<<"Case #"<<i<<": "<<mov<<endl;
}
return 0;
}
