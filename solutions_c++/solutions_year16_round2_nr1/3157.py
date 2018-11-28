#include<bits/stdc++.h>
using namespace std;

int main()
{
	freopen("asdl.in","r",stdin);
	freopen("asdout.txt","w",stdout);
	int t,k=1,i=0,r[2000];
	string s;
	cin>>t;
	while(k<=t)
	{
	for(int j=0;j<2000;j++)
	r[j]=-1;
		cin>>s;
		while(s.size()!=0)
		{
		//	cout<<"Helo";
			if(s.find("Z")!=string::npos)
			{
		//		cout<<"helo2";
				r[i]=0;
				i++;
				s.erase(s.begin()+s.find("Z"));
				s.erase(s.begin()+s.find("E"));
				s.erase(s.begin()+s.find("R"));
				s.erase(s.begin()+s.find("O"));
		//		cout<<"helo3";
				
			}
			
			else if(s.find("U")!=string::npos)
			{
				r[i]=4;
				i++;
				s.erase(s.begin()+s.find("F"));
				s.erase(s.begin()+s.find("O"));
				s.erase(s.begin()+s.find("U"));
				s.erase(s.begin()+s.find("R"));
			}
			else if(s.find("W")!=string::npos)
			{
				r[i]=2;
				i++;
				s.erase(s.begin()+s.find("T"));
				s.erase(s.begin()+s.find("W"));
				s.erase(s.begin()+s.find("O"));
			}
			else if(s.find("X")!=string::npos)
			{
				r[i]=6;
				i++;
				s.erase(s.begin()+s.find("S"));
				s.erase(s.begin()+s.find("I"));
				s.erase(s.begin()+s.find("X"));
			}
			else if(s.find("G")!=string::npos)
			{
				r[i]=8;
				i++;
				s.erase(s.begin()+s.find("E"));
				s.erase(s.begin()+s.find("I"));
				s.erase(s.begin()+s.find("G"));
				s.erase(s.begin()+s.find("H"));
				s.erase(s.begin()+s.find("T"));
			}
			else if(s.find("S")!=string::npos)
			{
				r[i]=7;
				i++;
				s.erase(s.begin()+s.find("S"));
				s.erase(s.begin()+s.find("E"));
				s.erase(s.begin()+s.find("V"));
				s.erase(s.begin()+s.find("E"));
				s.erase(s.begin()+s.find("N"));
			}
			else if(s.find("V")!=string::npos)
			{
				r[i]=5;
				i++;
				s.erase(s.begin()+s.find("F"));
				s.erase(s.begin()+s.find("I"));
				s.erase(s.begin()+s.find("V"));
				s.erase(s.begin()+s.find("E"));
			}
			else if(s.find("O")!=string::npos)
			{
				r[i]=1;
				i++;
				s.erase(s.begin()+s.find("O"));
				s.erase(s.begin()+s.find("N"));
				s.erase(s.begin()+s.find("E"));
			}
			else if(s.find("R")!=string::npos)
			{
				r[i]=3;
				i++;
				s.erase(s.begin()+s.find("T"));
				s.erase(s.begin()+s.find("H"));
				s.erase(s.begin()+s.find("R"));
				s.erase(s.begin()+s.find("E"));
				s.erase(s.begin()+s.find("E"));
			}
			else if(s.find("I")!=string::npos)
			{
				r[i]=9;
				i++;
				s.erase(s.begin()+s.find("N"));
				s.erase(s.begin()+s.find("I"));
				s.erase(s.begin()+s.find("N"));
				s.erase(s.begin()+s.find("E"));
			}
		}
		sort(r,r+2000);
		cout<<"Case #"<<k<<": ";
		for(i=0;i<2000;i++)
		{
			if(r[i]!=-1)
			cout<<r[i];
		}
		cout<<endl;
		i=0;
		k++;
	}
}
