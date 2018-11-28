#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
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

using namespace std;

int m[6][6];

vector<int>vi,vj;

int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("output.txt","w",stdout);
	int i,j,k,x,y,t,l,cases;
	m[1][1] = 1;
	m[1][2] = 2;
	m[1][3] = 3;
	m[1][4] = 4;

	m[2][1] = 2;
	m[2][2] = -1;
	m[2][3] = 4;
	m[2][4] = -3;

	m[3][1] = 3;
	m[3][2] = -4;
	m[3][3] = -1;
	m[3][4] = 2;

	m[4][1] = 4;
	m[4][2] = 3;
	m[4][3] = -2;
	m[4][4] = -1;

	scanf("%d",&cases);
	for(t = 1;t<=cases;t++)
	{

		string s,s1;
		s.clear();
		s1.clear();

		scanf("%d%d",&l,&x);
		cin >> s;

		for(i = 0;i<x;i++)
			s1+=s;

		//cout << "s1: "<< s1 <<endl;
		s.clear();

		vi.clear();
		vj.clear();
		bool flag = 0;
		for(i = 0;i<s1.length();i++)
		{
			if(s1[i] == '1') s+='1';
			else
				s+=s1[i]-'i'+2+'0';
		}

		int ans = 1;
		i = -1;

		//cout << "s:"<<s<<endl;

		for( i = 0;i<s.length();i++)
		{
			k = 1;
			if(ans < 0) k = -1;

			ans = m[abs(ans)][s[i]-'0'];
			ans = ans*k;

			//printf("i = %d ans = %d\n",i,ans);
			if(ans == 4)
				vj.push_back(i);
			else if (ans == 2)
				vi.push_back(i);

		}

		if(ans == -1)
		{
			for(i =0;i<vi.size();i++)
			{
				x = vi[i];
				if(upper_bound(vj.begin(),vj.end(),x) != vj.end())
				{
					flag = 1;
					break;
				}

			}
		}

		if(flag)
			printf("Case #%d: YES\n",t);
		else
			printf("Case #%d: NO\n",t);

	}

	return 0;

}
