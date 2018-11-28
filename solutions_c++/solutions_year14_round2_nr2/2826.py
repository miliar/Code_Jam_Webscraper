#include<iostream>
using namespace std;
int main()
{
 int t,cases;
 cin>>t;
 cases =0;
 while(t-->0){
		cases++;
	int a,b,k;
	long long count=0;
	cin>>a>>b>>k;
	for(int i=0;i<a;i++)
	{
	 for(int j=0;j<b;j++)
	 {
	  if((i&j) < k)
	  {
		//cout<<" "<<i<<" "<<j<<endl;
	   	count++;
		   }
	  }
	}
	cout<<"Case #"<<cases<<": "<<count<<endl; 
	}
	cin.get();
cin.get();	
return 0;
}
