#include <iostream>
#include <string>
using namespace std;

int main() {
	string s,s1;
	char temp,a,b;
	int t,T,len,i,j;
	cin>>T;
	for(t=1;t<=T;t++)
	{
		cin>>s;
		s1=s;
		len=s.length();
		a=s[0];
		s1[0]=a;
		for(i=1;i<len;i++)
		{
			if(s[i]>=s1[0])
			{
				temp=s1[0];
				s1[0]=s[i];
				for(j=s1.length();j>1;j--)
					s1[j]=s1[j-1];
				s1[1]=temp;
			}
			else
				s1[i]=s[i];
		}
		cout<<"Case #"<<t<<": "<<s1<<endl;
	}
	return 0;
}