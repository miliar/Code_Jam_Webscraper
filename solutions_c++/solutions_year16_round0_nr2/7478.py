#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <cstring>
#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <map>
#include <set>
#include <sstream>
#include <numeric>
#include <bitset>
#define REP(i, a, b) for ( int i = int(a); i <= int(b); i++ )
#define PB push_back
#define MP make_pair
#define for_each(it, X) for (__typeof((X).begin()) it = (X).begin(); it != (X).end(); it++)
#define DFS_WHITE -1
#define DFS_BLACK 1
#define MAXN 1000
#define pi 3.141592653589793
#define ARRAY_SIZE(A) sizeof(A)/sizeof(A[0])
#define INF 1<<30
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef pair<int, int> ii;
void reverseAndUpdate(string &input,int index, int start)
{
	reverse(input.begin() + start,input.begin() + index);
	for(int i = start ;i<=index ;i++)
		if(input[i] == '-')
			input[i] = '+';
		else
			input[i] = '-';
	}
int main()
{
	int tc = 0;
	cin>>tc;
	for(int i =1 ; i<=tc; i++)
	{
		string input;
		cin>>input;
		int c = 0;
		for(int i = 0; i < input.size()-1 ; i++)
		{
			if(input[i] != input[i+1])
			{
				reverseAndUpdate(input,i,0);
				//cout<<input<<endl;
				c++;
			}
		}
		if(input[0] == '-')
		{
			//cout<<" "<<input<<endl;
			c++;
		}
		cout<<"Case #"<<i<<": "<<c<<endl;
	}
	return 0;
}