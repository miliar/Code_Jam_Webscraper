// tictac.cpp : Defines the entry point for the console application.
//


#include <fstream>
#include <sstream>
#include <iostream>
#include <string>
#include <ctime>
#include <math.h>

using namespace std;

#define XDBG 0
#if XDBG
#define DBG std::cout
#else
#define DBG if(0) cout 
#endif

std::ofstream oF;
std::ifstream iF;



void process(int i);
int is_possible_sq(int n);

int main(int argc, char * argv[])
{
	iF.open("D:\\palin_in.dat",ios::in);
	oF.open("D:\\palin_out.txt",ios::out);

	int cases=0;
	iF>>cases;

	DBG<<"Starting..."<<cases<<"\n";
	clock_t t=clock();

	for(int i=0;i<cases;)
	{
		process(++i);
	}

	iF.close();
	oF.close();
	clock_t t2 = clock();
	DBG<<"time taken = "<<(t2-t)/18.2<<"\n";

	return 0;
}


typedef int INT ;

INT N, MAX_IN, MIN_IN;

int NIB(INT& n)
{

	return (n%10);
}

void INCR(INT& n)
{
	n++;
}

bool INCR_TO_NEXT_POSSIBLE(INT& n)
{
	while(n<MAX_IN){
		n++;
		int nib = NIB(n);
		if(is_possible_sq(nib)){
	//		cout<<"Moving to nexts candidate: "<<n<<"\n";
			return true;
		}
	}
		cout<<"Moving to nexts candidate failed. Hit : "<<MAX_IN<<"\n";
	return false;
}

bool GE(INT n, INT max)
{
	return (n>=max);
}

bool LESS()
{
	INCR(N);
	if(GE(N,MAX_IN))
		return true;
	return false;
}

int is_possible_sq(int n)
{
	switch(n)
	{
	case 0:
	case 1:
	case 4:
	case 5:
	case 6:
	case 9:
		return 1;
	}
	return 0;

}

bool is_square(INT& n, INT & root)
{
	int nib = NIB(n);
	if(is_possible_sq(nib)){
		int s = (int)sqrt(n);
		if(s*s == n)
		{
			root = s;
			return true;
		}
	}
	return false;
}

bool is_palin(INT& n)
{
	if(n<10)
		return true;
	stringstream s;
	s<<n;
	string S=s.str();
	int l = S.length();
	for(int i=0;i<l/2;i++)
	{
		if(S.at(i) != S.at(l-i-1)){

//			cout<<"NOT PAL.. char mismatch: "<<i<<"\n";
			return false;
		}
	}
	return true;
}


void process(int CASE){
int cand=0;
	oF<<"Case #"<<CASE<<":";
	iF>>MIN_IN>>MAX_IN;
	DBG<<"Case: "<<CASE<<":"<<MIN_IN<<":"<<MAX_IN<<"\n";

	bool done = false;

	INT N = MIN_IN;
	INT NN;
	bool is_pal;
	bool is_sq;
	while (!done)
	{

		is_sq = is_square(N,NN);
		if(is_sq){
			is_pal = is_palin(N);
			if(is_pal && is_palin(NN))
			{
				cout<<"YES! "<<N<<" == "<<NN<<"\n";
				cand++;
			}
		}
		done = (INCR_TO_NEXT_POSSIBLE(N) == false);
	}

		oF<<" " <<cand<<"\n";
#ifdef DBG
	oF.flush();
#endif
}

