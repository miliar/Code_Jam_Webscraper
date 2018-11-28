#include <iostream>
#include <stdio.h>
#include <cmath>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include<string>
#include <fstream>
#include<iomanip>
#include<cstring>
using namespace std;
#define rep(i, x, y) for(int i = x; i < y; i++)
#define Rep(i, x, y) for(int i = x; i <= y; i++)
#define vi vector<int>
#define vvi vector<vector<int> >
#define pp push_back
typedef unsigned long long ull;

int main()
{
	//freopen( "input.in", "r", stdin );
	//freopen( "output.out", "w", stdout );
	int t;
	double C, F, X;
	scanf( "%d", &t );
	rep( i,1,t+1 )
	{
		cin>>C>>F>>X;
		double total = 0, count = 2;
		double farms, notf;
		farms = ( C / 2 );
		notf = X / count;
		count += F;
		farms += X / count;
		while( farms < notf )
		{
			total += farms - ( X/count );
			farms = ( C / count );
			notf = X / count;
			count += F;
			farms += X / count;
		}
		total += notf;
		cout<<"Case #"<<i<<": "<<setprecision(7)<<fixed<<total<<endl;
	}
}