#include<iostream>
#include<fstream>
#include<string>
#include<algorithm>
#include<math.h>
using namespace std;

int main()
{
	fstream fin("a.in",ios::in);
	fstream fout("a.out",ios::out);
	int max_tc;
	fin>>max_tc;
	int tc = 1;
	while(tc<=max_tc)
	{
		int result1 = 0;
		int result2 = 0;
		int N = 0;
		int M[1001]={0};

		fin>>N;
		for (int i=0; i<N;i++)
			fin>>M[i];

		//method 1 
		for(int i=0;i<N-1;i++)
		{
			if (M[i+1]<M[i])
				result1+=max(0,(M[i]-M[i+1]));
		}
		//method 2
		int per_interval = 0;
		for(int i=0; i<N-1; i++)
		{
			int rate = M[i]-M[i+1];
			rate = max(0,rate);
			if(rate>per_interval)
				per_interval=rate;
		}

		for(int i=0; i<N-1; i++)
		{
			result2+=min(M[i],per_interval);
		}

		fout<<"Case #"<<tc<<": "<<result1<<" "<<result2<<endl;
		tc++;
	}
	return 0;
}