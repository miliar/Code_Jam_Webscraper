#include<iostream>

using namespace std;

int main()
{	
		freopen("B-large.in","r",stdin);
	   freopen("B-large.out","w",stdout);
    
    
	int t,m,p,i,j,k,c;
	
	cin>>t;
	
	c=t;
	
	while(t--)
	{
		string s;
		
		cin>>s;
		
		for(i=0;;i++)
		{	m=-1;
			p=-1;
			
			for(j=0;s[j]!='\0';j++)
				if(s[j]=='-')
				m=j;
			
		//	cout<<"length - "<<sizeof(s)<<" m - "<<m<<endl;
			
			for(j=0;j<m;j++)
			if(s[j]=='+')
			p=j;
			
			if(m==-1)
			break;
			
			if(s[0]=='-')
			{
				j=m;
				k=0;
				
				int arr[m+1];
				
				for(k=0,j=m;j>=0;k++,j--)
				{
					if(s[j]=='+')
					arr[k]=0;
					else arr[k]=1;
				}
				
				for(k=0;k<=m;k++)
				{
					if(arr[k]==0)
					s[k]='-';
					else s[k]='+';
				}
				
			}
			else {
				j=p;
				k=0;
				
				int arr[m+1];
				
				for(k=0,j=p;j>=0;k++,j--)
				{
					if(s[j]=='+')
					arr[k]=0;
					else arr[k]=1;
				}
				
				for(k=0;k<=p;k++)
				{
					if(arr[k]==0)
					s[k]='-';
					else s[k]='+';
				}
			}
			
		//	cout<<i+1<<" - "<<s<<endl;
		
		}
		
		cout<<"Case #"<<c-t<<": "<<i<<endl;
	}
}
