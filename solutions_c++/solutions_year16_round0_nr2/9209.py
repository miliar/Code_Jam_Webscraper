#include<iostream>
#include<conio.h>
#include<string.h>
using namespace std;
char a[101],b[101];
int c=0,y=0,e=1;

int main()
{
	FILE *fout = freopen("output.txt", "w", stdout);
	int t;
	cin>>t;
	while(t--)
	{
		c=0;
		
		cin>>a;	int y=strlen(a);
		while(y!=-1)
		{
		//cout<<y<<" ";
		for(int i=0;i<y;i++)
		b[i]=a[i];
		if(a[y-1]=='+')
		
	{
		int i=y-1;
		while((a[i]!='-')&&(y>=0))
		{
			y=y-1;
			i--;
		}
	}
	if(y==-1)
	break;
	else
	{
	
	if(a[0]=='-')
	{c=c+1;
//	cout<<"x";
		for(int i=0,j=y-1;i<y,j>=0;i++,j--)
		{
			if(b[j]=='+')
			a[i]='-';
			else if(b[j]=='-')
			a[i]='+';
			
		}
	}
	else if(a[0]=='+')
	{c=c+1;
	int k=0;
		while((a[k]!='-')&&(k<y))
	{
			a[k]='-';
			k++;
	}
		
	}
	
	
	}
	
}
cout<<"Case #"<<e<<": "<<c<<endl;
	e++;
}
getch();
return 0;
}
