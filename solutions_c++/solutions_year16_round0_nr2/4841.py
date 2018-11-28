#include <iostream>
#include<string>
using namespace std;

int index=1;
int main()
{
int tcase,r;
string s;
long long n;
scanf("%d",&tcase);
while(tcase--)
{	long long count=0;
	cin>>s;
	r=s.length();
	char z=s[0];
	for(int i=0;i<r;i++)
	{
		
		if(s[i]!=z)
		{	count++;
			z=s[i];
			continue;
		}
	}
	if(s[r-1]=='-')
	count++;
	cout<<"Case #"<<index<<": "<<count<<endl;
	index++;
}
}
		
		
		
		
		
