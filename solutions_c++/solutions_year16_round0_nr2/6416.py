#include <iostream>
using namespace std;
int main()
{
	int t,i,count,j,k;
	char str[100000],c;
	cin>>t;
	for(i=1;i<=t;i++)
	{
		k=0;count=0;
		cin>>str;
		while(str[k]!='\0')
		{
			c=str[k];
			while(str[k]==c)
				k++;
			count++;

		}
		if(c=='+')
			count--;
		cout<<"Case #"<<i<<": "<<count<<endl;
	}
}