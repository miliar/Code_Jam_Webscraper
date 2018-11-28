#include<iostream>
#include<math.h>
using namespace std;
int palindrome(int );
main()
{
	int t,i=0,x=0;
	//cout<<"enter the no of test cases\n";
	cin>>t;
	int count[100]={0},p,ch1,ch2,m,n;
	double k;
 while(x<t)
	{
		//cout<<"enter the range."<<endl;
		cin>>m>>n;
			for(i=m;i<=n;i++)
			{
				//	count[x]=0;
					p=i;
					ch1=palindrome(i);
					if(ch1==1)
						{
							k=sqrt(i);
							if((k-(int)k)==0)
								{
								ch2=palindrome((int)k);
									if(ch2==1)
									{
									count[x]++;
										//cout<<m<<endl;
    								}
								}
			
							}//cout<<"case #"<<x+1<<count[x]<<endl;
    			}x++;
	}
	for (x=0;x<t;x++){
	cout<<"Case #"<<x+1<<": "<<count[x]<<endl;
		}
//getch();
}

int palindrome(int n)
{
	int m,rev=0,rem;
	m=n;
	while(n>0)
	{
		rem=n%10;
		rev=rev*10+rem;
		n=n/10;
	}//out<<"rev"<<rev<<endl;
	if(m==rev)
	return 1;
	else
	return 0;
}

/*
int palindrome(double n)
{
double m,rev=0,rem;
	m=n;
	while(n>0)
	{
		rem=n%10;
		rev=rev*10+rem;
		n=n/10;
	}cout<<"rev"<<rev<<endl;
	if(m==rev)
	return 1;
	else
	return 0;
}


*/
