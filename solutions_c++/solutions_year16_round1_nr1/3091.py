#include <cstdio>
#include <time.h>
#include <cstdlib>
#include <random>
#include <iostream>
#include <vector>
#include <deque>

using namespace std;


int main (void)
{


	int T;
	cin >> T;
	
	for ( int c = 0; c < T; c++ )
	{
		string S;
		cin >> S;
		deque<char> myS;
		
		myS.push_back(S[0]);
		char front = S[0];
		for ( int d = 1; d < S.length(); d++ )
		{
			if ( S[d] >= front ){ 
				front = S[d];
				myS.push_front(S[d]);
			}else {
				myS.push_back(S[d]);
			}
		}
		
		cout << "Case #" << (c+1) << ": ";
		while ( myS.size() != 0 )
		{
			cout << myS.front();
			myS.pop_front();
		}
		cout << endl;
		
	}
}