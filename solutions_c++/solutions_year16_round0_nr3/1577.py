#include <iostream>
#include <iomanip>

//#define _DEBUG_
//#ifdef _DEBUG_
//#endif

using namespace std;

const int _MAXLEN_ = 32;

void convert2bin(int k, char *S, int l)
{
   while(k)
   {
      char c = '0'+(k&1); 
      S[l++] = c;
      S[l++] = c;
#ifdef _DEBUG_
      cout << "convert2bin: k c " << k << ' ' << c << endl;
#endif
      k = k>>1;
   }
}

int main()
{
	int T;

	cin >> T;
	for(int t=1; t<=T; t++){
		/************************************
		*	Input Data
		*************************************/
		int N,J;
		char S[_MAXLEN_+1];
		int D[11] = {0,0,3,4,5,6,7,8,9,10,11}; // D[i] - число 11 в системе счисления с основанием i
		
		cin >> N >> J;
		S[0] = S[N-1] = '1';
		S[N] = '\0';
		for(int i=1; i<N-1; i++)
		   S[i] = '0';
		/************************************
		*	Solve the Problem
		*************************************/
		/************************************
		*	Output Results
		*************************************/
		cout << "Case #" << t << ":" << endl;

		for(int k=0; k<J; k++)
		{
		   convert2bin(k,S,1);
		   cout << S;
		   for(int i=2; i<=10; i++)
		      cout << ' ' << D[i];
		   cout << endl;
		}
	}

	return 0;
}
