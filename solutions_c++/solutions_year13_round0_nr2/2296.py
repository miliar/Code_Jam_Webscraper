#include<iostream>
using namespace std;
int a[101][101];
int b[101][101];
int maxc[101];
int minr[101];
int maxr[101];
int main()
{
	int cas,r,c;
	cin>>cas;
	for(int q = 1;q<=cas ; q++)
	{
		cin>>r>>c;
		for(int i = 0 ;i < r ; i++){ maxr[i] = 0;minr[i] = 1000;}
		for(int i = 0 ;i < c ; i++) maxc[i] = 0;

		for(int i = 0 ;i < r ; i++)
			for(int j = 0 ;j < c ; j++)
			{
				cin>>a[i][j];
				minr[i] = min(minr[i],a[i][j]);
				maxr[i] = max(maxr[i],a[i][j]);
				maxc[j] = max(maxc[j],a[i][j]);
			}

		for(int i = 0 ;i < c ; i++)
			for(int j = 0 ;j < r ; j++)
				b[j][i] = maxc[i];
		
		for(int i = 0 ;i < r ; i++)
		{
			if(minr[i] == maxr[i])
			{
				for(int j = 0 ;j < c ; j++)
				{
					b[i][j] = minr[i];
				} 
			}
		}
		bool sol = true;
		for(int i = 0 ;i < r ; i++)
			for(int j = 0 ;j < c ; j++)
				if(a[i][j] != b[i][j])sol = false;

		cout<<"Case #"<<q<<": "<<(sol ? "YES": "NO")<<endl;
	}
	return 0;
}
