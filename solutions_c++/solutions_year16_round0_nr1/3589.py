#include<bits/stdc++.h>
using namespace std;
int main()
{
	fstream fin,fout;
	fin.open("A-large.in",ios::in);
	fout.open("large-out.txt",ios::out);
	
	int t,q;
	fin>>t;
	for(q=0;q<t;++q)
	{
		long long n,u=0,u1=0;
		int arr[10] = {0},flag=0,i;
		
		fin>>n;
		fout<<"Case #"<<q+1<<": ";
		
		if(n == 0)
		{
			fout<<"INSOMNIA\n";
			continue;
		}
		
		while(u < LONG_LONG_MAX && flag == 0)
		{
			u += n;
			u1 = u;
			while(u)
			{
				arr[u%10]++;
				u /= 10;
			}
			
			flag = 1;
			for(i=0;i<10;++i)
			if(arr[i] == 0)
			{
				flag = 0;
				break;
			}
			u = u1;
		}
		
		if(flag == 1)
			fout<<u<<"\n";
		else
			fout<<"INSOMNIA\n";
	}
	
	fout.close();
	fin.close();
	return 0;
}
