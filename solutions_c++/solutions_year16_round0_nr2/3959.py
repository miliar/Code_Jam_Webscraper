#include <bits/stdc++.h>
using namespace std;
int main( void )
{
	int t,k;
	cin>>k;
	for( t = 1 ; t <= k ; t++ )
	{
		int len,i,j,l,c=0;
		string st;
		cin>>st;
		len = st.length();
		for(i=0;i<len;i++)
		{
			if(st[i]=='-')
			{
				if(i==0)
				{
					j = 1;
					while(j<len && st[j]=='-')
						st[j++]='+';
					
					//for(l=0;j<j;l++)
					//	st[l]='+';
					c++;	
				}
				else
				{
					j = i+1;
					while(j<len && st[j]=='-')
						st[j++]='+';
					
	
					c+=2;
				}
			
			}
		
		
		}

		
		printf("Case #%i: %i\n",t,c);
	
	
	}
	




	return 0;
}
