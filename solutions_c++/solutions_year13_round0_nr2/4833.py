
//main includes
#include<iostream>
#include<cstdio>
#include<cstring>
#include<ctime>
#include<cmath>


//other includes
#include<algorithm>
#include<climits>
#include<vector>
#include<queue>
#include<stack>
#include<bitset>
#include<set>
#include<deque>
#include<cstdlib>
#include<map>
#include <utility>

#define re



using namespace std;

#define FOR(a,b)        for(__typeof(b) i=(a);i<(b);i++)

int t,m,n;
int **a;
int *row_max;
int *column_max;
void preprocess()
{
	cin>>n>>m;
	row_max = new int[n];
	column_max = new int[m];
		for(int i=0;i<n;i++)
			row_max[i] = INT_MIN;
		for(int j=0;j<m;j++)
			column_max[j] = INT_MIN;
	a = new int*[n];
	for(int i=0;i<n;i++)
		a[i] = new int[m];

	for(int i=0;i<n;i++)
		for(int j=0;j<m;j++)
		{
			cin>>a[i][j];

			if(a[i][j] > row_max[i])
				row_max[i] = a[i][j];
			if(a[i][j] > column_max[j])
				column_max[j] = a[i][j];


		}

}

bool solve()
{
	for(int i=0;i<n;i++)
	{
		for(int j=0;j<m;j++)
		{
		if(a[i][j] == row_max[i]  || a[i][j] == column_max[j])
				continue;
			else
				return false;
		}
	}
	return true;
}


int main(){
#ifdef re
freopen("input.txt","r",stdin);
freopen("output.txt","w",stdout);
freopen("log.txt","w",stderr);
#endif
cin>>t;
for(int i=1;i<=t;i++)
{
	preprocess();


	cout<<"Case #"<<i<<": ";
	if(solve())
		cout<<"YES";
	else
		cout<<"NO";
	cout<<endl;
}
#ifdef re
//printf("\n  Time Taken  %.31f sec\n",(double)clock()/(CLOCKS_PER_SEC));

#endif
return 0;
}

