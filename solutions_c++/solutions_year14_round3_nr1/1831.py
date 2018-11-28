#include<iostream>
#include<fstream>
#include<vector>
#include<map>
#include<string>
#include<cmath>
#include<algorithm>

int main()
{
	std::ifstream in;
	std::ofstream out;
	in.open("A-small-attempt1.in");
	out.open("A-small-attempt1.out");
	int T, count=0, p, q, res, tmp3, tmp4; double tmp1, tmp2;
	char ch;
	in>>T;
	while(T--)
	{
		count++;
		in>>p;
		in>>ch;
		in>>q;
		tmp1 = log((double)q)/log((double)2);
		tmp2 = log((double)p)/log((double)2);
		tmp3 = tmp1;
		tmp4 = tmp2; 
		if(tmp1-tmp3 > 0.0)
		{
			out<<"Case #"<<count<<": impossible"<<"\n";
			continue;
		}
		else if(p == 1)
		{
			res = tmp1;
		}
		else
		{
			res = ceil(tmp1 - tmp2);
		}

		

		out<<"Case #"<<count<<": "<<res<<"\n";
	}
	return 0;
}