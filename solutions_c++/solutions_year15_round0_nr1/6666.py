
#include<iostream>
#include<stdio.h>
#include<stdlib.h>
using namespace std;
#define MAX 1001
int main()
{
    int t,n=1;
        freopen("in.in","r",stdin);
        freopen("sandy.txt","w",stdout);

    cin>>t;
    while(t--)
    {
        int maxi,cnt=0,cnt1=0,temp;
        char s[MAX];
        cin>>maxi;
        cin>>s;
        for(int i=0;i<=maxi;i++)
        {
           // cout<<cnt;
            if(cnt<i){
                temp=i-cnt;
                cnt1+=temp;
                cnt=cnt+temp;
            }
             cnt+=s[i]-48;
        }
    cout<<"Case #"<<n<<": "<<cnt1<<endl;
        n++;
    }
    return 0;
}
