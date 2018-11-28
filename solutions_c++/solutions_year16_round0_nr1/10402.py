#include <iostream>
#include <stdlib.h>
using namespace std;

int main() {
	// your code goes here
	long long t,n,zero,one,two,ans,three,four,five,six,seven,eight,nine,a1,a,q,j=1;
	zero=one=two=three=four=five=six=seven=eight=nine=0;
	
	cin>>t;
	a=a1=q=0;
	ans=-1;
	for(int o=1;o<=t;o++)
	{
		zero=one=two=three=four=five=six=seven=eight=nine=0;
		
		a=a1=q=0;
		ans=0;
		cin>>n;
		
			for(j=1;j<100;j++)
			{
				
				a=j*n;
				a1=a;
			
				while(a>0)
				{
					q=a%10;
					if(q==0)
						zero++;
					else if(q==1)
							one++;
					else if(q==2)
							two++;
					else if(q==3)
							three++;
					else if(q==4)
							four++;
					else if(q==5)
							five++;
					else if(q==6)
							six++;
					else if(q==7)
							seven++;
					else if(q==8)
							eight++;
					else if(q==9)
							nine++;
					
					a=a/10;
				}	
				if((zero>0)&&(one>0)&&(two>0)&&(three>0)&&(four>0)&&(five>0)&&(six>0)&&(seven>0)&&(eight>0)&&(nine>0))
				{
					ans=a1;
					goto x;
				}
				
			}
					
		x:
		if((zero==0)||(one==0)||(two==0)||(three==0)||(four==0)||(five==0)||(six==0)||(seven==0)||(eight==0)||(nine==0))	
		cout<<"Case #"<<o<<": "<<"INSOMNIA\n";
		else
		cout<<"Case #"<<o<<": "<<ans<<"\n";
		
	
		
	}
	return 0;
}