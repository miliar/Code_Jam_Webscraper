#include<fstream>
#include<vector>

#define f(i,a,b) for( int (i)=(a);(i)<(b);++(i))
using namespace std;

ofstream fout;
ifstream fin;
int r[1000],c[1000];
int gr[1000][1000];
int ngr[1000][1000];
int t,n,m;
int main()
{
	fin.open("B-large.in");
	fout.open("B.out");
	fin>>t;
	f(cas,1,t+1)
	{
		fout<<"Case #"<<cas<<": ";
		fin>>n>>m;
		f(i,0,n)
		{
			f(j,0,m)
			{
				fin>>gr[i][j];
				ngr[i][j]=100;
			}
		}
				
		f(i,0,n)
		{
			int best=0;
			f(j,0,m)
				best=max(best,gr[i][j]);
			f(j,0,m)
			{
				ngr[i][j]=min(ngr[i][j],best);
			}
		}
		f(j,0,m)
		{
			int best=0;
			f(i,0,n)
				best=max(best,gr[i][j]);
			f(i,0,n)
			{
				ngr[i][j]=min(ngr[i][j],best);
			}
		}
		bool ans =true;
		f(i,0,n)
		{
			f(j,0,m)
			{
				ans =ans &&(gr[i][j]==ngr[i][j]);
			}
		}
		if (ans)
		{
			fout<<"YES\n";
		}
		else
		{
			fout<<"NO\n";
		}
	}
	fin.close();
	fout.close();

	return 0;
}
