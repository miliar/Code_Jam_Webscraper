#include<bits/stdc++.h>
using namespace std;

char buffer [7];

int sum=0;
int check(char ch)
{
	if(ch=='0')
		return 0;
	else if (ch=='1')
		return 1;
	else if(ch=='2')
		return 2;
	else if (ch=='3')
		return 3;
	else if(ch=='4')
		return 4;
	else if (ch=='5')
		return 5;
	else if(ch=='6')
		return 6;
	else if (ch=='7')
		return 7;
	else if(ch=='8')
		return 8;
	else if (ch=='9')
		return 9;
        return -1;
}
int main()
{
	int t,f=0,len;
	scanf("%d",&t);
	long int n,num,l;
	
	string s;
	for(int i=1; i<=t; i++)
	{  
        
    sum=0;
    int digit[10]={0,1,2,3,4,5,6,7,8,9};
  
		scanf("%d",&n);
        if(n==0)
            cout<<"Case #"<<i<<": "<<"INSOMNIA"<<"\n";
            else{
		num=n;
		for( l=1;sum!=(-10);l++)
		{
			sum=0;
		n=num*l;
	
		s=itoa(n,buffer,10);
		
        len=s.length();
		for(int j=0;j<len;j++)
			{
				f=check(s[j]);
				digit[f]=-1;
					
			}
		
			for(int k=0;k<10;k++)
			{
				
				sum+=digit[k];
			}
			
		}
		cout<<"Case #"<<i<<": "<<n<<"\n";
            }
	}
	return 0;
}