#include<iostream>

using namespace std;

int main()
{	

	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);


	int i,j,t,c;
	char temp;
	
	cin>>t;
	c=t;
	
	while(t--)
	{
		string s;
		
		cin>>s;
		
		for(i=0;s[i]!='\0';i++)
		{
			j=i;
			
			if(int(s[j])>=int(s[0]))
			{	temp=s[j];
				while(j>0)
				{
					
					s[j]=s[j-1];
					j--;
					
				}
				
				s[j]=temp;
			}
			
		}
	
		cout<<"Case #"<<c-t<<": "<<s<<endl;
	}
}
