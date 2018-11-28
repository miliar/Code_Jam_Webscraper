#include <bits/stdc++.h>

using namespace std;


int main()
{
	int n,t;
	freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);
	
	scanf("%d",&t);
	int tst=0;
	char s[105];
	
	while(t--)
	{
		tst++;
		
		scanf("%s",s);
		n= strlen(s);
		int fg=1;
		int ans=0;
		int j=n-1;
		
		while(1)
		{
		  	 while(s[j]=='+' && j>=0)
		  	 {
		  	 	s[j]='+';
			    j--;
		     }
              if(j<0)
		  	  break;
		  	
			while(s[j]=='-' && j>=0)
		  	 {
		  	 	s[j]='+';
			    j--;
		     }
		     
			 ans++;   	 
		  	 
			 if(j<0)
		  	  break;
		  	  
		  	 for(int i=0;i<=j;i++)
		  	   if(s[i]=='+') s[i]='-';
		  	 else s[i]='+';
		}
	    printf("Case #%d: %d\n",tst,ans);   
	}
	
	return 0;
}
