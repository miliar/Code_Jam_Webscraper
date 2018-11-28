#include <iostream>
#include <fstream>
using namespace std;

int main()
{
	ofstream fout("A-small-attempt3.out");
    ifstream fin("A-small-attempt3.in");

	int t,count=0;
	fin>>t;
	while(count++<t)
	{
		int a,b;
		char op;
		fin >> a >> op >> b;

		if(a>b)
		{
			fout << "Case #"<<count<<": impossible" <<endl;
			continue;
		}
		else if (a == b)
		{
			fout << "Case #"<<count<<": 0" <<endl;
			continue;
		}

		bool flag = true;
		while(flag)
		{
			if(a==1)break;
			for(int i=2;i<=a;i++)
			{
				if(a%i==0&&b%i==0)
				{
					a/=i;
					b/=i;
					continue;
				}
				if(i==a)
					flag=false;
			}
		}

	

		//fout <<a <<"/"<<b<<endl;
		bool out = true;

		int k = b;
		while(k!=1)
		{
			if(k%2==1)
			{
				out = false;
				break;
			}
			k/=2;
		}

		int co = 0;
		while(out)
		{
			while(b!=1&&b%2==1)
			{
				out = false;
				break;
			}
			co++;
			b/=2;
			if(a>=b)
				break;
		}

		if(out)
			fout << "Case #"<<count<<": " << co << endl;
		else
			fout << "Case #"<<count<<": impossible" <<endl;
	}
}
