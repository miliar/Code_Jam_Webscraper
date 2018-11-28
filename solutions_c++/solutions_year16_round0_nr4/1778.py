#include <iostream>
#include <iomanip>

//#define _DEBUG_
//#ifdef _DEBUG_
//#endif

using namespace std;

int main()
{
	int T;

	cin >> T;
	for(int t=1; t<=T; t++){
		/************************************
		*	Input Data
		*************************************/
		int K,C,S;
		cin >> K >> C >> S;
		/************************************
		*	Solve the Problem
		*************************************/
		
		/************************************
		*	Output Results
		*************************************/
		cout << "Case #" << t << ":";
		
		if( (C==1)&&(S<K) || (C>1)&&(S<K-1) )
		   cout << " IMPOSSIBLE" << endl;
		else
		{
		   if( (C==1) || (K==1) )
		      cout << ' ' << 1;
		   for(int i=2; i<=K; i++)
		      cout << ' ' << i;
		   cout << endl;
		}
	}

	return 0;
}
