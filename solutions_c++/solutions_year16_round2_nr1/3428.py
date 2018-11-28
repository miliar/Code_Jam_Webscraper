#include <iostream>
#include <stdio.h>
#include <string>
#include <string.h>
using namespace std;
string arr[] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
bool vis[2010];
int num[300];
int sta[300];
int sn;
bool canFind(int now)
{
    for(int i=0;i<arr[now].length();i++)
    {
        if(num[arr[now][i]]<=0)return false;

    }
    return true;
}
bool dfs(int now,int length)
{
    if(now==10)return false;
    if(length==0)
    {
        return true;
    }
    if(canFind(now))
    {
        for(int i=0;i<arr[now].length();i++)
        {
            num[arr[now][i]]--;
        }
        if(dfs(now,length-arr[now].length()))
        {
            sta[sn++]=now;
            return true;
        }

        for(int i=0;i<arr[now].length();i++)
        {
            num[arr[now][i]]++;
        }
    }
    return dfs(now+1,length);
}
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    cin>>t;
    for(int ti=1;ti<=t;ti++)
    {
        string input;
        cin>>input;
        memset(vis,false,sizeof(vis));
        memset(num,0,sizeof(num));
        sn=0;
        for(int i=0;i<input.length();i++)
        {
            num[input[i]]++;
        }
        dfs(0,input.length());
        cout<<"Case #"<<ti<<": ";
        for(int i=sn-1;i>=0;i--)
            cout<<sta[i];
        cout<<endl;
    }

    return 0;
}
