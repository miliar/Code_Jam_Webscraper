#include <iostream>
#include<string>
using namespace std;

int main() {
	int t,T,count,i,j,check;
	string s;
	cin>>T;
	for(t=1;t<=T;t++)
	{
		check=0;
		count=0;
		cin>>s;
		for(i=s.length()-1;i>=0;i--)
		{
			if(s[i]=='-')
			{	
				check=1;
				j=i;
				count++;
			}
			else check=0;
			while(check==1 && j>=0)
			{
				if(s[j]=='-')
					s[j]='+';
				else
					s[j]='-';
				j--;
			}
		}
		cout<<"Case #"<<t<<": "<< count<<endl;
	}
	return 0;
}