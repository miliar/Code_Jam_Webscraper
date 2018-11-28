#include <iostream>
#include <cstring>
#include <cstdio>
#include <stdio.h>
using namespace std;

int main()
{
    freopen ("myfile.in","r",stdin);
     freopen ("myfile.out","w",stdout);
    int t;
    cin>>t;int cas=1;
    while(t--){

    int sol;
    cin>>sol;
    int arr[4];
    bool chosen[20];
    memset(chosen,false,20);
    for(int i=0;i<4;i++)
    {
        int l;
        for(int j=0;j<4;j++)
        {
            if(sol== (i+1) )
            {
               cin>> arr[j];
               chosen[arr[j]]=true;
            }
            else
            {
                cin>>l;
            }
        }
    }
    int sol2;
    cin>>sol2;
    int cnt=0;
    int print=-1;
    for(int i=0;i<4;i++)
    {
        int l;
        for(int j=0;j<4;j++)
        {
            if(sol2== (i+1) )
            {
               cin>> l;
               if(chosen[l])
               {
                   cnt++;
                   print=l;
               }
            }
            else
            {
                cin>>l;
            }
        }
    }
    cout<<"Case #"<<cas<<": ";
    cas++;
    if(cnt==0)
    {
        cout<<"Volunteer cheated!"<<endl;
    }
    else if(cnt==1)
    {
        cout<<print<<endl;
    }
    else
    {
        cout<<"Bad magician!"<<endl;
    }
    }
    return 0;
}
