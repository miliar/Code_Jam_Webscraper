#include<bits/stdc++.h>
using namespace std;
int main()
{
  int tc,ans,i,j,k,pos,p=1,count;
  string pies;
  freopen("B-large.in","r",stdin);
  freopen("B-large.out","w",stdout);
  cin>>tc;
  while(tc--)
  {
  	cin>>pies;
  	count=0;
  	int l;l=pies.length();
  	if(l==1&&pies[l-1]=='-')
  	cout<<"case #"<<p++<<": "<<1<<endl;
  	else
  	{
  	for(i=l-1;i>=0;i--)
  	{
  		if(pies[i]=='-')
  		{
  			if(pies[l-1]=='-')
		  count++;
		  break;}
	  }
	  if(pies[l]=='-')
	  pos=i;
	  else
	  pos=i+1;
  	for( j=pos;j>=0;j--)
  	{
  		if(pies[j]=='-')
  		{
  		     for(k=j;k>=0;k--)
  		     {
  		     	if(pies[k]=='+')
  		     	{count++;
  		     		break;
				   }
			   }
			   j=k+1;
		  }
		  else
		  {
		  	for(k=j;k>=0;k--)
		  	{
		  		if(pies[k]=='-')
		  		{
		  			count++;
		  			break;
				  }
			  }
			  j=k+1;
		  }
	  }
	if(pies[l-1]=='-')
	cout<<"case #"<<p++<<": "<<count-1<<endl;
	else
		cout<<"case #"<<p++<<": "<<count<<endl;
  }
}
return 0;
  
}
