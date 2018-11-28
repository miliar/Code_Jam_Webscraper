#include<bits/stdc++.h>
using namespace std;
int main()
{
	 int t;
	 cin>>t;
	 int len,cnt,i;
	 char arr[105];
	 for(int j=1;j<=t;j++)
	  {
	  	 scanf("%s",arr);
	  	 len=strlen(arr);
	  	 cnt=0;
	  	 while(1)
	  	 {
	  	    for( i=len-1;i>=0;i--)
			   {
			       if(arr[i]=='-')
			        {
			        	break;
					}
				    	
			   }
			   if(i==-1)
			     break;
			   cnt++;
			   while(arr[i]=='-'&&i>=0)
			     {
				   arr[i]='+';
				   i--;
			     }
			   while(i>=0)
			     {
			     	if(arr[i]=='+')
			     	 arr[i]='-';
			     	else
			     	 arr[i]='+';
			     	i--;
				 }
		 }
	  	 cout<<"Case #"<<j<<": "<<cnt<<endl;
	  }
	return 0;
}