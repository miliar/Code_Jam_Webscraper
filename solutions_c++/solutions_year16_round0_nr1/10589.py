#include<iostream>
using namespace std;
int main()
{
    long long int n,r,dig,temp,i,res,cnt,flag,t,j,arr[205];
    cin>>t;
    for(i=0;i<t;i++)
        cin>>arr[i];
    for(j=0;j<t;j++)
    {

        flag=0;
    int a[10]={0};
     cnt=0;
    n=arr[j];
    for(i=1;i<=202;i++)
    {
        res=i*n;
        temp=res;
        while(temp!=0)
        {
            dig=temp%10;
            temp/=10;
            if(a[dig]==0)
            {
                a[dig]=1;
                cnt++;

            }
            if(cnt==10)
            {
               flag=1;
               break;
            }


        }

        if(flag==1)
        {

          break;
        }

    }
    cout<<"Case #"<<j+1<<": ";
    if(flag==1)
        cout<<res<<"\n";
    if(flag==0)
    cout<<"INSOMNIA\n";
    }



    return 0;
}
