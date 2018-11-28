#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
    int arr[5][5],arr1[5][5],t,temp=0,value,flag=1,c=0,ans1,ans2;
    char str1[]="Volunteer cheated!";
    char str2[]="Bad magician!";
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    cin>>t;
    while(t--)
    {
        temp++;
        cin>>ans1;
        for(int i=1;i<=4;i++)
        for(int j=1;j<=4;j++)
        cin>>arr[i][j];
        cin>>ans2;
        for(int i=1;i<=4;i++)
        for(int j=1;j<=4;j++)
        cin>>arr1[i][j];
        for(int i=1;i<=4;i++)
        for(int j=1;j<=4;j++)
        if(arr[ans1][i]==arr1[ans2][j])
        {
        flag=0;
        c++;
        value=arr[ans1][i];
        }
        if(flag)
        cout<<"Case #"<<temp<<": "<<str1<<endl;
        else if(c>1)
        cout<<"Case #"<<temp<<": "<<str2<<endl;
        else
        cout<<"Case #"<<temp<<": "<<value<<endl;
        flag=1;
        c=0;
    }
return 0;
}
