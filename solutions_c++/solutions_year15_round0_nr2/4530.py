#include <stdio.h>
#include <vector>
#include <algorithm>
#include <string>
#include <limits.h>
#include <math.h>
#include <iostream>
#include <fstream>
using namespace std;
int main()
{
	int t,i,x,d,temp,divide,sum,case_no,num,ans;
	case_no=1;
	ifstream inf("B-small-attempt7.in");
	inf >> t;
	ofstream outf("pancake_output.txt");
	while(t--)
	{
		outf << "Case #" << case_no << ": ";
		vector<int> ar;
		inf >> d;
		sum=0;
		for(i=0;i<d;i++)
		{
			inf >> num;
			sum += num;
			ar.push_back(num);
		}
		sort(ar.begin(),ar.end());
		ans = ar[d-1];
		
		divide=1;
		while(divide<=sum)
		{
			printf("ans= %d\n",ans);
			temp=0;
			for(i=0;i<d;i++)
			{
				temp += (( ceil((double)ar[i]/(double)divide) -1 ) );
			}
			temp += (divide);
			if(temp<ans)
				ans=temp;
			divide++;
		}
		
		outf << ans << "\n";
		case_no++;
	}
	outf.close();
	inf.close();
	return 0;
}
