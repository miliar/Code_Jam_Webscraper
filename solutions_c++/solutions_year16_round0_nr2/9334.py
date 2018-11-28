#include <iostream>
#include <stack>
#include <cstring>
#include <cstdlib>
using namespace std;

int main() {
	
	char str[100];
	long int t,i,minusCount,flip=0;
	cin>>t;
	for(i=1;i<=t;i++)
	{
		cin>>str;
		long int len=strlen(str);
			//cout<<"len"<<len<<endl;
		if(len==1 && str[0]=='-')
			cout<<"Case #"<<i<<": "<<len<<endl;
		else if (len==1 && str[0]=='+')
			cout<<"Case #"<<i<<": "<<len-1<<endl;
		else{
			
			flip=0;	
			minusCount=0;
			
			for(int j=len-1;j>=0;j--)
			{
				//cout<<minusCount<<" j: "<<j<<endl;
				if(str[j]=='-')
				 {
				 	minusCount++; 
				 }
				else if(minusCount>0 && str[j]=='+')
				{	
						
					j=j+minusCount;
						//cout<<"plus"<<" j: "<<j<<endl;
					flip+=1;
						//cout<<str<<endl;
					for(int k=j;k>=0;k--)
					{
						if(str[k]=='-')
								{	str[k]='+';//cout<<str<<endl;
								}
							
						else if(str[k]=='+')
								{	str[k]='-'; //cout<<str<<endl;
								}
					}
					minusCount=0;
				}
				//cout<<"plus"<<" j: "<<j<<endl;
			}
			if(minusCount>0)
				flip+=1;
				
			cout<<"Case #"<<i<<": "<<flip<<endl;
		}
	}
	return 0;
}