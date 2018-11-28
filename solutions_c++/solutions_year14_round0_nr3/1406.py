


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

#define MAXN 55
int mp[MAXN][MAXN];
int r,c,m;
int vx[8] = {0,1,1,1,0,-1,-1,-1};
int vy[8] = {1,1,0,-1,-1,-1,0,1}; //8������

bool isin(int x,int y) 
{
	if(x>=1&&x<=r&&y>=1&&y<=c)
		return true;
	return false;
}
bool boom(int x,int y)
{
	for(int i=0;i<8;i++)
	{
		if( isin(x+vx[i],y+vy[i]) && (mp[x+vx[i]][y+vy[i]] == 1))
			return false;
	}
	return true;
}
void work()
{
	
	memset(mp,0,sizeof(mp));  //0��ʾ.
	cin>>r>>c>>m;
	//�涨r<c
	int flag = 0;
	if(r>c)  
	{
		swap(r,c);  flag = 1; //��ʾrc�����ˡ�
	}
	int res = 1; //����Ƿ��н⡣
	//̰�������Ž⡣
	int t = m; //��ʾʣ����ٸ���
	int k = 1;
	if(r<=2)
	{
		for(int j=1;j<=c;j++)
			for(int i=1;i<=r;i++)
			{
				if(t==0) break;
				mp[i][j] = 1;
				t--;
			}
	}

	else
	{
		while(t>=r+c+1-2*k)
		{
			for(int i=1;i<=r;i++)
				mp[i][k] = 1; 
			for(int i=1;i<=c;i++)
				mp[k][i] = 1;
			t -= r+c+1-2*k;
			k++;
		}
		// t<r+c+1-2*k
		if(r-k+1<=2) //��<=2��
		{
			for(int j=k;j<=c;j++)
			{
				for(int i=k;i<=r;i++)
				{
					if(t==0) break;
					mp[i][j] = 1;
					t--;
				}
				if(t==0) break;
			}
		}

		else if(t == c+r-2*k-3) //��>=3
		{
			//���
			for(int i=k;i<=r-2;i++)
				mp[i][k] = 1;
			for(int j=k;j<=c-2;j++)
				mp[k][j] = 1;
		}
		else if(t == c+r-2*k-2)
		{
			//����һ���ض�һ����
			if((c-k+1) == 3)
			{
				mp[k][k] = mp[k+1][k] = 1;
			}
			else
			{
				for(int i=k;i<=r;i++)
					mp[i][k] = 1;
				for(int j=k;j<=c-3;j++)
					mp[k][j] = 1;
			}


		}
		else if(t == c+r-2*k-1)
		{
			//����һ�м���
			for(int i=k;i<=r;i++)
				mp[i][k] = 1;
			for(int j=k;j<=c-2;j++)
				mp[k][j] = 1;
		}
		else if(t == c+r-2*k)
		{
			//����������
			if(r>=4)
			{
				for(int i=k;i<=r;i++)
				{
					for(int j=k;j<=c;j++)
					{
						if(t==0) break;
						mp[i][j] = 1;
						t--;
					}
					if(t==0) break;
				}
			}
			else //����������
			{
				for(int j=k;j<=c;j++)
					for(int i=k;i<=r;i++)
					{
						if(t==0) break;
						mp[i][j] = 1;
						t--;
					}
			}
			
		}
		else
		{
			for(int i=k;i<=r-2;i++)
			{
				if(t==0) break;
				mp[i][k] = 1;
				t--;
			}
			for(int j=k+1;j<=c-2;j++)
			{
				if(t==0) break;
				mp[k][j] = 1;
				t--;
			}
		}
	}

	

// 	for(int i=1;i<=r;i++)
// 	{
// 		for(int j=1;j<=c;j++)
// 		{
// 			cout<<mp[i][j];
// 		}
// 		cout<<endl;
// 	}

	// ����ж��Ƿ�Ҫ�������
	// �ҳ���������㡣������Щ����չ�������Ȼ��0���֣���Imposible
	for(int i=1;i<=r;i++)
		for(int j=1;j<=c;j++)
		{
			if(mp[i][j]==0 && boom(i,j))
			{
				mp[i][j]=2; //������boom���2
			}
		}
	for(int i=1;i<=r;i++)
		for(int j=1;j<=c;j++)
		{
			if(mp[i][j]==2)
			{
				for(int k=0;k<8;k++)
				{
					int ni = i+vx[k];
					int nj = j+vy[k];
					if(isin(ni,nj) && mp[ni][nj]==0 )
						mp[ni][nj] = 3;
				}
			}
		}
	for(int i=1;i<=r;i++)
		for(int j=1;j<=c;j++)
			if(mp[i][j] == 0)
			{ 
				res = 0; break;
			}
	if((r*c-1)==m ) 
		res = 1;
	else if(r*c<=m)
		res = 0;
	if(res == 0)
		cout<<"Impossible"<<endl;
	else if(!flag)
	{
		for(int i=1;i<=r;i++)
		{
			for(int j=1;j<=c;j++)
			{
				if(i==r && j==c)
					cout<<"c";
				else if(mp[i][j] == 1)
				{
					cout<<"*";
				}
				else
					cout<<".";
			}
			cout<<endl;
		}
	}
	else
	{
		for(int j=1;j<=c;j++)
		{
			for(int i=1;i<=r;i++)
			{
				if(i==r && j==c)
					cout<<"c";
				else if(mp[i][j] == 1)
				{
					cout<<"*";
				}
				else
					cout<<".";
			}
			cout<<endl;
		}
	}
}

int main()
{
	freopen("a2.in", "r", stdin);
	freopen("a2.out", "w", stdout);

	int t2;
	cin >> t2;
	for (int t1 = 1; t1 <= t2; ++t1) {
		printf("Case #%d: \n", t1);
		work();
//		printf("\n");
	}

	return 0;
}

