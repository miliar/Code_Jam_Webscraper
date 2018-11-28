#include <iostream>
#include <vector>
#include <algorithm>
#include <string.h>
#include <stdio.h>
#include <cmath>
#include <math.h>
#include <sstream>
#include <iomanip>
#include <time.h>
#include <fstream>

using namespace std;



int main()
{

	
	int cases;
	cin>>cases;
	vector<int> inpData,outData;

	for(int i=0;i<cases;i++)
	{
		int x;
		cin>>x;
		inpData.push_back(x);
	}
	for(int caseNo=0;caseNo<cases;caseNo++)
	{
		int N,N0;
		N0=inpData[caseNo];
		if (N0==0)
		{
			outData.push_back(-1);
			continue;
		}
		int a[10];
		for (int i=0;i<10;i++) a[i]=0;
		int iter=0;
		while(true)
		{
			iter++;
			N=iter*N0;
			while(N!=0)
			{
				a[N%10]=1;
				N/=10;
			}
			bool complete=true;
			for(int i=0;i<10;i++)
			{
				if (a[i]==0) complete=false;
			}
			if(complete) 
			{
				outData.push_back(iter*N0);
				break;
			}
		}
	}
	for(int caseNo=0;caseNo<cases;caseNo++)
	{
		if (outData[caseNo]==-1) cout<<"Case #"<<caseNo+1<<": INSOMNIA\n";
		else cout<<"Case #"<<caseNo+1<<": "<<outData[caseNo]<<"\n";

	}
	return 0;
}