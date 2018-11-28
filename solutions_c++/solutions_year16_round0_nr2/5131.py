#include<iostream>
#include<conio.h>
using namespace std;
int main()
{
	int n,nc,count;
	int i,j;
	char a[101],ch;
	
	
	cin>>n;
	nc=n;
	while(n>0)
	{
		count=0;
		cin>>a;
		ch=a[0];
		for(i=1;a[i]!='\0';i++)
		{
			if(a[i]!=ch)
			{
				count++;
				ch=a[i];
			}
		}
		if(ch=='-')
			count++;
		cout<<"Case #"<<(nc-n)+1<<": "<<count<<endl;
		n--;
	
		
	}
}
