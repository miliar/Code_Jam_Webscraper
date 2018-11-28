#include<iostream>
#include<algorithm>
using namespace std;
bool comp(int a,int b)
{
    return (a>b);
}
int main()
{
    int j=1,t;
    cin>>t;
    while(j<=t)
    {
        int max,i,n,d,arr[1000005]={0},rem=0,re=100000000;
        cin>>d;
        for(i=0;i<d;i++)
            cin>>arr[i];
        sort(arr,arr+d,comp);
        max=arr[0];
        for(i=1;i<=max;i++)
        {
            int temp=0,temp1=i;
            for(int k=0;k<d;k++)
            {
                if(arr[k]>i)
                {
                    temp+=(arr[k]/i);
                    if(arr[k]%i==0)
                        temp--;
                }
            }
            temp+=temp1;
            if(temp<re)
                re=temp;
        }
        cout<<"Case #"<<j<<": "<<re<<"\n";
        j++;
    }
}
