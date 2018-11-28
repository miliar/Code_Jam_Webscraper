

#include <iostream>
#include <sstream>
#include <cstring>
#include <cstdlib>
#include <string>
#include <cstdio>
#include <algorithm>
#include <numeric>
#include <functional>
#include <vector>
#include <deque>
#include <list>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <cmath>
using namespace std;

int a;
int b;
vector<int> veca;
vector<int> vecb;

void work()
{
	veca.clear();
	vecb.clear();
	int ra,rb;
	cin>>ra;
	for(int i=1;i<=4;i++)
		for(int j=1;j<=4;j++)
		{
			cin>>a;
			if(i==ra)
				veca.push_back(a);
		}
	cin>>rb;
	for(int i=1;i<=4;i++)
		for(int j=1;j<=4;j++)
		{
			cin>>b;
			if(i==rb)
				vecb.push_back(b);
		}
	int cnt = 0;//表示有多少个相同的元素。
	for(int i=0;i<vecb.size();i++)
		for(int j=0;j<veca.size();j++)
		{
			if(veca[j] == vecb[i])
			{
				cnt++;  a = veca[j];
			}
		}
	if(cnt == 1)
		cout<<a<<endl;
	else if(cnt==0)
		cout<<"Volunteer cheated!"<<endl;
	else
		cout<<"Bad magician!"<<endl;
}

int main()
{
	freopen("a2.in", "r", stdin);
	freopen("a2.out", "w", stdout);

	int t2;
	cin >> t2;
	for (int t1 = 1; t1 <= t2; ++t1) {
		printf("Case #%d: ", t1);
		work();
//		printf("\n");
	}

	return 0;
}