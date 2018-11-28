#include<iostream>
#include<string>
#include<fstream>
using namespace std;
int main()
{
	int sum;
	int c=0,T,n;
	ifstream in("B-large.in");
	in>>T;
	//cout<<"enter the number of test cases";
	//cin>>T;
	for(int i=1;i<=T;i++)
	{
		string s;
		char r;
		int l,p,count=0;
		
		//cout<<"enter the string";
		//cin>>s;
		in>>s;
		l=s.length();
		//l=4;
		p=l;
		char stack[l];
		for(int j=0;j<l;j++)
		{
			stack[j]=s[j];
	//		cout<<stack[j];
			
		}
		sum=0;
		int j=0;
		while(sum!=l)
		{
		
	int t=0,	c=0,n=0;
	sum=0;
	//count++;
		
	//cout<<"hello";	
		
		
			r=stack[0];
		///	int count =0;
		for(int k=1;k<l;k++)
		{
		
			if(stack[k]!=r)
			{
			 n=k;
				break;
			}
			else 
			n=0;
		}
		//cout<<n<<endl;
	if(n>0)
	{
	count++;
			for(int t=0;t<n;t++)
				{
					if(stack[t]=='+')
					{
						stack[t]='-';
						//cout<<"hi";
						
					}
					else
					{
						//cout<<"hello";
						stack[t]='+';
						//cout<<stack[t];
					}
		//			count++;
				}
			//	count++;
				
			/*	for(int g=0;g<l;g++)
				{
					cout<<stack[g];
					
				}*/
				int j1=0;
				
				while(j!=l)
				{
	//			cout<<"hi";
				if(stack[j]=='-')
				{
				
					j1++;
		
				}
				//c++;
				j++;
				
			
			}
	///		cout<<count;
			if(j1==l)
			{
	//		break;
			for(int k=0;k<l;k++)
			{
			
			
		
				stack[k]='+';
				
		
		
		}
		count++;
	}
	
		
	//cout<<"hi";
	sum=0;
		for(int q=0;q<l;q++)
		{
			if(stack[q]=='+')
			{
			
			sum=sum +1;
			//cout<<"hi";
			//count++;
		}
		
		
		
		
		}
//		cout<<sum;
		//sum=l;
		
		

	
}
else if(stack[t]=='-')
{

count++;
break;
}
else
{
	count=0;
	break;
}
t++;
//sum=l;
}
	/*	cout<<sum<<endl;
	
	cout<<count;
	
	}
	}
	
	
	
	
	
	
	
	//cout<<count;
	*/ofstream out;
	out.open("output11.txt",ios::app);
	out<<"Case"<<" "<<"#"<<i<<":"<<" "<<count<<endl;
	out.close();
	cout<<"Case"<<" "<<"#"<<i<<":"<<" "<<count<<endl;
}
in.close();
	return 0;
}
