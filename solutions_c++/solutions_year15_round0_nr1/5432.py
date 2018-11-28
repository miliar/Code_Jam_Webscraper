#include <stdio.h>
#include <string>
#include <iostream>
#include <fstream>
using namespace std;
int main()
{
	int i,j,num,t,len,k,smax,no_of_ppl,ans,case_no;
	string s;
	case_no=1;
	ifstream inf("A-large.in");
	inf >> t;
	ofstream outf("standing_ovation.txt");
	while(t--)
	{
		inf >> smax;
		inf >> s;
		len = smax + 1;
		outf << "Case #" << case_no << ": ";
		ans=no_of_ppl=0;
		for(i=0;i<len;i++)
		{	
			num = (int)s[i] - (int)'0';
			if(num>0 && i>no_of_ppl)
			{
				ans += (i-no_of_ppl);
				no_of_ppl += (i-no_of_ppl);
			}
			no_of_ppl += num;
		}
		outf << ans <<"\n";
		case_no++;	
	}
	outf.close();
	inf.close();
	return 0;
}