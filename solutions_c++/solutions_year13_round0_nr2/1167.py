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
#include <fstream>

// Thanks for http://d.hatena.ne.jp/EmK/20071015
#define foreach(i,v) \
for(bool i##_bool2=true;i##_bool2;i##_bool2=false)\
for(const __typeof(v)& i##_foreach_##i=v;i##_bool2;i##_bool2=false)\
for(__typeof((i##_foreach_##i).begin())i##_iter=(i##_foreach_##i).begin(),i##_end=(i##_foreach_##i).end();\
i##_iter!=i##_end;i##_iter++)\
for(bool i##_bool=true;i##_bool;\
i##_bool = (i##_bool?i##_end=i##_iter,advance(i##_end,1),false:false))\
for(const __typeof(*i##_iter)& i=*i##_iter ; i##_bool ; i##_bool=false)

using namespace std;
static const double EPS = 1e-5;
typedef long long ll;


int main( int c, char *v[] )
{
	string input;
	
	if( c == 1 )
		input = "sample.txt";
	else
		input = v[1];
	
	
	std::ifstream in( input.c_str() );
	std::ofstream out( (input + "_out.txt").c_str() );
	
	int T = 0;
	in >> T;
	
	int N, M;
	
	for( int t = 0; t < T; t++ )
	{
		in >> N;
		in >> M;
		
		vector< vector<int> > goal;
		vector< vector<int> > init;
		
		// initialize lawn
		for( int n = 0; n < N; n++ )
		{
			vector<int> v;
			
			for( int m = 0; m < M; m++ )
			{
				v.push_back(100);
			}
			
			init.push_back(v);
		}
		
		// read problem
		for( int n = 0; n < N; n++ )
		{
			vector<int> v;
			
			for( int m = 0; m < M; m++ )
			{
				int x;
				in >> x;
				v.push_back(x);
			}
			
			goal.push_back(v);
		}
		
		
		
		// simulation
		for( int n = 0; n < N; n++ )
		{
			vector<int> g = goal[n];
			int max = *max_element( g.begin(), g.end() );

			for( int m = 0; m < M; m++ )
				init[n][m] = min( init[n][m], max );
		}
				
		for( int m = 0; m < M; m++ )
		{
			int max = 0;
			for( int n = 0; n < N; n++ )
				max = std::max( max, goal[n][m] );
			
			for( int n = 0; n < N; n++ )
				init[n][m] = min( init[n][m], max );
		}
		
		
		if( init == goal )
			out << "Case #" << t + 1 << ": " << "YES" << endl;
		else
			out << "Case #" << t + 1 << ": " << "NO" << endl;

	}
	
	
	
	return EXIT_SUCCESS;
}