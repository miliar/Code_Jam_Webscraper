#include<stdio.h>
#include<iostream>
#include<string.h>

using namespace std;

int main()
{
    int i,t,j,n,ctr;
    string str;
    cin>>t;
    for(i=0;i<t;i++)
    {
        ctr=0;
        cin>>n>>str;
        int arr[n+1],cnt=0;
        for(j=0;j<=n;j++)
        {
            arr[j]=(int)str[j]-48;
            //cout<<arr[j];
            if(cnt<j)
            {
                cnt++;
                ctr++;
            }
            cnt=cnt+arr[j];
        }
        cout<<"Case #"<<i+1<<": "<<ctr<<"\n";
    }
    return 0;
}
