#include <iostream>
#include <cstring>
#include <cstdio>
#include <queue>
#include <stack>
#include <string>
using namespace std;
int arr[5][5]={0,0,0,0,0,0,1,2,3,4,0,2,-1,4,-3,0,3,-4,-1,2,0,4,3,-2,-1};
char a[10001];
char result[200001];
int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
    int T;
    int l,x;
    bool zf;
    int ans;
    cin>>T;
    for(int i=1;i<=T;i++)
    {
        cin>>l>>x;
        cin>>a;
        if(x%4==0)
        {
            cout<<"Case #"<<i<<": NO"<<endl;
            continue;
        }
        zf=true;
        for(int j=0;j<l;j++)
        {
            if(a[j]=='i')a[j]='2';
            if(a[j]=='j')a[j]='3';
            if(a[j]=='k')a[j]='4';
        }
        ans=a[0]-'0';
        for(int j=1;j<l;j++)
        {
            ans=arr[ans][a[j]-'0'];
            if(ans<0)
            {
                zf=!zf;
                ans=-ans;
            }
        }
        if(!zf)
            ans=-ans;
        if(ans==1||(ans==-1&&x%2==0)||(ans!=-1&&x%2!=0))
        {
            cout<<"Case #"<<i<<": NO"<<endl;
            continue;
        }
        if(x>15)
            x=x-(x-15)/4*4;
        int len=0;
        for(int j=0;j<x;j++)
        {
            for(int k=0;k<l;k++)
            result[len++] = a[k];
        }
        zf=true;
        ans=result[0]-'0';
        int k;
        for(k=1;k<len;k++)
        {
            if(zf&&ans==2)
                break;
            ans=arr[ans][result[k]-'0'];
            if(ans<0)
            {
                zf=!zf;
                ans=-ans;
            }
        }
        if(!(zf&&ans==2))
        {
            cout<<"Case #"<<i<<": NO"<<endl;
            continue;
        }
        zf=true;
        ans=result[k]-'0';
        k++;
        for(;k<len;k++)
        {
            if(zf&&ans==3)
                break;
            ans=arr[ans][result[k]-'0'];
            if(ans<0)
            {
                zf=!zf;
                ans=-ans;
            }
        }
        if(!(zf&&ans==3))
        {
            cout<<"Case #"<<i<<": NO"<<endl;
        }
        else
        {
            cout<<"Case #"<<i<<": YES"<<endl;
        }
    }
    return 0;
}
