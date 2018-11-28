#include<iostream>
#include<stdio.h>
#include<algorithm>
#include<cmath>
#include<cstring>
#include<vector>

using namespace std;

int main()
{
    freopen("input.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t,x,i,j,fans,sans,temp,f[5],s[5],temp2;
    cin>>t;
    for(x=1;x<=t;x++)
    {
        cin>>fans;
        for(i=1;i<=4;i++)
        {
            for(j=1;j<=4;j++)
            {
                cin>>temp;
                if(i==fans)
                {
                    f[j]=temp;
                }
            }
        }
        cin>>sans;
        for(i=1;i<=4;i++)
        {
            for(j=1;j<=4;j++)
            {
                cin>>temp;
                if(i==sans)
                {
                    s[j]=temp;
                }
            }
        }
        temp=0;
        for(i=1;i<=4;i++)
        {
            for(j=1;j<=4;j++)
            {
                if(f[i]==s[j])
                {
                    temp++;
                    temp2=f[i];
                }
            }
        }
        if(temp==1)
        {
            cout<<"Case #"<<x<<": "<<temp2<<endl;
        }
        else if(temp>1)
        {
            cout<<"Case #"<<x<<": "<<"Bad magician!"<<endl;
        }
        else
        {
            cout<<"Case #"<<x<<": "<<"Volunteer cheated!"<<endl;
        }
    }
}
