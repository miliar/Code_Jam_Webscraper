#include<iostream>
#include<fstream>
#include <vector>
#include <sstream>
#include <string>
using namespace std;

int main()
{
	vector<int>vc;
	int a;
	string s1;
	ofstream of;
	ifstream iff;
	iff.open("input.txt");
	of.open("output.txt");
	iff>>a;
	
	for(int i=0;i<a;i++)
	{
		int b;
		iff>>b;
		vc.push_back(b);
	}
	for(int i=0;i<a;i++)
	{
		
		if(vc[i]==0)
		{
			of<<"Case #"<<i+1<<": "<<"INSOMNIA"<<endl;
		}
		else
		{
			int zer=0,one=0,two=0,three=0,f=0,five=0,six=0,sev=0,eig=0,nine=0;
			int t=1;
			int count=2;
			int temp=vc[i];
			int number=vc[i];
			while(t!=0)
			{
				
				int rem;
				while(number>0)
				{
					rem = number % 10;
    				number = number / 10;
					if(rem==0)
					{
						zer=1;
					}
					else  if(rem==1)
					{
						one=1;
					}
					else  if(rem==2)
					{
						two=1;
					}
					else  if(rem==3)
					{
						three=1;
					}
					else  if(rem==4)
					{
						f=1;
					}
					else  if(rem==5)
					{
						five=1;
					}
					else  if(rem==6)
					{
						six=1;
					}
					else  if(rem==7)
					{
						sev=1;
					}
					else  if(rem==8)
					{
						eig=1;
					}
					else  if(rem==9)
					{
						nine=1;
					}
				
					}
					if(zer==1 && one==1 && two==1 && three==1 && f==1 &&five==1 && six==1  && sev==1 && eig==1 && nine==1)
					{
						of<<"Case #"<<i+1<<": "<<temp<<endl;
					t=0;
					}
					temp=vc[i]*count;
					number=temp;
					count++;
			}
		}
		}
		
	}
	
	
	
	
	

