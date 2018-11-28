#include <iostream>
using namespace std;
#include <set>
#include <cmath>
#include <vector>
#include <algorithm>
#include <string>
#include <string.h>
#include <sstream> 
#include <cstdio>
#include <stdio.h>
#include<utility>
#include <math.h>
#include <functional>
#include <map>
#include <queue>
int arr[4][4];
int main()
{
	freopen("A-small-attempt3.in", "r", stdin);
	freopen("out1.out", "w", stdout);
	bool da5al=0,da5altani=0;
	int T,R,ans,sum=0;
	cin>>T;
	vector<int>v;
	for (int i = 0; i < T; i++)
	{
		cout<<"Case #"<<i+1<<": ";//Case #1: 
		cin>>R;
		for (int r = 0; r < 4; r++)
		{
			for (int c = 0; c < 4; c++)
				cin>>arr[r][c];
		}
		v.push_back(arr[R-1][0]);v.push_back(arr[R-1][1]);v.push_back(arr[R-1][2]);v.push_back(arr[R-1][3]);
		cin>>R;
		for (int rr = 0; rr < 4; rr++)
		{
			for (int cc = 0; cc < 4; cc++)
				cin>>arr[rr][cc];
		}
		v.push_back(arr[R-1][0]);v.push_back(arr[R-1][1]);v.push_back(arr[R-1][2]);v.push_back(arr[R-1][3]);
		sort(v.begin(),v.end());
		int rep=1;
		for (int a = 0; a < 8; a+=rep)
		{
			rep=count (v.begin(), v.end(), v[a]);
			sum++;
			if(rep==2)
			{
				if(da5al)da5altani=1;
				da5al=1;
				ans=v[a];
			}
		}
		
		if(da5altani)cout<<"Bad magician!"<<endl;
		else if(da5al)cout<<ans<<endl;
		else cout<<"Volunteer cheated!"<<endl;
		v.clear();sum=0;da5al=da5altani=0;

	}
	return 0;
}