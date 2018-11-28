#include <set>
#include <map>
#include <list>
#include <stack>
#include <queue>
#include <cmath>
#include <deque>
#include <bitset>
#include <cstdio>
#include <vector>
#include <string>
#include <complex>
#include <sstream>
#include <utility>
#include <climits>
#include <cstring>
#include <fstream>
#include <iostream>
#include <iomanip>
#include <algorithm>

#define OO (int) 1e9

using namespace std;


int main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("out.text","w",stdout);
	int f,s;
	int tc;
	cin>>tc;
	for(int a=1;a<=tc;a++)
	{
		vector <int> firstRow,secondRow;
		cin>>f;
		int x;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				cin>>x;
				if(i==f-1) firstRow.push_back(x);
			}
		}
		cin>>s;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				cin>>x;
				if(i==s-1) secondRow.push_back(x);
			}
		}

		int intersection=0;
		int res=0;
		for(int i=0;i<firstRow.size();i++)
		{
			for(int j=0;j<secondRow.size();j++)
			{
				if(firstRow[i]==secondRow[j])
				{
					intersection++;
					res=firstRow[i];
					break;
				}
			}
		}
		cout<<"Case #"<<a<<": ";
		if(intersection==1) cout<<res<<endl;
		else if (intersection>1) cout<<"Bad magician!"<<endl;
		else cout<<"Volunteer cheated!"<<endl;

	}

}
