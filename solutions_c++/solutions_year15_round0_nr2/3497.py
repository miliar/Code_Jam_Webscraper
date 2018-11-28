#include <stdio.h>
#include <vector>
#include <string>
#include <limits.h>
#include <math.h>
#include <iostream>
#include <fstream>
#include <algorithm>
using namespace std;
long long getAns(vector<long long>,long long,long long);
int main()
{
	long long test_case,i,d,sum,cn,no,ans;
	cn=1;
	ifstream inf("B-large.in");
	ofstream outf("finalop.txt");
	inf >> test_case;
	while(test_case--)
	{
		outf << "Case #" << cn << ": ";
		vector<long long> ar;
		inf >> d;
		sum=0;
		for(i=0;i<d;i++)
		{
			/*
				store sum 
				as we input
			*/
			inf >> no;
			sum += no;
			ar.push_back(no);
		}
		
		ans = getAns(ar,d,sum);
		outf << ans << "\n";
		cn++;
	}
	/*
		close the streams
	*/
	outf.close();
	inf.close();
	return 0;
}
long long getAns(vector<long long>ar,long long d,long long sum)
{
	sort(ar.begin(),ar.end());
	long long ans = ar[d-1];
	/*
		initial value is max element
	*/
	long long temp,i,equally=1;
	while(equally<=sum && equally<ans)
	{
		printf("ans= %lld\n",ans);
		temp=0;
		for(i=0;i<d;i++)
		{
			temp += (( ceil((double)ar[i]/(double)equally) -1 ) );
		}
		temp += equally;
		if(temp<ans)
			ans=temp;
		equally+=1;
	}
	return ans;
}
