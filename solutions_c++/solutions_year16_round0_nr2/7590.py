#include <iostream>
#include <string>
using namespace std;
int main()
{
	long int t,d=1;
	cin>>t;
	string str;
	char *q,*p,*z;
	do{long int count=0;
		cin>>str;
		
	    q=&str[0];
		p=q;
		z=q;
		
		while(*p!='\0')
		{
			
			p++;
		}
		
		
		p--;
		
		q++;
		while(*q!='\0')
		{
		
		
			if(*q!=*z)
			{count++;
			
			}
			z++;
			q++;
		}
		if(*p=='-')
		{count++;
		}
		
		cout<<"Case #"<<d<<": "<<count<<endl;
		
	d++;}while(d<=t);
	
	
	
	
	return 0;
}