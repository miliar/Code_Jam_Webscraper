#include<vector>
#include<algorithm>
#include<string>
#include<iostream>

using namespace std;

int main()
{
    int c;
    int arr[]={0,1,4,9,121,484};
    cin>>c;
    int t=0;
    while(++t<=c)
    {
                 int a,b,count=0;
                 cin>>a>>b;
                 
                 for(int i=0;i<6;i++)
                 if(arr[i]>=a && arr[i]<=b)
                 count++;
                 
                 cout<<"Case #"<<t<<": "<<count<<endl;                        
    }
    return 0;
}
