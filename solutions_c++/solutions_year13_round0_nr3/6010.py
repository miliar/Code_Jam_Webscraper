#pragma comment(linker, "/STACK:16777216")
#pragma warning (disable : 4786)
#include <set>
#include <map>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <cctype>
#include <cstdio>
#include <string>
#include <vector>
#include <cassert>
#include <cstdlib>
#include <cstring>
#include <sstream>
#include <fstream>
#include <iostream>
#include <algorithm>
 
#define maxsize 100010  
   
using namespace std;
 
const double EPS = 1e-11;
const int INF = ( 1<<29 );
const double PI = 2 * acos( 0.0 );
 
int MAX( int a , int b ) { return a > b ? a : b;  }
int MIN( int a , int b ) { return a < b ? a : b;  }
void SWAP( int &a , int &b ) { int t = a; a = b; b = t; }
int GCD( int a , int b ) { while( b ) { b ^= a ^= b ^= a %= b; } return a; }

bool cmp(const int &a, const int &b)
{
    if(a<b) return true;
    else return false;
}

int arr[5]={1,4,9,121,484};

void result(int k);
 
 
int main()
{
	freopen ( "input.in", "r", stdin );
	freopen ( "output.out", "w", stdout );
	int test, k;
	scanf("%d", &test);
	for(k=1; k<=test; k++)
		result(k);
	//system("pause");
	return 0;
}
 
void result(int k)
{
	int a, b, ans=0, i;
	scanf("%d %d", &a, &b);
	for(i=0; i<5; i++)
		if(arr[i]>=a && arr[i]<=b)
			ans++;
	printf("Case #%d: %d\n", k, ans);
}