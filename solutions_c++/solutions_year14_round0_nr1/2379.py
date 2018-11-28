/*************************************************************************
    > File Name: 1.cpp
    > Author: mengshangqi
    > Mail: mengshangqi@gmail.com 
    > Created Time: 2014年04月12日 星期六 16时42分19秒
 ************************************************************************/

#include<iostream>
#include<cstdio>
#include<set>
#include<map>
#include<algorithm>
#include<vector>
#include<cstring>
#include<string>
#include<bitset>
#include<sstream>
#include<queue>
#include<stack>
#include<cmath>
using namespace std;
int main()
{
#ifndef ONLINE_JUDGE
    freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
#endif
	int t;
	int x,y;
	int num;
	set<int> cont;
	cin>>t;
	for(int c=1;c<=t;c++)
	{
		cin>>x;
		cont.clear();
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
			{
				cin>>num;
				if(i==x-1) cont.insert(num);
			}
		cin>>y;
		vector<int> ans;
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
			{
				cin>>num;
				if(i==y-1)
				{
					if(cont.count(num)) ans.push_back(num);
				}
			}
		printf("Case #%d: ",c);
		if(ans.size()==1) cout<<ans[0]<<endl;
		else if(ans.size()==0) cout<<"Volunteer cheated!"<<endl;
		else cout<<"Bad magician!"<<endl;
	}
    return 0;
}
