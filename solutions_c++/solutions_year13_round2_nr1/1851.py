// roundb.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <algorithm>
#include <deque>
using namespace std;
deque<unsigned long> q;
unsigned long temp, minM = -1;
unsigned long long A,N,T;
void advance() {
	while ( !q.empty() ) {
		if ( A <= q.front() )
			break;
		A += q.front();
		q.pop_front();
	}
}

int _tmain(int argc, _TCHAR* argv[])
{
	cin >> T;
	for ( unsigned long i = 0; i < T; i++ )
	{
		cin >> A;
		cin >> N;
		for ( unsigned long j = 0; j < N; j++ ) {
			cin >> temp;
			q.push_back(temp);
		}
		sort ( q.begin(), q.end() );
		if ( A == 1 ) {
			cout << "Case #" << i+1 << ": " << q.size() << "\n";
			minM = -1;
			q.erase (q.begin(),q.end());
			continue;
		}
		unsigned long move = 0;
		while ( !q.empty() ) {
			advance();
			if ( minM == -1 || minM > move + q.size())
				minM = move + q.size();
			A += A;
			A--;
			move++;
		}
		if ( minM == -1 || minM > move + q.size())
			minM = move + q.size();
		cout << "Case #" << i+1 << ": " << minM << "\n";
		minM = -1;
	}
	return 0;
}

