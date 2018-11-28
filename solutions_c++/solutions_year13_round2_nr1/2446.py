// tictac.cpp : Defines the entry point for the console application.
//


#include <fstream>
#include <sstream>
#include <iostream>
#include <string>
#include <ctime>
#include <math.h>
#include <vector>
#include <list>
#include <algorithm>

using namespace std;

typedef unsigned long long int INT;

//#define OF oF
#define OF cout

std::ofstream oF;
std::ifstream iF;


typedef unsigned long long int UINT;

void process(int i);


int main(int argc, char * argv[])
{

	iF.open("D:\\2a_1_small_in.txt",ios::in);
	oF.open("D:\\2a_1_small_out.txt",ios::out);

	int cases=0;
	iF>>cases;

	OF<<"Starting..."<<cases<<"\n";
	clock_t t=clock();

	for(int i=0;i<cases;)
	{
		process(++i);
	}

	iF.close();
	clock_t t2 = clock();
	cout<<"time taken = "<<(t2-t)/18.2<<"\n";
	oF.close();
	cout<<"time taken = "<<(t2-t)/18.2<<"\n";

	return 0;
}



bool printFunc(UINT i) { OF<<i<<" "; return true;}
bool compareFunc (UINT i,UINT j) { return (i<j); }

void process(int CASE){

	oF<<"Case #"<<CASE<<": ";
	cout<<"Case #"<<CASE<<": ";

	int A,N;

	iF>>A>>N;
	vector<UINT> v;
	v.resize(N);
	long int n;
	for(n=0;n<N;n++)
	{
		iF>>v[n];
	}

	OF<<"Test case details: A = "<<A<<":N="<<N<<"\n";
	std::sort (v.begin(), v.end(), compareFunc);
	std::for_each(v.begin(),v.end(),printFunc);
	OF<<"\n";
	UINT sum=A,cn;
	int deltas=0;

	if(A==1)
	{
		OF<<"Deleting ALL"<<N<<"\n";
		deltas+=N;
		goto done;
	}



	for(n=0;n<N;n++)
	{
		cn = v[n];
		if(sum > cn)
		{
			sum+=cn;
			continue;
		}

		if(n==N-1)
		{
			deltas++;
			OF<<"Delete this last entry!"<<cn<<"\n";
			break;
		}


		if(cn==1 )
		{
			deltas++;
			OF<<"Can not delete small numbers..skipping "<<cn<<"\n";
			continue;
		}

	UINT p2= 1;	
	for(int t=1;t<N-n;t++)
		p2*=2;
	UINT fac = (N-n)^2;
	UINT SUM = p2 * sum -  p2 + 1;

	//sum + (sum-1) + (2*sum-2)
	if(SUM <=cn)
	{
		OF<<"Deleting ALL remaining..."<<(N-n)<<"\n";
		deltas+=(N-n);
		goto done;
	}


		OF<<"adding multiple huge entries..\n";
		while(sum<=cn)		// if sum-1 can not bridge the gap??
		{
			deltas++;
			OF<<"Adding a big number.. sum-1="<<(sum-1)<<"\n";
			sum+=sum-1;
		}
		sum+=cn;
	}

	OF<<"----\n";
done:;

	oF<< deltas<<"\n";
	oF.flush();

}

