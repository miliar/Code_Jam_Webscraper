#include<fstream>
using namespace std;
int main()
{
	ifstream f("B-large.in");
	ofstream f1("output.txt");
	int t=0;
	f>>t;
	int n,m,ans=1;
	int maxr[100]={0},maxc[100]={0};
	int a[100][100];
	for(int k=0;k<t;k++)
	{
		ans=1;
		f>>n>>m;
		for(int i=0;i<n;i++)
			maxr[i]=0;
		for(int i=0;i<m;i++)
			maxc[i]=0;
		for(int i=0;i<n;i++)
		{
			for(int j=0;j<m;j++)
			{
				f>>a[i][j];
				if(a[i][j]>maxr[i])
				{
					maxr[i]=a[i][j];
				}
				if(a[i][j]>maxc[j])
				{
					maxc[j]=a[i][j];
				}
			}
		}
		for(int i=0;i<n;i++)
		{
			for(int j=0;j<m;j++)
				if(maxr[i]>a[i][j]&&maxc[j]>a[i][j])
				{
					ans=0;
					break;
				}
		}
		f1<<"Case #"<<k+1<<": ";
		if(ans==1)
			f1<<"YES";
		else
			f1<<"NO";
		f1<<endl;
	}
	return 0;
}