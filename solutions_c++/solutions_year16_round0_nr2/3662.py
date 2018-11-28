#include<bits/stdc++.h>
using namespace std;
int main()
{
	fstream fin,fout;
	fin.open("B-large.in",ios::in);
	fout.open("large-out.txt",ios::out);
	
	int t,q;
	fin>>t;
	for(q=0;q<t;++q)
	{
		fout<<"Case #"<<q+1<<": ";
		
		string str;
		fin>>str;
		int len = str.length(),i,count=0,rev=0;
		int arr[len];
		
		for(i=len-1;i>=0;--i)
		{
			if((str[i] == '-' && !rev) || (str[i] == '+' && rev))
			{
				rev = ~rev;
				count++;
			}
		}
		fout<<count<<"\n";
	}
	
	fout.close();
	fin.close();
	return 0;
}
