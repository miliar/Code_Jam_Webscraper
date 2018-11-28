#include <fstream>
using namespace std;

int chk[100][100];
int a[100][100];
int N, M;
int cnt;

void f1(int h)
{
	int i, j;
	int chk2;

	for(i=0;i<N;i++)
	{
		chk2=0;
		for(j=0;j<M;j++)
		{
			if(h < a[i][j]) break;
			else if(h == a[i][j]) chk2=1;
		}
		if(j==M && chk2)
		{
			for(j=0;j<M;j++)
			{	
				if(h == a[i][j] && !chk[i][j]) 
				{
					chk[i][j]=1;
					cnt++;
				}
			}
		}
	}
}

void f2(int h)
{
	int i, j;
	int chk2;

	for(j=0;j<M;j++)
	{
		chk2=0;
		for(i=0;i<N;i++)
		{
			if(h < a[i][j]) break;
			else if(h == a[i][j]) chk2=1;
		}
		if(i==N && chk2)
		{
			for(i=0;i<N;i++)
			{	
				if(h == a[i][j] && !chk[i][j]) 
				{
					chk[i][j]=1;
					cnt++;
				}
			}
		}
	}	
}

int main()
{
	ifstream cin("B-large.in");
	ofstream cout("out.txt");
	int max = 0;
	int T;
	cin >> T;
	for(int t=1;t<=T;t++)
	{
		cin >> N >> M;
		for(int i=0;i<N;i++)
		{
			for(int j=0;j<M;j++)
			{
				cin >> a[i][j];
				chk[i][j] = 0;
				if(max<a[i][j]) max = a[i][j];
			}
		}
		cnt = 0;
		int h;
		for(h=max;h>0;h--)
		{
			f1(h);
			f2(h);
			if(cnt==N*M)
			{
				cout << "Case #" << t << ": YES" << endl;
				break;
			}
		}
		if(h==0) cout << "Case #" << t << ": NO" << endl;
	}
}
