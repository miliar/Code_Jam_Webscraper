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
vector <vector <char> > ans;
int r,c,m;
bool is_star(int i,int j)
{
	if(i<0)
		return false;
	if(i>=r)
		return false;
	if(j<0)
		return false;
	if(j>=c)
		return false;
	if(ans[i][j]=='*')
		return true;
	return false;
}
bool is_zero(int i,int j)
{
	if(i<0)
		return false;
	if(i>=r)
		return false;
	if(j<0)
		return false;
	if(j>=c)
		return false;
	if(is_star(i-1,j-1))
		return false;
	if(is_star(i-1,j))
		return false;
	if(is_star(i-1,j+1))
		return false;
	if(is_star(i,j-1))
		return false;
	if(is_star(i,j))
		return false;
	if(is_star(i,j+1))
		return false;
	if(is_star(i+1,j-1))
		return false;
	if(is_star(i+1,j))
		return false;
	if(is_star(i+1,j+1))
		return false;
	return true;
}
bool checker()
{
	int c_count=0,m_count=0;
	for(int i=0;i<r;i++)
	{
		for(int j=0;j<c;j++)
		{
			if(ans[i][j]=='c')
				c_count++;
			if(ans[i][j]=='*')
				m_count++;
		}
	}
	if(c_count!=1)
		return false;
	if(m_count!=m)
		return false;
	vector < vector<int> > A(r,vector <int> (c,0));
	for(int i=0;i<r;i++)
	{
		for(int j=0;j<c;j++)
		{
			if(ans[i][j]=='.' || ans[i][j]=='c')
			{
				if(is_zero(i-1,j-1))
					continue;
				if(is_zero(i-1,j))
					continue;
				if(is_zero(i-1,j+1))
					continue;
				if(is_zero(i,j-1))
					continue;
				if(is_zero(i,j))
					continue;
				if(is_zero(i,j+1))
					continue;
				if(is_zero(i+1,j-1))
					continue;
				if(is_zero(i+1,j))
					continue;
				if(is_zero(i+1,j+1))
					continue;
				return false;
			}
		}
	}
	return true;
}
void refresher()
{
	for(int i=0;i<r;i++)
	{
		for(int j=0;j<c;j++)
		{
			ans[i][j]='*';
		}
	}
}
bool click_at_corner()
{
	refresher();
	ans[0][0]='c';
	int normal_left=(r*c)-1-m;
	if(normal_left>=(r*r))
	{
		if(normal_left%r==0 && normal_left%c==0)
			return false;
		else if(normal_left%r==0)
		{
			for(int i=0;i<r;i++)
			{
				for(int j=0;j<c;j++)
				{
					if(i==0 && j==0)
						continue;
					ans[i][j]='.';
					normal_left--;
					if(!normal_left)
						break;
				}
				if(!normal_left)
					break;
			}
			return true;
		}
		else
		{
			for(int j=0;j<c;j++)
			{
				for(int i=0;i<r;i++)
				{
					if(i==0 && j==0)
						continue;
					ans[i][j]='.';
					normal_left--;
					if(!normal_left)
						break;
				}
				if(!normal_left)
					break;
			}
			return true;
		}
	}
	else
	{
		for(int i=1;i<r;i++)
		{
			if(normal_left==0)
				return true;
			if(normal_left>=(2*i)+1)
			{
				for(int j=0;j<=i;j++)
				{
					ans[i][j]='.';
					ans[j][i]='.';
				}
				normal_left-=(2*i)+1;
			}
			else
			{
				if(i==1)
					return false;
				else
				{
					if(normal_left==1 || normal_left==3)
						return false;
					if(normal_left==2)
					{
						ans[i][0]='.';
						ans[i][1]='.';
						return true;
					}
					if(normal_left%2==0)
					{
						ans[i][0]='.';
						ans[0][i]='.';
						int curr_pos=1;
						normal_left-=2;
						while(normal_left)
						{
							ans[i][curr_pos]='.';
							ans[curr_pos][i]='.';
							normal_left-=2;
							curr_pos++;
						}
						return true;
					}
					if(normal_left%2==1)
					{
						ans[i][i]='.';
						ans[i][i-1]='.';
						ans[i][i-2]='.';
						ans[i-1][i]='.';
						ans[i-2][i]='.';
						int curr_pos=i-3;
						normal_left-=5;
						while(normal_left)
						{
							ans[i][curr_pos]='.';
							ans[curr_pos][i]='.';
							normal_left-=2;
							curr_pos--;
						}
						return true;
					}
				}
			}
		}
		if(normal_left==0)
			return true;
	}
	return false;
}
int main()
{
	freopen("cs.in","r",stdin);
	freopen("c_small.out","w",stdout);
	int t;
	cin>>t;
	for(int testc=1;testc<=t;testc++)
	{
		int org_r,org_c;
		cin>>org_r>>org_c>>m;
		r=min(org_r,org_c);
		c=max(org_r,org_c);
		ans.clear();
		ans.resize(r,vector <char> (c));
		bool ans_exist=false;
		if(r==1)
		{
			ans_exist=true;
			for(int i=0;i<c;i++)
				ans[0][i]='*';
			ans[0][0]='c';
			for(int i=1;i<c-m;i++)
				ans[0][i]='.';
		}
		else if(r==2)
		{
			if(m==(r*c)-1)
			{
				ans_exist=true;
				refresher();
				ans[0][0]='c';
			}
			else if(m<=(r*c)-4)
			{
				if(m%2==0)
				{
					ans_exist=true;
					refresher();
					ans[0][0]='c';
					for(int i=0;i<r;i++)
					{
						for(int j=0;j<c-(m/2);j++)
						{
							if(i || j)
								ans[i][j]='.';
						}
					}
				}
				else{
					ans_exist=false;
				}
			}
			else
			{
				ans_exist=false;
			}
		}
		else if(r==3)
		{
			if(click_at_corner())
			{
				ans_exist=true;
			}
			else
			{
				ans_exist=false;
			}
		}
		else if(r==4)
		{
			if(click_at_corner())
			{
				ans_exist=true;
			}
			else if(c==4 && m==4)
			{
				ans_exist=true;
				refresher();
				ans[0][0]='c';
				for(int i=0;i<3;i++)
				{
					for(int j=0;j<4;j++)
					{
						if(i || j)
						{
							ans[i][j]='.';
						}
					}
				}
			}
			else if(c==4 && m==6)
			{
				ans_exist=true;
				refresher();
				ans[0][0]='c';
				for(int i=0;i<4;i++)
				{
					for(int j=0;j<2;j++)
					{
						if(i || j)
							ans[i][j]='.';
					}
				}
				ans[0][2]='.';
				ans[1][2]='.';
			}
			else if(c==5 && m==8)
			{
				ans_exist=true;
				refresher();
				ans[0][0]='c';
				for(int i=0;i<4;i++)
				{
					for(int j=0;j<3;j++)
					{
						if(i || j)
							ans[i][j]='.';
					}
				}
			}
			else if(c==5 && m==10)
			{
				ans_exist=true;
				refresher();
				ans[0][0]='c';
				for(int i=0;i<2;i++)
				{
					for(int j=0;j<5;j++)
					{
						if(i || j)
							ans[i][j]='.';
					}
				}
			}
			else
			{
				ans_exist=false;
			}
		}
		else
		{
			if(click_at_corner())
			{
				ans_exist=true;
			}
			else if(c==5)
			{
				if(m==6)
				{
					ans_exist=true;
					refresher();
					ans[0][0]='c';
					for(int i=0;i<4;i++)
					{
						for(int j=0;j<5;j++)
						{
							if(i || j)
								ans[i][j]='.';
						}
					}
					ans[3][4]='*';
				}
				if(m==8)
				{
					ans_exist=true;
					refresher();
					ans[0][0]='c';
					for(int i=0;i<3;i++)
					{
						for(int j=0;j<5;j++)
						{
							if(i || j)
								ans[i][j]='.';
						}
					}
					ans[3][0]='.';
					ans[3][1]='.';
				}
				if(m==13)
				{
					ans_exist=true;
					refresher();
					ans[0][0]='c';
					for(int i=0;i<4;i++)
					{
						for(int j=0;j<4-i;j++)
						{
							if(i || j)
								ans[i][j]='.';
						}
					}
					ans[3][1]='.';
					ans[1][3]='.';
				}
				if(m==15)
				{
					ans_exist=true;
					refresher();
					ans[0][0]='c';
					for(int i=0;i<2;i++)
					{
						for(int j=0;j<5;j++)
						{
							if(i || j)
								ans[i][j]='.';
						}
					}
				}
			}
			else
			{
				ans_exist=false;
			}
		}
		printf("Case #%d:\n",testc);
		if(ans_exist)
		{
			if(r==org_r)
			{
				for(int i=0;i<r;i++)
				{
					for(int j=0;j<c;j++)
					{
						printf("%c",ans[i][j]);
					}
					printf("\n");
				}
			}
			else
			{
				for(int j=0;j<c;j++)
				{
					for(int i=0;i<r;i++)
					{
						printf("%c",ans[i][j]);
					}
					printf("\n");
				}
			}
			// if(!checker())
			// {
			// 	printf("Fallacy\n");
			// 	for(int i=0;i<r;i++)
			// 	{
			// 		for(int j=0;j<c;j++)
			// 		{
			// 			printf("%c",ans[i][j]);
			// 		}
			// 		printf("\n");
			// 	}
			// }
		}
		else
		{
			printf("Impossible\n");
		}
	}
	return 0;
}