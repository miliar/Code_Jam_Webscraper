#include<iostream>
#include<map>
using namespace std;
int main()
{
	bool fap[1001];
	for(int i=0;i<=1000;i++)
	{
		fap[i]=false;
	}
	fap[1]=true;
	fap[4]=true;
	fap[9]=true;
	fap[121]=true;
	fap[484]=true;
	int test;
	cin>>test;
	//cout<<fap[100];
	int c=1;
	while(test--)
	{
		int a,b,count=0;
		cin>>a>>b;
		
		for(int i=a;i<=b;i++)
		{
			if(fap[i])
			count++;			
		}
		cout<<"Case #"<<c++<<": "<<count<<endl;
	}
	
	
	
	
	
	return 0;
}
