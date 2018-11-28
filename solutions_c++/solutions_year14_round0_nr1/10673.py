#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#define REP(i, n) for(int i=0;i<n;i++)
#define ll long long

int arr[4][4];
int brr[4][4];

int main()
{
	int t;
	cin>>t;
	int c=0;
	while( t-- )
	{
		c++;
		int a, b;
		cin>>a;a--;
		REP(i, 4)
			REP(j, 4)
				cin>>arr[i][j];
		cin>>b;b--;
		REP(i, 4)
			REP(j, 4)
				cin>>brr[i][j];
		int val=-1;
		REP(i, 16)
		{
			bool pos = false;
			REP(j, 4)
				if( arr[a][j] == i+1 )
					pos = true;
			if( !pos )
				continue;
			pos = false;
			REP(j, 4)
				if( brr[b][j] == i+1 )
					pos = true;
			if( !pos )
				continue;
			if( val == -1 )
				val = i+1;
			else
				val = 100;
		}
		cout<<"Case #"<<c<<": ";
		if( val == -1 )
			cout<<"Volunteer cheated!";
		else if( val > 50 )
			cout<<"Bad magician!";
		else
			cout<<val;
		cout<<endl;
	}
	return 0;
}
		
		


