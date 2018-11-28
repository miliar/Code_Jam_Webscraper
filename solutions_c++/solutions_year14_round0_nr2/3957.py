//
//  main.cpp
//  Problem B. Cookie Clicker Alpha
//
//  Created by keta on 2014/04/11.
//  Copyright (c) 2014年 Keisuke Ueda. All rights reserved.
//

#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <memory>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <sstream>
#include <complex>
#include <stack>
#include <queue>
#include <numeric>
#include <random>


using namespace std;





double small( const double C, const double F, const double X )
{
	int max_num_of_buying = X;
	int num_of_buying = 0;
	
	double gain = 2;
	
	double best = X / 2;
	
	// simulation
	while( num_of_buying <= max_num_of_buying )
	{
		int times_to_buy = num_of_buying;
		double sec = 0;
		gain = 2;
		
		while( times_to_buy-- )
		{
			sec += C / gain;
			gain += F;
		}
		
		sec += X / gain;

		
		best = min(best, sec);
		if( sec != best )
			break;
		num_of_buying++;
	}
	
	return best;
}

int main()
{
	int T;
	double C, F, X;
	
	cin >> T;
	for( int t = 0; t < T; t++ )
	{
		cin >> C >> F >> X;
		printf( "Case #%d: %.7lf\n", t + 1, small( C, F, X ) );
	}
	
	
	return 0;
}





int main11()
{
	printf( "Case #%d: %.7lf\n", 1, small( 1.02238, 3.07174, 1999.44708 ) );
	
	return 0;
}



int main6()
{
	for( int i = 0; i < 100; i++ )
	{
		// random generator
		mt19937 rng{ random_device()() };
		uniform_int_distribution<double> C( 1, 10000 );
		uniform_int_distribution<double> F( 1, 100 );
		uniform_int_distribution<double> X( 1, 100000 );
		
		double c = C(rng);
		double f = F(rng);
		double x = X(rng);
		
		printf( "Case #%d: %.7lf\n", 1, small( c, f, x ) );
		
	}
	
	
	return 0;
}

int main7(int argc, const char * argv[])
{
	double best = 99999999999999.9;
	
	const double C = 500.0;
	const double F = 4.0;
	const double X = 2000.0;
	
	struct node
	{
		double gain;
		double sec;
		double cookies;
	};
	
	node n;
	n.gain = 2;
	n.cookies = 0;
	n.sec = 0;
	
	queue<node> q;
	q.push(n);
	
	while(!q.empty())
	{
		n = q.front();
		q.pop();
		
		double next_buying_chance = std::max(( C - n.cookies ), 0.0) / n.gain;
		double time_remaining_to_be_finished = (X - n.cookies) / n.gain;
		
		cout << "debug : cookies = " << n.cookies << endl;
		
		if( n.cookies > X )
		{
			if( n.sec < best )
				best = n.sec;
			
			cout << "Debug info, the best time = " << best << endl;
			
			continue;
		}
		
		if( time_remaining_to_be_finished < next_buying_chance )
		{
			if( n.sec + time_remaining_to_be_finished < best )
				best = n.sec + time_remaining_to_be_finished;
			
			continue;
		}
		
		// buy
		node next;
		next.gain = n.gain + F;
		next.sec = n.sec + next_buying_chance;
		next.cookies = n.cookies + next_buying_chance * n.gain - C;
		q.push(next);
		
		// not buy
		next.gain = n.gain;
		next.sec = n.sec + next_buying_chance;
		next.cookies = n.cookies + next_buying_chance * n.gain;
		q.push(next);
		
	}
	
    return 0;
}

