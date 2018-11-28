#include<iostream>
#include<cstdio>
#include<fstream>
#include<cstring>
using namespace std;

int main()
{
	int T,s_max,count1,ans1;
	string s;
	
	ifstream fin;
	fin.open("A-large.in",ios::in);

	ofstream fout;
	fout.open("codejamq1outlarge.txt",ios::out);
	
	//cin>>T;
	fin>>T;
	
	for(int j=1;j<=T;j++)
	{
		count1 = 0;
		ans1 = 0;
		
		fin >> s_max >> s;
		
		//cin>>s_max;
		//cin>>s;
		
		if(s_max==0)
		{
			//cout<<"Case #"<<j<<": "<<0<<endl;
			fout<<"Case #"<<j<<": "<<0<<endl;
		}
		else
		{
			count1 += s[0]-'0';
			//cout<<"\nCOUNT! is " <<count1<<endl;
			for(int i=1;s[i]!='\0';i++)
			{
				//cout<<" i is "<<i<<endl;
				if(i>count1 && (s[i]-'0')!=0)
				{
					//cout<<i<<" is less than "<<count1<<endl;
					ans1 += (i-count1);
					count1 += (i-count1);
					//cout<<" now ans1 is : "<<ans1<<endl;
				}
				count1 += (s[i]-'0');
			}
			
			//cout<<"Case #"<<j<<": "<<ans1<<endl;
			fout<<"Case #"<<j<<": "<<ans1<<endl;
		}
		
	}
	
	
	return 0;
}
