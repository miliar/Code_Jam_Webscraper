#include<iostream>
#include<fstream>
using namespace std;
int main()
{
		ofstream fout ("sub1.out");
    ifstream fin ("sub1.in");
		int tes;
		fin>>tes;
		for(int u=0;u<tes;u++)
		{
				int ms;
				fin>>ms;
				fin.ignore(5,' ');
				char str[ms+2];
				fin.getline(str,ms+2);
				int ct=0;
				int tc=0;
				for(int i=0;i<=ms;i++)
				{
						if(ct+tc<i)
						{
								cout<<i<<' '<<"needed\n";								
								tc+=((i-ct)-tc);
						}
						else
						{
								cout<<i<<' '<<"not needed\n";
						}						
						if(str[i]-48)
						{
								ct+=(str[i]-48);
								cout<<i<<' '<<"added\n";
						}
						cout<<"ct="<<ct<<"  tc="<<tc<<'\n';
				}
				cout<<tc<<endl;
				fout<<"Case #"<<u+1<<": "<<tc<<'\n';
		}
		return 0;
}
