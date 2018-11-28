#include <iostream>
#include <iomanip>

//#define _DEBUG_
//#ifdef _DEBUG_
//#endif

using namespace std;

int digits(int N)
{
   int set = 0;
   while(N)
   {
      int d = N%10;
      N/=10;
      set = set | (1<<d);
   }
   return set;
}

int main()
{
	int T;

	cin >> T;
	for(int t=1; t<=T; t++){
		/************************************
		*	Input Data
		*************************************/
		int set = 0b1111111111;
		int N;
		cin >> N;
		/************************************
		*	Solve the Problem
		*************************************/
		
		/************************************
		*	Output Results
		*************************************/
		int k;
		cout << "Case #" << t << ": ";
		
		if(N==0)
		   cout << "INSOMNIA" << endl;
		else
		{
		   for(k=1; set = set & ~digits(N*k); k++)
#ifdef _DEBUG_
                   cout << "set k N*k: " << setbase(16) << showbase << set << ' ' << setbase(10) << k << ' ' << N*k << endl;
#endif
		      ;
		   cout << N*k << endl;
		}
	}

	return 0;
}
