#include <bits/stdc++.h>
using namespace std;
int main()
{
	cout.tie(0);
    std::ios::sync_with_stdio(false);
    ifstream fin;
    fin.open("input.in",ios::in);
    ofstream fout;
    fout.open("output.txt",ios::out);
	int t,T;
	fin>>T;
	for(t=1;t<=T;t++)
	{
		string s;
		fin>>s;
		int last=s.size(),i,count=0,flag=0;
		char sign;
		do
		{
			sign=s[last-1];
			for(i=last-2;(i>=0 && flag==0);i--)
			{
				if(sign!=s[i])
				{
					count++;
					int j=0;
					while(j<=i)
					{
						if(s[j]=='+') {s[j]='-';}
						else {s[j]='+';}
						j++;
					}
				}
			}
			for(i=0;i<last;i++)
			{
				if(s[i]==sign) flag=1;
				else {flag=0;break;}
			}			
		}while(flag==0);
		if(s[0]=='-') count=count+1;
		fout<<"Case #"<<t<<": "<<count<<endl;
	}
}