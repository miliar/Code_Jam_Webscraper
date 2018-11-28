#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <cctype>
#include <algorithm>
#include <vector>
#include <numeric>
#include <set>
#include <queue>
#include <map>
#include <list>
#include <string>
#include <iostream>
#include <stack>
#include <sstream>
using namespace std; 
#define PB push_back
#define MP make_pair
#define F first
#define S second 
#define BE(a) a.begin(),a.end() 
#define CLS(a,b) memset(a,b,sizeof(a))
#define SZ(a) ((int)a.size())
const long double pi=acos(-1.0);
#define torad(a) ((a)*pi/180.0)
typedef vector<int> vi ; 
typedef vector<string> vs ; 
typedef vector<double> vd ; 
typedef pair<int,int> pii ; 
typedef long long ll ; 
typedef long double ld ; 
typedef double dl ; 
class node {public:
};
typedef vector<node> vn ; 
int cases,g,n;
vi red;
vi blue;
int main()
{
	freopen("A-small-attempt5.in","r",stdin);
	freopen("A-small-attempt5.out","w",stdout);
	int n,ans1,ans2,output,count=0,array1[4][4],array2[4][4],arr1[4],arr2[4];
	cin>>n;
	for(int i=1;i<=n;i++)
	{
		cin>>ans1;
		for(int j=0;j<4;j++)
			for(int k=0;k<4;k++)
			{
				cin>>array1[j][k];
				if(j==ans1-1)
					arr1[k] = array1[j][k];
			}

			cin>>ans2;
	for(int j=0;j<4;j++)
		for(int k=0;k<4;k++)
			{
				cin>>array2[j][k];
				if(j==ans2-1)
					arr2[k] = array2[j][k];
			}

	for(int j=0;j<4;j++)
		for(int k=0;k<4;k++)
			{
				if(arr1[j] ==arr2[k])
				{
					output=arr1[j];
					count++;
				}
				if( count > 1)
					break;
		}

		if( count == 0 )
			cout<<"Case #"<<i<<": Volunteer cheated!"<<endl;
		else if( count > 1)
			cout<<"Case #"<<i<<": Bad magician!"<<endl;
		else
			cout<<"Case #"<<i<<": "<<output<<endl;

		count=0;
	}
	return 0;
}
