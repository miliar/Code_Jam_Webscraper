#include <iostream>
using namespace std;
char prod(char x,char y)
{
	if(x=='1')
	{
		return y;
	}
	else if(x=='i')
	{
		switch(y)
		{
			case '1':return 'i';break;
			case 'i':return '2';break;
			case 'j':return 'k';break;
			case 'k':return 'J';break;
			case '2':return 'I';break;
			case 'I':return '1';break;
			case 'J':return 'K';break;
			case 'K':return 'j';break;
		}
	}
	else if(x=='j')
	{
		switch(y)
		{
			case '1':return 'j';break;
			case 'i':return 'K';break;
			case 'j':return '2';break;
			case 'k':return 'i';break;
			case '2':return 'J';break;
			case 'I':return 'k';break;
			case 'J':return '1';break;
			case 'K':return 'I';break;
		}
        }
else if(x=='k')
	{
		switch(y)
		{
			case '1':return 'k';break;
			case 'i':return 'j';break;
			case 'j':return 'I';break;
			case 'k':return '2';break;
			case '2':return 'K';break;
			case 'I':return 'J';break;
			case 'J':return 'i';break;
			case 'K':return '1';break;
		}
}
else if(x=='2')
	{
		switch(y)
		{
			case '1':return '2';break;
			case 'i':return 'I';break;
			case 'j':return 'J';break;
			case 'k':return 'K';break;
			case '2':return '1';break;
			case 'I':return 'i';break;
			case 'J':return 'j';break;
			case 'K':return 'k';break;
		}
}
else if(x=='I')
	{
		switch(y)
		{
			case '1':return 'I';break;
			case 'i':return '1';break;
			case 'j':return 'K';break;
			case 'k':return 'j';break;
			case '2':return 'i';break;
			case 'I':return '2';break;
			case 'J':return 'K';break;
			case 'K':return 'j';break;
		}
}
else if(x=='J')
	{
		switch(y)
		{
			case '1':return 'J';break;
			case 'i':return 'k';break;
			case 'j':return '1';break;
			case 'k':return 'I';break;
			case '2':return 'j';break;
			case 'I':return 'K';break;
			case 'J':return '2';break;
			case 'K':return 'i';break;
		}
}
else if(x=='K')
	{
		switch(y)
		{
			case '1':return 'K';break;
			case 'i':return 'J';break;
			case 'j':return 'i';break;
			case 'k':return '1';break;
			case '2':return 'k';break;
			case 'I':return 'j';break;
			case 'J':return 'I';break;
			case 'K':return '2';break;
		}
}
}


int main() {
	int t,i,l,x,j,c,k,m;
	cin>>t;
	for(i=1;i<=t;i++)
	{
		c=0;
		cin>>l>>x;
		char a[l*x+1];
		a[0]='1';
		for(j=1;j<l+1;j++)
		cin>>a[j];
		for(j=l+1;j<=l*x;j++)
		a[j]=a[j-l];
		for(j=1;j<l*x;j++)
		{
			if(prod(a[j-1],a[j])=='i')
			{
				
				c=1;
				a[j]='1';
				break;
			}
			a[j]=prod(a[j-1],a[j]);
		}
		if(c==1)
		{
			for(k=j+1;k<l*x;k++)
			{
				if(prod(a[k-1],a[k])=='j')
				{
					
					c=2;
					a[k]='1';
					break;
				}
				a[k]=prod(a[k-1],a[k]);
			}
		}
		if(c==2)
		{
			for(m=k+1;m<=l*x;m++)
			{
				a[m]=prod(a[m-1],a[m]);
			}
			if(a[m-1]=='k')
			{
				c=3;
			}
			
		}
		if(c==3)
		cout<<"Case #"<<i<<": YES"<<"\n";
		else
		cout<<"Case #"<<i<<": NO"<<"\n";
		
			
		}
	}
	