#include<bits/stdc++.h>
using namespace std;
int main()
{
	fstream fin,fout;
	fin.open("large.txt",ios::in);
	fout.open("large-out.txt",ios::out);
	
	int t,q;
	fin>>t;
	for(q=0;q<t;++q)
	{
		fout<<"Case #"<<q+1<<": ";
		int lim,i;
		long count=0,sum=0;
		char C;
		fin>>lim;
		for(i=0;i<=lim;++i)
		{
			fin>>C;
			if(sum < i)
			{
				count += i-sum; sum += i-sum;
			}
			sum += C-48;
		}
		fout<<count<<endl;
	}
	
	fout.close();
	fin.close();
	return 0;
}
