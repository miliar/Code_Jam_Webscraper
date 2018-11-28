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


struct node
{
	int x;
	int y;
	int jump;
	string route;
};


int main2( int c, char *v[] )
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
		int X;
		int Y;
		
		in >> X;
		in >> Y;
		
		int dx[] = {1, 0, -1, 0};
		int dy[] = {0, 1, 0, -1};
		char r[] = { 'E', 'N', 'W', 'S' };
		
		
		node n;
		n.x = 0;
		n.y = 0;
		n.jump = 1;
		
		queue<node> q;
		q.push(n);
		
		string ans;
		
		while( !q.empty() )
		{
			n = q.front();
			q.pop();
			
			if( n.x == X && n.y == Y )
			{
				ans = n.route;
				break;
			}
			
			for( int i = 0; i < 4; i++ )
			{
				node next = n;
				next.x += dx[i] * next.jump;
				next.y += dy[i] * next.jump;
				next.route += r[i];
				next.jump++;
				
				if( abs(next.x) <= 100 && abs(next.y) <= 100 )
					q.push(next);
			}
		}
		
		
		cout << "Case #" << t + 1 << ": " << ans << endl;
		
	}
	
	return EXIT_SUCCESS;
}

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
		int X;
		int Y;
		
		in >> X;
		in >> Y;
		
		string route;
		
		int x = 0;
		int y = 0;
		int jump = 1;
		
		while( x != X )
		{
			if( x < X )
			{
				if( x + jump <= X )
				{
					x += jump;
					jump++;
					route += 'E';
				}
				else
				{
					x -= jump;
					jump++;
					route += 'W';
				}
				
			}
			else
			{
				if( x - jump < X )
				{
					x += jump;
					jump++;
					route += 'E';
				}
				else
				{
					x -= jump;
					jump++;
					route += 'W';
				}
			}
		}

		while( y != Y )
		{
			if( y < Y )
			{
				if( y + jump <= Y )
				{
					y += jump;
					jump++;
					route += 'N';
				}
				else
				{
					y -= jump;
					jump++;
					route += 'S';
				}
				
			}
			else
			{
				if( y - jump < Y )
				{
					y += jump;
					jump++;
					route += 'N';
				}
				else
				{
					y -= jump;
					jump++;
					route += 'S';
				}
			}
		}
		
		
		cout << "Case #" << t + 1 << ": " << route << endl;
		
	}
	
	return EXIT_SUCCESS;
}