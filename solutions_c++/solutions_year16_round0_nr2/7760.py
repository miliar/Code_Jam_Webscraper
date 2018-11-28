 #include<iostream>
#include<cstdio>
#include<string>
using namespace std;
int main()
{
	string sadiq,nabila;
	long long i,t,j,k,co,temp;
	cin>>t;
	for(i=1;i<=t;i++)
	{
		cin>>sadiq;
		co=0;
		cout<<"Case "<<"#"<<i<<": ";
	 for(j=0;j<sadiq.size();j++)
	 {
		 if(sadiq[j]=='+')
			 co++;
	 }
	  if(co==sadiq.size())
	  {
		  cout<<0<<"\n";
		  continue;
	  }
	   co=0,temp=0;
	  while(1)
	  {
		  temp++;
		  for(j=sadiq.size()-1;j>=0;j--)
		  {
			  if(sadiq[j]=='-')
				  break;
		  }
		  nabila="";
		  for(k=0;k<sadiq.size();k++)
		  {
			  if(k<=j)
			  {
				  if(sadiq[k]=='-')
					  nabila=nabila+'+';
				  else
					  nabila=nabila+'-';
			  }
			  else
				  nabila=nabila+sadiq[k];
		  }
		  co=0;
		  for(j=0;j<nabila.size();j++)
		  {
			  if(nabila[j]=='+')
				  co++;
		  }
		 // cout<<sadiq<<" "<<nabila<<"\n";
		  if(co==nabila.size())
			  break;
		  sadiq=nabila;

	  }
	  cout<<temp<<"\n";

	}

}