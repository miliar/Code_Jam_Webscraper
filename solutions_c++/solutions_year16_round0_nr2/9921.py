#include<bits/stdc++.h>
using namespace std;

int main()
{
	int t=0,q;
	bool f=1;
	long long int x,len=0;
	cin>>t;
	for(q=0;q<t;q++)
	{
	    x=0;
		char str[101];
		cin>>str;
        len=strlen(str);
		for(int j=len-1;j>=0;j--)
		{
			f=1;
			for(int k=0;k<len;k++)
			{
				if(str[k]!='+') 
				f=0;
			}
			if(f) break;
			if(str[j]=='-')
			{
				for(int k=0;k<=j;k++)
				 {
					if(str[k]=='-')
					str[k]='+';
					else str[k]='-';
				 }
				x++;
		    }
     	}
     	printf("Case #%d: %lld\n",q+1,x);
	}
	return 0;
}