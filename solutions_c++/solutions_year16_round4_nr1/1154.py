#include<bits/stdc++.h>
using namespace std;
int T,n,R[13],P[13],S[13];
bool check()
{
    for(int i=n;i>=1;--i)
    {
        R[i-1]=(R[i]+S[i]-P[i])/2;
        P[i-1]=(P[i]+R[i]-S[i])/2;
        S[i-1]=(S[i]+P[i]-R[i])/2;
        if(R[i-1]<0 || P[i-1]<0 || S[i-1]<0)
            return false;
    }
    return true;
}
string dfs(int d,string now)
{
    if(d == n)return now;
    string l,r;
    if(now[0] == 'R')
    {
        l = dfs(d+1,(string)("R"));
        r = dfs(d+1,(string)("S"));
    }
    else if(now[0] == 'S')
    {
        l = dfs(d+1,(string)("S"));
        r = dfs(d+1,(string)("P"));
    }
    else 
    {
        l = dfs(d+1,(string)("P"));
        r = dfs(d+1,(string)("R"));
    }
    if(l+r < r+l)
        return l+r;
    else return r+l;
}
void work()
{
    string now="",tmp="";
    if(R[0])now="R";
    else if(P[0])now="P";
    else now="S";
    cout<<dfs(0,now)<<endl;
}
int main()
{
    cin>>T;
    for(int data=1;data<=T;data++)
    {
        cin>>n;
        cin>>R[n]>>P[n]>>S[n];
        if(!check())
            cout<<"Case #"<<data<<": IMPOSSIBLE" << endl;
        else 
        {
            cout<<"Case #"<<data<<": ";
            work();
        }
    }
}
