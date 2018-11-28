#include <iostream>
#include <fstream>
#include<bits/stdc++.h>
using namespace std;

#define ll long long int

int main()
{

	ifstream myfile("input2l.in");
	ofstream outfile("output2l.txt");
	ll t,n,i,tno=1,chk,count;
	
	
	myfile>>t;
	//cin>>t;
	

	while(t--)
	{
			chk=0;
			count=0;
			string s;
			
			myfile>>s;
			//cin>>s;
			for(i=s.length()-1;i>=0;i--)
			{	
				if(s[i]=='+'&&chk==0)
				continue;
				
				
				if(s[i]=='-'&&chk==0)
				{
					count++;
					chk=1;
				}
				
				if(s[i]=='-'&&chk==1)
				continue;
				
				if(s[i]=='+'&&chk==1)
				{
					count++;
					chk=0;
				}
			}
			
			outfile<<"Case #"<<tno<<":"<<" "<<count<<endl;
			//cout<<"Case #"<<tno<<":"<<" "<<count<<endl;
			tno++;		
	 }
				

	return 0;

}
