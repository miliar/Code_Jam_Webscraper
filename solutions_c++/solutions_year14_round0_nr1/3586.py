#include <vector>
#include <list>
#include <map>
#include <set>
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
#include <fstream>
#define tr(c,i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
using namespace std;
int main()
{
	freopen("as.in","r",stdin);
	freopen("a_small.out","w",stdout);
	int t;
	cin>>t;
	for(int testc=1;testc<=t;testc++)
	{
		int choice1,choice2,A[4][4];
		vector <int> B(4);
		cin>>choice1;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				cin>>A[i][j];
			}
		}
		for(int i=0;i<4;i++)
			B[i]=A[choice1-1][i];
		cin>>choice2;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				cin>>A[i][j];
			}
		}
		int counter=0,ans;
		for(int i=0;i<4;i++)
		{
			if(find(B.begin(),B.end(),A[choice2-1][i])!=B.end())
			{
				counter++;
				ans=A[choice2-1][i];
			}
		}
		if(counter==0)
			cout<<"Case #"<<testc<<": Volunteer cheated!\n";
		else if(counter==1)
			cout<<"Case #"<<testc<<": "<<ans<<"\n";
		else
			cout<<"Case #"<<testc<<": Bad magician!\n";
	}
	return 0;
}