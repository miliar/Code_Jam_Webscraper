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
		
	for( int t = 0; t < T; t++ )
	{
		int A, N;

		in >> A;
		in >> N;
		
		vector<int> others;
		
		for( int n = 0; n < N; n++ )
		{
			int temp;
			in >> temp;
			others.push_back(temp);
		}
		
		sort( others.begin(), others.end() );
		
		struct node
		{
			int A;
			int count;
			vector<int> others;
		};
		
		node n;
		n.A = A;
		n.count = 0;
		n.others = others;
		
		queue<node> q;
		q.push(n);
		
		while( !q.empty() )
		{
			n = q.front();
			q.pop();
			
			while( n.others.size() != 0 )
			{
				if( n.A <= n.others[0] )
					break;
				
				n.A += n.others[0];
				
				sort( n.others.begin(), n.others.end(), greater<int>() );
				n.others.pop_back();
				sort( n.others.begin(), n.others.end() );
			}
			
			if( n.others.size() == 0 )
				break;
			
			node next1 = n;
			node next2 = n;
			
			next1.A = next1.A * 2 - 1;
			next1.count++;
			
			next2.count++;
			next2.others.pop_back();
			
			q.push(next1);
			q.push(next2);
		}
		
		cout << "Case #" << t + 1 << ": " << n.count << endl;
		
	}
	
	return EXIT_SUCCESS;
}