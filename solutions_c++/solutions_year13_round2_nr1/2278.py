#include<iostream>
#include<fstream>
#include<sstream>
#include<stdlib.h>
#include<math.h>
#include<iomanip>
#include<algorithm> 
#include<string>
#include<vector>
using namespace std;
int main()
{
int inc=1;
	ifstream file("i1.in");
	ofstream file2("o1.txt",ios::trunc);
	string s1;
	getline(file,s1);
	int t=atoi(s1.c_str());
	
	long long a,s[102],temp;
	for(int x=1;x<=t;x++)
	{
		
		file2<<"Case #"<<inc++<<": ";
		getline(file,s1,' ');
		 a=atoi(s1.c_str());
		getline(file,s1);
		int n=atoi(s1.c_str());
		
		for(int z=1;z<n;z++)
		{
			getline(file,s1,' ');
		    s[z]=atoi(s1.c_str());
		    
		}
		
		if(n!=0)
		{
			getline(file,s1);
		    s[n]=atoi(s1.c_str());
		}
		
		for(int z=1;z<=n;z++)
		{
			for(int y=z+1;y<=n;y++)
			{
				if(s[z]>s[y])
				{
					temp=s[z];
					s[z]=s[y];
					s[y]=temp;
				}
			}
		}
		
		int i=1,c1=0,c2=0,c=0; 
		long long b;
		
		while(i<n||i==n)
		{
			while(s[i]<a&&(i<n||i==n))
			{
				a=a+s[i];
				i++;
				
			}
			
			int q=0;
			if(s[i]>a||s[i]==a)
			{
				q=1;
				c1=n-i+1;
				c2=0;
				
				while(s[i]>a||s[i]==a)
				{
					a=a+a-1;
					c2++;
					
					if(c2>c1||c2==c1)
					{
						
						c=c+c1;
						goto done;
					}
				}
				
				
			}
			
			if(q==1)
			c=c+c2;
		}
		
		done: ;
		
	    
	    
		file2<<c;
		
		
		file2<<endl;
	}
}
