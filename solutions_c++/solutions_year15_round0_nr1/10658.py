#include<iostream>
#include<string.h>
using namespace std;

int main()
{
	int T;
	cin>>T;
	int i=0;
	for(i;i<T;i++)
	{
		int Smax;
		cin>>Smax;
		char *str = new char[Smax+2];
		cin>>str;
		int size = strlen(str);
		int cnt=0,extra=0;
		for(int j=0;j<size;j++)
		{
			int val=(int)str[j]-(int)'0';
			
			if(j!=0 && val!=0 && cnt<j )
			{
				extra+= j-cnt;
				cnt+=extra;
			}
				
			cnt+=val;
			
			
		}
		cout<<"Case #"<<i+1<<": "<<extra<<endl;
	}
	
}