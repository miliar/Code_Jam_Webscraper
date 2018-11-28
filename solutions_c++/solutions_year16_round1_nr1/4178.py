#include<iostream>
#include<string.h>
#include<vector>
#include<fstream>
#include<stdlib.h>
#define ll long long int
using namespace std;
int main()
{
	int t;
	string s;
	ofstream myfile;
	myfile.open ("example.txt");
	cin>>t;
	//vector<string>
	for(ll k=1;k<=t;k++)
	{
		char s1[1000]={'\0'};
		ll i;
		int flag=0;
		cin>>s;
		myfile<<"Case #"<<k<<": ";
		//cout<<s<<endl;
		for(i=0;i<s.length();i++)
		{
			if(flag==0)
			{
				s1[0]=s[0];
				//cout<<"INSIDE FLAG";

				flag=1;
			}
			else if(s[i]>=s1[0])
			{
				//cout<<"INSIDE ELSE IF"<<endl;
				for(ll j=0;j<=i;j++)
				{
					
					char temp;
					if(j==0)
					{
						temp=s1[0];
						s1[0]=s[i];
					}
					else
					{
						char temp1;
						temp1=s1[j];
						//cout<<temp1;
						s1[j]=temp;
						temp=temp1;
					}
					
				}
			}
			else
			{
				//cout<<"inside else"<<endl;
				s1[i]=s[i]; 
				//cout<<s1[i]<<endl;
			}
		}
		s1[s.length()]='\0';
		for(i=0;i<s.length();i++)
		{
			//cout<<s1[i];
			myfile<<s1[i];
		}
		//cout<<endl;
		myfile<<endl;
		
		
	}
	return 0;
}	
					
