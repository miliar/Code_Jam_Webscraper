#include <iostream>
using namespace std;

int main() 
{
 int limit;
 char ch[7];
 int arr[7],ar1[7],ar2[7],Smax;
 cin>>limit;
 for(int i=0;i<limit;i++)
 {
 	cin>>Smax;
 	for(int i=0;i<=Smax;i++)
 	{
 		cin>>ch[i];
 		arr[i]=ch[i]-48;
 	}
 	int sum=0;
	for(int k=0;k<=Smax;k++)
	{
	sum+=arr[k];
	ar1[k]=sum;
	}
int sub;
    for(int j=1;j<=Smax+1;j++)
    {
        sub=j-ar1[j-1];
        ar2[j]=sub;
    }
    
    int max=0;
   for(int s=1;s<=Smax;s++)
    {
      if(ar2[s]>max)
      max=ar2[s];
    }
  
   cout<<"Case #"<<i+1<<":"<<" "<< max<<endl;
	}
	return 0;
}