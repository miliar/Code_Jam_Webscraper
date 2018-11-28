# include<iostream>
using namespace std;
int main()
{
    freopen("A:\\in.in","r",stdin);
    freopen("A:\\out.txt","w",stdout);
    long long int num[42]={0,1,2,3,11,22,101,111,121,202,212,1001,1111,2002,10001,10101,10201,11011,11111,11211,20002,20102,100001,101101,110011,111111,200002,1000001,1001001,1002001,1010101,1011101,1012101,1100011,1101011,1102011,1110111,1111111,1112111,200002,2001002,100000000};
    long long int arr[42];
    for(int i=0;i<42;i++)
    {
            arr[i]=num[i]*num[i];
    }
    
    int t,x=1;
    cin>>t;
    while(t--)
    {
           long long int a,b,count1=0;
           cin>>a;
           cin>>b;
           for(int i=0;i<42;i++)
           {
                   if(arr[i]>=a&&arr[i]<=b)
                   count1++;
           }
           cout<<"Case #"<<x<<": "<<count1<<"\n";
           x++;
    }
}
