#include <iostream>
#include <stdio.h>
using namespace std;
string str;

string cal(char c, int n)
{
    if(n==1)
    {
        string ret = "";
        ret+=c;
        return ret;
    }
    string tmp;
    if(c=='R')
    {
        tmp = "RS";
    }
    else if(c=='P')
    {
        tmp = "PR";
    }
    else if(c=='S')
    {
        tmp = "PS";
    }
    int l = n/2+(n%2);
    int r = n-l;
    string ls=cal(tmp[0],l);
    string rs=cal(tmp[1],r);
//    cout<<ls<<' '<<rs<<endl;
    if(ls>rs)
    {
        swap(ls,rs);
    }
    return ls+rs;
}
int r,p,s,n;
bool judge(string str,int tr,int tp,int ts)
{

    for(int i=0;i<str.size();i++)
    {
        if(str[i]=='R')tr--;
        if(str[i]=='P')tp--;
        if(str[i]=='S')ts--;
    }
//    cout<<ts<<' '<<tp<<' '<<tr<<endl;
    return ts==0&&tp==0&&tr==0;
}
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);

    int t;
    cin>>t;
    for(int ti=1;ti<=t;ti++)
    {
        cout<<"Case #"<<ti<<": ";

        int r,p,s,n;
        cin>>n>>r>>p>>s;

        str = "IMPOSSIBLE";

        string ans = cal('P',(1<<n));
//        cout<<"ANS "<<ans<<endl;
        if(judge(ans,r,p,s))
        {
            str = ans;
        }
        ans = cal('R',(1<<n));
//        cout<<"ANS "<<ans<<endl;
        if(judge(ans,r,p,s))
        {
            if(str=="IMPOSSIBLE"||ans<str)
            str= ans;
        }
        ans = cal('S',(1<<n));
//        cout<<"ANS "<<ans<<endl;
        if(judge(ans,r,p,s))
        {
            if(str=="IMPOSSIBLE"||ans<str)
            str=ans;
        }

        cout<<str<<endl;
    }
    return 0;
}
