#include <bits/stdc++.h>

using namespace std;

int main(int argc, char const *argv[])
{

	ofstream outfile;
	outfile.open("soln.out",ios::out);
	
	ifstream infile;
	infile.open("B-large.in",ios::in);
  	
  	int tt;
	infile >> tt;
		
	for (int i = 0; i < tt; ++i)
	{
		outfile << "Case #" << i+1 << ": ";
		string s;
		infile >> s;
		int n = s.length();
		int m2p = 0;
		int p2m = 0;
		for (int j = 0; j < n-1; ++j)
			{
				if(s[j]=='+' && s[j+1]=='-')
					p2m++;
				if(s[j]=='-' && s[j+1]=='+')
					m2p++;
			}
		int pad = 0;
		if(m2p==0 && s[0]=='-')
			pad=1;
		if(p2m==1 && m2p==0)
			pad=1;
		if(p2m+m2p>1 && s[n-1]=='-')
			pad=1;
		outfile << m2p+p2m+pad<< "\n";
	}
	
	return 0;
}
