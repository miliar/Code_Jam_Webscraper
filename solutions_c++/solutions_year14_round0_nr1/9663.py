#include<iostream>
#include<cstdio>
#include<string>
#include<sstream>
#include<cmath>

#include<algorithm>
#include<array>
#include<bitset>
#include<deque>
#include<list>
#include<map>
#include<queue>
#include<set>
#include<stack>
#include<valarray>
#include<vector>

#include<complex>
#include <functional>
#include<iomanip>
#include <numeric>
#include <utility>
#include<cassert>


typedef long long LL;

//#define Px(x)	cout<<#x<<": "<<(x)<<endl
//#define P(x)	cout<<(x)<<endl
//#define all(v)	((v).begin()), ((v).end())
//#define sz(v)	((int)((v).size()))
//#define max(a,b) ((a)>(b))?(a):(b)
//#define min(a,b) ((a)<(b))?(a):(b)
//#define between(a,x,b) (((a)<(x))&&((x)<(b)))
//#define between01(a,x,b) (((a)<(x))&&((x)<=(b)))
//#define between10(a,x,b) (((a)<=(x))&&((x)<(b)))
//#define between2(a,x,b) (((a)<=(x))&&((x)<=(b)))
//#define for_range(i,a,b) for(int (i) = (a);(i)<(b);(i)++)

using namespace std;

void main1();
void main()
{
	freopen("input.txt","rt",stdin);
	freopen("output.txt","wt",stdout);
	int n=0;
	cin>>n;
	for(int i=0;i<n;i++)
	{	
		cout<<"Case #"<<i+1<<": ";
		main1();
		cout<<endl;
	}
}

void main1()
{
	int grid1[4][4];
	int grid2[4][4];
	vector<int> chosen1;
	vector<int> chosen2;
	int n1,n2;
	cin>>n1;
	for (int i = 0; i < 4; i++)
	{
		for (int j = 0; j < 4; j++)
		{
			cin>>grid1[i][j];
			if(i==(n1-1))
				chosen1.push_back(grid1[i][j]);
		}
	}

	cin>>n2;
	for (int i = 0; i < 4; i++)
	{
		for (int j = 0; j < 4; j++)
		{
			cin>>grid2[i][j];
			if(i==(n2-1))
				chosen2.push_back(grid2[i][j]);

		}
	}
	vector<int> intersec;
	sort(chosen1.begin(),chosen1.end());
	sort(chosen2.begin(),chosen2.end());
	set_intersection(chosen1.begin(),chosen1.end(),chosen2.begin(),chosen2.end(),back_inserter(intersec));
	if(intersec.size()==1)
	{
		cout<<intersec[0];
	}
	else if(intersec.size()==0)
		cout<<"Volunteer cheated!";
	else
		cout<<"Bad magician!";

}