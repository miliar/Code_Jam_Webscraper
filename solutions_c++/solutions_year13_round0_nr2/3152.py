#include <iostream>
#include <list>
#include <vector>
#include <queue>
using namespace std;
int lawn[105][105];
class Node
{
public:
	int h;
	int x;
	int y;
	Node(int h_,int x_,int y_)
	{
		h=h_;
		x=x_;
		y=y_;
	}
	Node()
	{
	}
	bool operator < (const Node another)
	{
		return h>another.h;
	}
};
bool operator < (const Node a, const Node b)
	{
		return a.h>b.h;
	}
int main()
{
	int T,N,M;
	cin>>T;
	for (int i=1;i<=T;i++)
	{
		cin>>N>>M;
		priority_queue<Node> que;
		for (int j=0;j<N;j++)
			for (int k=0;k<M;k++)
			{
				cin>>lawn[j][k];
				que.push(Node(lawn[j][k],j,k));
			}

		bool valid = true;
		while(!que.empty())
		{
			Node cur = que.top();
			que.pop();
			int cnt = 0;
			for (int j=0;j<N;j++)
				if (lawn[j][cur.y]>cur.h)
				{
					cnt++;
					break;
				}
			
			for (int j=0;j<M;j++)
				if (lawn[cur.x][j]>cur.h)
				{
					cnt++;
					break;
				}
			if (cnt>=2)
			{
				valid = false;
				break;
			}
		}
		cout<<"Case #"<<i<<": ";
		if (valid)
			cout<<"YES"<<endl;
		else cout<<"NO"<<endl;
	}
	return 0;
}