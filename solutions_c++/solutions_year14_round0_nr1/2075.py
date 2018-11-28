#include <iostream>
#include <fstream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <stdio.h>
#include <cmath>
#include <math.h>
#include <stdlib.h>

#include <algorithm>
#include <cstring>
#include <vector>
#include <string>
#include <sstream>
#include <queue>
using namespace std;
int main()
{
	int T,ans,tmp;
	cin>>T;
	for (int i=1;i<=T;i++)
	{
		int cnt[16]={0};
		cin>>ans;
		for (int j=1;j<=4;j++)
		{
			for (int k=0;k<4;k++)
			{
				cin>>tmp;
				if (j==ans)
				{
					 cnt[tmp-1]++;
				}
			}
		}
		cin>>ans;
		for (int j=1;j<=4;j++)
		{
			for (int k=0;k<4;k++)
			{
				cin>>tmp;
				if (j==ans)
				{
					 cnt[tmp-1]++;
				}
			}
		}
		int res=-1, flag = 0;
		for (int j=0;j<16;j++)
		{
			if (cnt[j]==2)
			{
				if (res==-1)
					res = j+1;
				else
					flag = 1;
			}
		}
		cout<<"Case #"<<i<<": ";
		if (flag == 1)
			cout<<"Bad magician!"<<endl;
		else if (res == -1)
			cout<<"Volunteer cheated!"<<endl;
		else cout<<res<<endl;
	}
}