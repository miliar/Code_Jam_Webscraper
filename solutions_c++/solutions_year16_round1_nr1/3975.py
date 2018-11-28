#include<iostream>
#include<string.h>

using namespace std;
void strfcat(char a[],char b)
{
	int n;	
	n=strlen(a);
	for(int i=n;i>=0;i--)
	{
		a[i+1]=a[i];
		
	}
	a[0]=b;

}
void strlcat(char a[],char b)
{
	int n;
	n=strlen(a);
	a[n]=b;
	a[n+1]='\0';

}

int main()
{
	int n,nc,len;
	char str[1001];
	int i,j;
	char ans[1001];
	cin>>n;
	nc=n;
	while(n>0)
	{
		cin>>str;
		ans[0]='\0';
		len=strlen(str);
		
		for(i=0;i<len;i++)
		{
			if(ans[0]>str[i])
				strlcat(ans,str[i]);
			else 
				strfcat(ans,str[i]);
		}
		
		
		cout<<"Case #"<<(nc-n)+1<<": "<<ans<<endl;
		n--;
	}
}
