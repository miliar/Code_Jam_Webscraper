//
//  main.cpp
//  Problem D. Deceitful War
//
//  Created by keta on 2014/04/12.
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


int War( vector<double> Naomi, vector<double> Ken )
{
	int win = 0;
	
	sort( Ken.begin(), Ken.end() );
	
	for( auto n : Naomi )
	{
//		cout << "Naomi took " << n << endl;
		
		double chosen_ken = -1;
		for( auto k : Ken )
		{
			if( k > n )
			{
				chosen_ken = k;
				break;
			}
		}
		
		if( chosen_ken < 0 )
			chosen_ken = Ken[0];
		
//		cout << "Ken took " << chosen_ken << endl;
		
		Ken.erase( remove( Ken.begin(), Ken.end(), chosen_ken ), Ken.end() );
		
		if( n > chosen_ken )
			win++;
	}
	
	return win;
}

int DeceitfulWar( vector<double> Naomi, vector<double> Ken )
{
	int win = 0;
	
	sort( Ken.begin(), Ken.end() );
	sort( Naomi.begin(), Naomi.end() );
	
	while( Naomi.size() != 0 )
	{
		double min_naomi = *min_element( Naomi.begin(), Naomi.end() );
		double min_ken = *min_element( Ken.begin(), Ken.end() );
		
		if( min_naomi < min_ken )
		{
			double chosen_naomi = *min_element( Naomi.begin(), Naomi.end() );
			double chosen_ken = *max_element( Ken.begin(), Ken.end() );
			
			Naomi.erase( remove( Naomi.begin(), Naomi.end(), chosen_naomi ), Naomi.end() );
			Ken.erase( remove( Ken.begin(), Ken.end(), chosen_ken ), Ken.end() );
		}
		else
		{
			double chosen_naomi = *min_element( Naomi.begin(), Naomi.end() );
			double chosen_ken = *min_element( Ken.begin(), Ken.end() );
			
			Naomi.erase( remove( Naomi.begin(), Naomi.end(), chosen_naomi ), Naomi.end() );
			Ken.erase( remove( Ken.begin(), Ken.end(), chosen_ken ), Ken.end() );
			
			win++;
		}
	}
	
	return win;
}

int main()
{
	int T;
	
	cin >> T;
	for( int t = 0; t < T; t++ )
	{
		int N;
		cin >> N;
		
		vector<double> Naomi(N);
		vector<double> Ken(N);
		
		for( int n = 0; n < N; n++ )
			cin >> Naomi[n];
		
		for( int n = 0; n < N; n++ )
			cin >> Ken[n];
		
		int war = War( Naomi, Ken );
		int deceitful = DeceitfulWar( Naomi, Ken );
		
		cout << "Case #" << t + 1 << ": " << deceitful << " " << war << endl;
	}
	
	
	return 0;
}