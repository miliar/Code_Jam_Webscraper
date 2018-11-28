#include <iostream>
#include <cstring>
using namespace std;
int arr[10];
void cal(long long int,long long int&);
int main()
{

    int t,i,j,k;long long int n,temp,sum;
    cin>>t;
    for(int k=1;k<=t;k++)
    {   sum=0;int flag=0;
        memset(arr,0,sizeof(arr));
        cin>>n;
        if(n==0)
        {
            cout<<"Case #"<<k<<": "<<"INSOMNIA"<<endl;
            continue;
        }
        temp=n;
        for(i=2;1;i++)
        {
            cal(temp,sum);
            if(sum==55)break;
            temp=n*i;
        }
        cout<<"Case #"<<k<<": "<<temp<<endl;
    }
    return 0;
}
void cal(long long int n,long long int &sum)
{   int temp;
    while(n)
    {
        temp=n%10;
        if(arr[temp]==0)
        {
            arr[temp]=1;
            if(temp==0)sum+=10;
            else sum+=temp;
        }
        n/=10;
    }
}
