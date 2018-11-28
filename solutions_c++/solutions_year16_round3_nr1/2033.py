#include<bits/stdc++.h>
using namespace std;
int arr[100];
int cp[100];
int n;
int a1,a2;
int sumarr()
{
    int s=0;
    for(int i=0;i<n;i++)
        s+=arr[i];
    return s;
}
int sumcp()
{
     int s=0;
    for(int i=0;i<n;i++)
        s+=cp[i];
    return s;
}
void copyarr()
{
    for(int i=0;i<n;i++)
        cp[i]=arr[i];
}
void great()
{
    int a1in,a2in;
    a1=-100;a2=-100;
    for(int i=0;i<n;i++)
    {
        if(a1<cp[i])
        {
            a1=cp[i];
            a1in=i;
        }
    }
    cp[a1in]=-200;
    for(int i=0;i<n;i++)
    {
        if(a2<cp[i])
        {
            a2=cp[i];
            a2in=i;
        }
    }
    a1=a1in;
    a2=a2in;
}
bool arck()
{
    for(int i=0;i<n;i++)
    {
        if(arr[i]!=0)
            return false;
    }
    return true;
}
int main()
{
    freopen("A-large.in","r",stdin);
     freopen("B-small-practice12345678.out","w",stdout);
     int t;
     cin>>t;
     int sc=0;
     while(t--)
     {

         cin>>n;
         for(int i=0;i<n;i++)
            cin>>arr[i];
            sc++;
            cout<<"Case #"<<sc<<": ";
        while(!arck())
        {

            int st=sumarr();
            copyarr();
            great();

            if(arr[a1]==arr[a2] && sumarr()%2==0)
            {
                arr[a1]-=1;
                arr[a2]-=1;
                cout<<char(65+a1)<<char(65+a2)<<" ";
            }
            else if(arr[a1]==arr[a2] && sumarr()%2!=0)
            {
                arr[a2]-=1;
                cout<<char(65+a2)<<" ";
            }
            else
                {
                    if(arr[a1]>1)
                    {
                    arr[a1]-=2;
                    cout<<char(65+a1)<<char(65+a1)<<" ";
                    }
                    else
                    {
                        arr[a1]-=1;
                    cout<<char(65+a1)<<" ";
                    }
                }
        }

cout<<endl;
     }
    return 0;
}
