#include<iostream>
#include<string.h>
#include<math.h>
#include<sstream>
using namespace std;
int main()
{
	freopen("C-small-attempt0.in","r",stdin);
    freopen("shoutput.txt","w",stdout);
	int t;
	cin>>t;
	int trev=1;
	while(t>0)
	{
	
	int a,b;
	cin>>a>>b;
	int count=0;
	for(float c=a ;c<=b;c++)
	{
		float req=sqrt(c);
		int flag_a=0;
		int flag_b=0;
		string req_sqrt = static_cast<ostringstream*>( &(ostringstream() <<req ) )->str();
		string req_int = static_cast<ostringstream*>( &(ostringstream() <<c ) )->str();
		for(int d=0;d<=req_sqrt.length()/2;d++)
		{
			
			if(req_sqrt[d]!=req_sqrt[req_sqrt.length()-d-1])
			{
				flag_a=1;
				break;
			}
			
		}
		for(int d=0;d<=req_int.length()/2;d++)
		{
			
			if(req_int[d]!=req_int[req_int.length()-d-1])
			{
				flag_b=1;
				break;
			}
			
		}
		if(flag_a==0 && flag_b==0)
		{
			count++;
		}
	}
	cout<<"Case #"<<trev<<": "<<count<<endl;
	t--;
	trev++;
}
	return 0;
}
