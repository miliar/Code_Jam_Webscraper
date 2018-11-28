#include <iostream>
using namespace std;

int main()
{
   
   int T,cno=1,count,i,j,a,b,k,value;
   cin>>T;
   while(T!=0)
   {
   	cin>>a;
   	cin>>b;
   	cin>>k;
   	count=0;
   	for(i=0;i<a;i++)
   	{
   		for(j=0;j<b;j++)
   		{
   			value=i&j;
   			if(value<k)
   			count++;
   		}
   	}
   	cout<<"Case #"<<cno<<": "<<count<<endl;
   	cno++;
   	T--;
   }
    return 0;
}
