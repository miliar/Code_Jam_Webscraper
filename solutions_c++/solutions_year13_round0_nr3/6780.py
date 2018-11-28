#include<iostream>
using namespace std;
int main()
{
    int n;
    cin>>n;
    int arr[]={0, 1, 2, 3, 11, 22,101, 111, 121, 202, 212,1001, 1111, 2002,10001, 10101, 10201, 11011, 11111, 11211,20002, 20102, 100001, 101101, 110011, 111111, 200002,1000001, 1001001};
    for(int k=1;k<=n;k++)
    {
      int i=0,a,b,j=0;
      cin>>a>>b;
     while(1)
     {
      if(arr[i]*arr[i]<a)
      i++;
      else if(arr[i]*arr[i]<=b)
      {
       j++;
       i++;
      }
      else
      break;
     }
     cout<<"case #"<<k<<": "<<j<<endl;
   }
}