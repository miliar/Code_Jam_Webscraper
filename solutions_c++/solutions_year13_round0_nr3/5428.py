#include<iostream>
#include<vector>
#include<queue>
#include<algorithm>
#include<map>
#include<stack>
#include<stdio.h>
#include<math.h>
#include<string>

using namespace std;

void ntos(int n,char *a,int l)
{
	int i=l-1;
	
	a[l]='\0';
	
	while(n)
	{
		a[i--]=n%10+'0';
		n/=10;
	}
	
}

int leng(long long n)
{
	int l=0;
	
	while(n)
	{
		l++;
		n/=10;
	}
	
	return l;
}

bool checkpalin(char *ch,int l)
{
	int i,j;
	
	for(i=0,j=l-1;i<j;i++,j--)
		if(ch[i]!=ch[j])
			return false;
	
	return true;
}

int ar[10000010][2];

int main()
{
	int j,t,l;
	long long a,b,n,k,m,i;
	double d;
	char ch[20];
	j=0;
	
	for(i=1;i<=10000000;i++)
	{
		if(i<10)
			l=1;
		else if(i<100)
			l=2;
		else if(i<1000)
			l=3;
		else if(i<10000)
			l=4;
		else if(i<100000)
			l=5;
		else if(i<1000000)
			l=6;
		else if(i<10000000)
			l=7;
		else
			l=8;
			
		ntos(i,ch,l);
						
		if(checkpalin(ch,l))
		{
			l=leng(i*i);
			ntos(i*i,ch,l);
			
			if(checkpalin(ch,l))	
			{				
				ar[i][0]=j++;
				ar[i][1]=1;
//				cout<<i<<" "<<(i*i)<<endl;
			}
			else
			{				
				ar[i][0]=j;
				ar[i][1]=0;
			}
		}
		else
		{
			ar[i][1]=0;	
			ar[i][0]=j;
		}
		
		
			
	}
	
	cin>>t;
	
	for(int tt=1;tt<=t;tt++)
	{
		cin>>a>>b;
		
		d=sqrt(a);
		k=sqrt(a);
		
		if(d!=k)
			k++;
		
		d=sqrt(b);
		m=sqrt(b);					
		
		cout<<"Case #"<<tt<<": "<<(ar[m][0]-ar[k][0]+ar[m][1])<<endl;		
	}
	
	return 0;
}