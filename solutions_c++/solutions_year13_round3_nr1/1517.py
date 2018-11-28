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


bool isVowel(char ch)
{
    if( ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch =='u')
		return true;
    else return false;
}


int count( const string &in )
{
	int max = 0;
	int count = 0;
	
	for( int i = 0; i < in.length(); i++ )
	{
		if( !isVowel(in[i]) )
		{
			count++;
		}
		else
		{
			max = std::max( count, max );
			count = 0;
		}
	}
	max = std::max( count, max );
	
	return max;
	
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
		string L;
		int N;
		
		in >> L;
		in >> N;
		
		int ans = 0;
		
		for( int n = N; n <= L.length(); n++ )
		{
			for( int i = 0; i < L.length() - n + 1; i++ )
			{
				string sub = L.substr( i, n );
//				cout << sub << " " << count(sub) << endl;
				if( count(sub) >= N )
					ans++;
			}
		}

		cout << "Case #" << t + 1 << ": " << ans << endl;
		
	}
	
	return EXIT_SUCCESS;
}