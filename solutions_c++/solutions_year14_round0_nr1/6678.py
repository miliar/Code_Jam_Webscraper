#include<fstream>

#define f(i,a,b) for(int (i)=(a);(i)<(b);++(i))

using namespace std;

int main()
{
	ifstream fin("A-small-attempt0.in");
	ofstream fout("A.out");
	int t;
	fin>>t;
	for(int cas=1;cas<=t;++cas)
	{
		fout<<"Case #"<<cas<<": ";
		int g[2];
		int a[2][4][4];
		f(k,0,2)
		{
			fin>>g[k];
			g[k]--;
		f(i,0,4)
		{
			f(j,0,4)
			{
				fin>>a[k][i][j];
			}
		}
		}
		int count=0,val=-1;
		for(int i=1;i<=16;++i)
		{
			bool good=true;
			f(k,0,2)
			{
				bool tgood=false;
					f(j,0,4)
					{
						if(i==a[k][g[k]][j])
							tgood=true;
					}
				good=(good&&tgood);
			}
			if(good)
			{
				count++;
				val=i;
			}
		}
		if(count==1)
		{
			fout<<val<<'\n';
		}
		else if(count==0)
		{
			fout<<"Volunteer cheated!\n";
		}
		else
		{
			fout<<"Bad magician!\n";
		}
	}
	return 0;
}
