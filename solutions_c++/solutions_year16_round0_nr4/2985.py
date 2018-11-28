#include<bits/stdc++.h>
using namespace std;
int main()
{
	fstream fin,fout;
	fin.open("D-small-attempt0.in",ios::in);
	fout.open("small1-out.txt",ios::out);
	
	int t,q;
	fin>>t;
	for(q=0;q<t;++q)
	{
		fout<<"Case #"<<q+1<<": ";
		
		int k,c,s;
		fin>>k>>c>>s;
		
		int i;
		
		if(s < k)
			fout<<"IMPOSSIBLE";
		
		else
			for(i=0;i<s;++i)
				fout<<(i+1)<<" ";
		
		fout<<"\n";
	}
	
	fout.close();
	fin.close();
	return 0;
}
