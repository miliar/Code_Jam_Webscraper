#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <set>
#include <map>
#include <vector>
#include <string>
#include <iterator>
#include <algorithm>

using namespace std;

void readMatrix(vector< vector<int> >& v)
{
	for (int i=0; i<4; ++i)
	{
		for (int j=0; j<4; ++j)
		{
			cin>>v[i][j];
		}
	}
}


int main()
{
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);
	vector< vector<int> > v( 4, vector<int>(4, 0) );
	int t;
	int icase = 1;
	cin>>t;
	while ( t-- )
	{
		int ans;
		cin>>ans;
		readMatrix( v );
		vector<int> v1 = v[ans-1];
		cin>>ans;
		readMatrix( v );
		vector<int> v2 = v[ans-1];
		vector<int> res;
		sort( v1.begin(), v1.end() );
		sort( v2.begin(), v2.end() );
		set_intersection(v1.begin(), v1.end(), v2.begin(), v2.end(), 
			back_insert_iterator< vector<int> >(res));
		printf("Case #%d: ", icase++ );
		if ( res.size() == 1 )
		{
			printf("%d\n", res[0]);
		}
		else if( res.empty() )
		{
			printf("Volunteer cheated!\n");
		}
		else
			printf("Bad magician!\n");
	}
	return 0;
}