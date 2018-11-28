#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

ifstream in ("Osmos.in");
ofstream out ("Osmos.out");

vector<int> motes;

int getMToAdd(int &curSz, int toReach)
{
	if(curSz>toReach)return 0;
	int res=0;
	while(curSz<=toReach)
	{
		curSz+=curSz-1;
		res++;
	}
	return res;
}

int main()
{
	int nCases;
	in >> nCases;
	for(int cs = 1; cs <= nCases; cs++)
	{
		int mSz,N;
		in >> mSz >> N;
		motes.resize(N);
		for(int i = 0; i < N; i++)
			in >> motes[i];
		int sol=0;
		int i = 0;
		if(mSz==1)
		{
		    i=N;
		    sol=N;
		}
		sort(motes.begin(),motes.end());
		while(i<N)
		{
			while(motes[i]<mSz&&i<N)
				mSz+=motes[i++];
            if(i==N)break;
			int cSz = mSz;
			int nToAdd=getMToAdd(cSz,motes[i]);
			if(nToAdd>N-i)
			{
				sol+=N-i;
				break;
			}
			else
			{
				sol+=nToAdd;
				mSz = cSz;
			}
		}
		out << "Case #" << cs << ": " << sol << '\n';
	}
}
