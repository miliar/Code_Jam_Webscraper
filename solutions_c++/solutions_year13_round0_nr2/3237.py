#include<fstream>
#include<cmath>
using namespace std;
int T,n,m,mat[110][110],maximL[110],maximC[110];

inline bool PosibilBrut()
{
	int i,j,k;
	bool ok,gasit;
	for(i=1;i<=n;i++)
	{
		for(j=1;j<=m;j++)
		{
			gasit=false;
			ok=true;
			for(k=1;k<=m && ok;k++)
				if(mat[i][k]>mat[i][j])
					ok=false;
			if(ok)
				gasit=true;
			else
			{
				ok=true;
				for(k=1;k<=n && ok;k++)
					if(mat[k][j]>mat[i][j])
						ok=false;
				if(ok)
					gasit=true;
			}
			if(!gasit)
				return false;
		}
	}
	return true;
}

inline bool Posibil()
{
	int i,j;
	for(i=1;i<=n;i++)
	{
		maximL[i]=0;
		for(j=1;j<=m;j++)
			maximL[i]=max(maximL[i],mat[i][j]);
	}
	for(j=1;j<=m;j++)
	{
		maximC[j]=0;
		for(i=1;i<=n;i++)
			maximC[j]=max(maximC[j],mat[i][j]);
	}
	for(i=1;i<=n;i++)
		for(j=1;j<=m;j++)
			if(mat[i][j]!=maximL[i] && mat[i][j]!=maximC[j])
				return false;
	return true;
}

int main()
{
	int i,j,t;
	ifstream fin("B.in");
	ofstream fout("B.out");
	fin>>T;
	for(t=1;t<=T;t++)
	{
		fin>>n>>m;
		for(i=1;i<=n;i++)
			for(j=1;j<=m;j++)
				fin>>mat[i][j];
		if(Posibil())
			fout<<"Case #"<<t<<": YES\n";
		else
			fout<<"Case #"<<t<<": NO\n";
	}
	fin.close();
	fout.close();
	return 0;
}
