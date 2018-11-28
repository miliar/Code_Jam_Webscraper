#include <iostream>
#include <fstream>
using namespace std;
//#define TEST

int BreakTo(int N, int K)
//Given a plate with N pancakes, return the least operation times if 
// we want to let it be a lot of plates with no more than K pancakes.
{
	if(N<=K) return 0;
	else if(N%K==0) return N/K-1;
	else return N/K;
}

int main(int argc, char **argv)
{
#ifndef TEST 
	ifstream inf("in.txt",ios_base::in);
	ofstream ouf("out.txt",ios_base::out);
#endif
	
	int T;
#ifndef TEST
	inf>>T;
#else
	cin>>T;
#endif
	for(int x=1;x<=T;++x)
	{
		int D;
		int *P;
#ifndef TEST
		inf>>D;
#else
	    cin>>D;
#endif
		P = new int[D];
		for(int i=0;i<D;++i) 
#ifndef TEST 
			inf>>P[i];
#else
			cin>>P[i];
#endif
		
		//find the max P[i]
		int maxP = -1;
		for(int i=0;i<D;++i)
			if(P[i]>maxP) maxP = P[i];
		//try all the K, from maxP to 1
		int miny=-1;
		for(int K=maxP;K>0;--K)
		{
			int sum = K;
			for(int i=0;i<D;++i)
			{
				sum += BreakTo(P[i],K);
			}
#ifdef TEST
			cout<<K<<" sum: "<<sum<<endl;
#endif
			if(miny==-1 || sum<miny) 
				miny = sum;
		}
#ifndef TEST
		ouf<<"Case #"<<x<<": "<<miny<<endl;
#else
		cout<<"Case #"<<x<<": "<<miny<<endl;
#endif
		
		delete []P;
	}
#ifndef TEST
	ouf.close();
	inf.close();
#endif
	return 0;
}