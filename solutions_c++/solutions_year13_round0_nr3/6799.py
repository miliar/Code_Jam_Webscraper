#include<iostream>
using namespace std;
#include<stdio.h>
#include<string.h>
#include<math.h>

int sq();
int palindrome();
int sq(int n)
{
	int a;
	float f=0;
	a=sqrt(n);
	
	if(a*a==n)
	{
		f=1;
	//	cout<<"a="<<a<<endl<<"n="<<n<<endl;
		return a;
		
	}
	else return 0;

	
}
int palindrome(char ar[])
{
	int len;
	int f=1,j,l;
	len =strlen(ar);
	//cout<<len<<endl;
	l=len/2;
	for(j=0;j<=l;j++)
	{
		len--;
		if(ar[j]!=ar[len])
		{
			f=0;
			break;
		}
		if(!f) break;
	}
	if(f) return true;
	else return false;
}
void main()
{
	freopen("f.txt","r",stdin);
	freopen("fairout.txt","w",stdout);
	int n;
	int i,j;
	int s,f;
	int pal=0,sqr=0,sqr_pal=0,count=0;
	char *ar,*arr;
	ar=new char[10];
	arr=new char[10];
	cin>>n;
	for(i=1;i<=n;i++)
	{
		cin>>s>>f;
		for(j=s;j<=f;j++)
		{
			itoa(j,ar,10);
			pal=palindrome(ar);
			
			if(pal)
			{
				sqr=sq(j);
				if(sqr)
				{
					//cout<<"sqr root of "<<j<<"is ="<<sqr<<endl;
					itoa(sqr,arr,10);
					//cout<<arr<<endl;
					sqr_pal=palindrome(arr);
					if(sqr_pal) 
					{
						count++;
						//cout<<"count="<<count<<endl;
					}
				}

			}
		

		}
		cout<<"Case #"<<i<<": "<<count<<endl;
		count=0;
		pal=0;
		sqr=0;
		sqr_pal=0;

	}
	

}