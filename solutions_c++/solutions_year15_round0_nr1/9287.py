#include<bits/stdc++.h>

using namespace std;

int main()
{
	freopen("A-large.in","r",stdin);

	freopen("output.out","w",stdout);

  	
	long int t=0,i=0,j=1,max=0,audience=0,val=0;
	long int addaud=0;	        
	cin>>t;
     	while(j<=t)
	{
		cin>>max;		
		string s;
		cin>>s;
		addaud=0;

		switch(s[0])
			{
				case '0':val=0;
					break;
				case '1':val=1;
					break;
				case '2':val=2;
					break;
				case '3':val=3;
					break;
				case '4':val=4;
					break;
				case '5':val=5;
					break;
				case '6':val=6;
					break;
				case '7':val=7;
					break;
				case '8':val=8;
					break;
				case '9':val=9;
					break;
			}		

		audience=val;	
		for(i=1;i<s.length();i++)
		{
			
			switch(s[i])
			{
				case '0':val=0;
					break;
				case '1':val=1;
					break;
				case '2':val=2;
					break;
				case '3':val=3;
					break;
				case '4':val=4;
					break;
				case '5':val=5;
					break;
				case '6':val=6;
					break;
				case '7':val=7;
					break;
				case '8':val=8;
					break;
				case '9':val=9;
					break;
			}
				
			if(audience>=i||val==0)
					{
						
						audience+=val;
						continue;
					}	
			else
				{
					addaud+=(i-audience);
					audience+=val+(i-audience);
				}		
		}	
				
				
         	cout<<"Case #"<<j<<": "<<addaud<<"\n";
		j++;
	}
}
