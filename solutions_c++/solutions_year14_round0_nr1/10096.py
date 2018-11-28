#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <algorithm>
#include <sstream>
#include <limits.h>
#include <iomanip>
#include <cstring>
#include <bitset>
#include <fstream>
#include <cmath>
#include <cassert>
#include <stdio.h>
#include <ctype.h>
using namespace std ;
#define all(v) v.begin(),v.end()
#define rep(i,n,m) for( int i = (int)(n), _m = (int)(m) ; i < _m ; ++i )
#define ull unsigned long long
int getCollision(vector<int> a, vector<int> b, int & lastFound)
{
	int c=0;
	lastFound = -1;
	rep(i,0,a.size())
		if(find(b.begin(), b.end(), a[i]) != b.end())
			c++, lastFound = a[i];
	return c;
}
int main()
{
	freopen("in.in","r",stdin);
	freopen("out.txt","w",stdout);
	int tc;
	int ans1, ans2;
	int finalAnswer;
	vector<vector<int> >	b1(4,vector<int>(4)),
							b2(4,vector<int>(4));

	cin>>tc;
	rep(tt,1,tc+1)
	{
		cin>>ans1;
		rep(i,0,4)rep(j,0,4)cin>>b1[i][j];
		cin>>ans2;
		rep(i,0,4)rep(j,0,4)cin>>b2[i][j];
		int col = getCollision(b1[ans1-1], b2[ans2-1], finalAnswer);
		
		cout<<"Case #"<<tt<<": ";
		
		if(col == 0) cout<<"Volunteer cheated!"<<endl;
		if(col == 1) cout<<finalAnswer<<endl;
		if(col >  1) cout<<"Bad magician!"<<endl;
	}
	return 0;
}