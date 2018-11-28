#include<iostream>
#include<string>
#include<vector>
#include<fstream>
#define mp make_pair

using namespace std;

pair<int,string> mul(string s1,string s2)
{
    if(s1=="1"&&s2=="1")
    {
        return mp(0,"1");
    }
    if(s1=="1"&&s2=="i")
    {
        return mp(0,"i");
    }
    if(s1=="1"&&s2=="j")
    {
        return mp(0,"j");
    }
    if(s1=="1"&&s2=="k")
    {
        return mp(0,"k");
    }
//________________________

    if(s1=="i"&&s2=="1")
    {
        return mp(0,"i");
    }
    if(s1=="i"&&s2=="i")
    {
        return mp(1,"1");
    }
    if(s1=="i"&&s2=="j")
    {
        return mp(0,"k");
    }
    if(s1=="i"&&s2=="k")
    {
        return mp(1,"j");
    }
//________________________

    if(s1=="j"&&s2=="1")
    {
        return mp(0,"j");
    }
    if(s1=="j"&&s2=="i")
    {
        return mp(1,"k");
    }
    if(s1=="j"&&s2=="j")
    {
        return mp(1,"1");
    }
    if(s1=="j"&&s2=="k")
    {
        return mp(0,"i");
    }
//_________________________

    if(s1=="k"&&s2=="1")
    {
        return mp(0,"k");
    }
    if(s1=="k"&&s2=="i")
    {
        return mp(0,"j");
    }
    if(s1=="k"&&s2=="j")
    {
        return mp(1,"i");
    }
    if(s1=="k"&&s2=="k")
    {
        return mp(1,"1");
    }
}

int main()
{
    int i,j,k,l,m,n,t,L,X,Case,mn,mx;
    freopen("Input_4.in","r",stdin);
    freopen("Output.txt","w",stdout);
    string S,s,ex,ans;
    pair<int,string> sum,lc;
    cin>>t;
    Case=0;
    while(t--)
    {
        Case++;
        cin>>L>>X;
        cin>>s;
        S="";
        for(i=0;i<X;i++)
        {
            S=S+s;
        }
        mn=S.length();
        mx=-1;
        sum.first=0;
        sum.second="1";
        for(i=0;i<(int)S.length();i++)
        {
            ex=S[i];
            lc=mul(sum.second,ex);
            sum.first+=lc.first;
            sum.first%=2;
            sum.second=lc.second;
            if(sum.first==0&&sum.second=="i")
            {
                mn=min(mn,i);
            }
        }
        if(sum.first==1&&sum.second=="1")
        {
        sum.first=0;
        sum.second="1";
        for(i=(int)S.length()-1;i>mn&&mx<=mn;i--)
        {
            ex=S[i];
            lc=mul(ex,sum.second);
            sum.first+=lc.first;
            sum.first%=2;
            sum.second=lc.second;
            if(sum.first==0&&sum.second=="k")
            {
                mx=max(mx,i);
            }
        }
        if(mx>mn)
        {
            ans="YES";
        }
        else
        {
            ans="NO";
        }
        }
        else
        {
            ans="NO";
        }
        cout<<"Case #"<<Case<<": "<<ans<<endl;
    }
    return 0;
}
